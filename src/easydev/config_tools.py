# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://www.assembla.com/spaces/pyeasydev/wiki
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""
.. testsetup::

    from easydev.config_tools import *

"""
from ConfigParser import ConfigParser
import os
from collections import OrderedDict

__all__ = ["OrderedDictAttribute", "DynamicConfigParser", "ConfigExample"]


class OrderedDictAttribute(OrderedDict):
    """This is an extension of :class:`~collections.OrderedDict` class with key as read/write attribute
    
    Consider the following example. The key **test** can be altered
    as a normal attribute. 
    
    .. doctest::

        >>> from easydev.config_tools import OrderedDictAttribute   
        >>> o = OrderedDictAttribute()    
        >>> o['test'] = 1
        >>> o.test   # equivalent to o['test']
        1
        >>> o.test = 1 # equivalent to o['test'] = 1
        
    .. warning:: the key-attribute can be altered **only** if already
        added in the dictionary itself.
        
    .. doctest::

        >>> from easydev.config_tools import OrderedDictAttribute
        >>> o = OrderedDictAttribute() # o['test'] = 1; let us omit this required step
        >>> o.test = 1 #doctst: +SKIP
        >>> o.test     #doctest: +SKIP this is an attribute (not a key)
        1
        >>> o.has_key("test")
        False 
        
    .. todo:: when setting an attribute that is not a key, we could
        add it in the dictionary.
        
    """
    def __init__(self, *args, **kwds):
        super(OrderedDictAttribute, self).__init__(*args, **kwds)
        
        # The spirit of this class is to have a mapping between keys and 
        # an attribute with the same name. Yet, one can set an attribute
        # while the key hasnot yet been set, which is not expected usage
        
        # FIXME one could solve this issue by creating the key on the fly.
        
        # meanwhile, we will use a print statement to inform the user that this attribute
        # is not yet a key. 
        
        # Yet, when we create an instance of this class, the message will 
        # be printed. To prevent this, we use th e _init attribute below
        # and catch its presence in the __setattr__ method
        self._init = True  # used in set attributete to figure out if

    def __getattr__(self, attr):
        if self.has_key(attr):
            return super(OrderedDictAttribute, self).__getitem__(attr)
        else:
            return super(OrderedDictAttribute, self).__getattr__(attr)
    def __setattr__(self, attr, value):
        if self.has_key(attr):
            return super(OrderedDictAttribute, self).__setitem__(attr, value)
        else:
            if "_init" in self.__dict__.keys():
                print("warning: attribute {} not in the dictionary yet.".format(attr))
                print("If you want this attribute to be in the dictionary, you must add it first as a key")
            
            return super(OrderedDictAttribute, self).__setattr__(attr, value)

    
                     

class ConfigExample(object):
    """Create a simple example of ConfigParser instance to play with

    ::

        >>> from easydev.pipeline.config import ConfigExample
        >>> c = ConfigExample().config  # The ConfigParser instance
        >>> assert 'General' in c.sections()
        >>> assert 'GA' in c.sections()

    This example builds up a ConfigParser instance from scratch.

    This is equivalent to having the following input file::

        [General]
        verbose = True
        tag = test

        [GA]
        popsize = 1


    which can be read with ConfigParser as follows::

        >>> from ConfigParser import ConfigParser
        >>> config = ConfigParser()
        >>> config.read("file.ini")


    """
    def __init__(self):
        self.config = ConfigParser()
        self.config.add_section('General')
        self.config.set('General', 'verbose', 'true')
        self.config.add_section('GA')
        self.config.set('GA', 'popsize', '50')




class DynamicConfigParser(ConfigParser):
    """Enhanced version of Config Parser

    Provide some aliases to the original ConfigParser class and
    new methods such as :meth:`save` to save the config object in a file.

    ::

        >>> from easydev.config_tools import ConfigExample
        >>> standard_config_file = ConfigExample().config
        >>> c = DynamicConfigParser(standard_config_file)
        >>>
        >>> # then to get the sections, simply type as you would normally do with ConfigParser
        >>> c.sections()
        >>> # or for the options of a specific sections:
        >>> c.get_options('General')

    You can now also directly access to an option as follows::

        >>> c.General.tag

    Then, you can add or remove sections (:meth:`remove_section`, :meth:`add_section`),
    or option from a section :meth:`remove_option`. You can save the instance into a file
    or print it::

    >>> print c

    .. warning:: if you set options manually (e.G. self.GA.test =1 if GA is a 
        section and test one of its options), then the save/write does not work
        at the moment even though if you typoe self.GA.test, it has the correct value
        

    Methods inhereited from ConfigParser are available:

    ::
    
        # set value of an option in a section
        c.set(section, option, value=None)
        # but with this class, you can also use the attribute
        c.section.option = value
        
        # set value of an option in a section
        c.remove_option(section, option)
        c.remove_section(section)
        
    
    """
    def __init__(self, config_or_filename=None):
        # why not a super usage here ? Maybe there wee issues related to old style class ?
        ConfigParser.__init__(self)
        
        # I'm hacking the ConfigParser to replace the _sections OrderedDict
        # by an OrderedDictAttribute to easily access to sections.
        self._sections = OrderedDictAttribute()

        
        self._config = None
        # set the sections and options
        if type(config_or_filename) == str:
            self.read(config_or_filename)
        elif isinstance(config_or_filename, ConfigParser):
            config = config_or_filename
            self._replace_config(config)
        elif config_or_filename == None:
            pass
        else:
            raise TypeError("config_or_filename must be a valid filename or valid ConfigParser instance")

    def read(self, filename):
        """Load a new config from a filename (remove all previous sections)"""
        if os.path.isfile("test.ini")==False:
            raise IOError("filename {} not found".format(filename))
            
        config = ConfigParser()
        config.read(filename)
        
        self._replace_config(config)

    def _replace_config(self, config):
        """Remove all sections and add those from the input config file

        :param config:

        """
        for section in self.sections():
            self.remove_section(section)
            
        for section in config.sections():
            self.add_section(section)
            for option in config.options(section):
                data = config.get(section, option)
                self.set(section, option, data)

    def get_options(self, section):
        """Alias to get all options of a section in a dictionary
    
        One would normally need to extra each option manually::

            for option in config.options(section):
                config.get(section, option, raw=True)#
                
        then, populate a dictionary and finally take care of the types.
        
        .. warning:: types may be changed .For instance the string "True" 
            is interepreted as a True boolean.

        ..  seealso:: internally, this method uses :meth:`section2dict` 
        """
        return self.section2dict(section)

    def section2dict(self, section):
        """utility that extract options of a ConfigParser section into a dictionary

        :param ConfigParser config: a ConfigParser instance
        :param str section: the section to extract

        :returns: a dictionary where key/value contains all the options/values of the section required

        Let us build up  a standard config file::

            >>> import ConfigParser
            >>> c = ConfigParser.ConfigParser()
            >>> c.add_section('general')
            >>> c.set('general', 'step', str(1))
            >>> c.set('general', 'verbose', 'True')

        To access to the step options, you would write::

            >>> c.get('general', 'step')

        this function returns a dictionary that may be manipulated as follows::

            >>> d_dict.general.step

        .. note:: a value (string) found to be True, Yes, true, yes is transformed to True
        .. note:: a value (string) found to be False, No, no, false is transformed to False
        .. note:: a value (string) found to be None; none, "" (empty string) is set to None
        .. note:: an integer, or float is transformed to float
        """
        options = {}
        for option in self.options(section):
            data = self.get(section, option, raw=True)
            if data in ['True', 'Yes', 'true', 'yes']:
                options[option] = True
            elif data in ['False', 'false', 'no', 'No']:
                options[option] = False
            elif data in ['None', None, 'none', '']:
                options[option] = None
            else:
                try: # numbers
                    options[option] = self.getfloat(section, option)
                except: #string
                    options[option] = self.get(section, option, raw=True)
        return options

    def save(self, filename):
        """Save all sections/options to a file.

        :param str filename: a valid filename
  
        ::
         
            config = ConfigParams('config.ini') #doctest: +SKIP
            config.save('config2.ini') #doctest: +SKIP
   
        """
        try:
            if os.path.exists(filename) == True:
                print "Warning: over-writing %s " % filename
            fp = open(filename,'w')
        except Exception, e:
            print e
            raise Exception('filename could not be opened')
     
          
        self.write(fp)
        fp.close()

    def add_section(self, section):
        """add a section in the configuration file

        ::

            >>> c = DynamicConfigParser()
            >>> c.add_section("general")

        .. note:: this method overloads the parent's method to make sure
            that OrderedDict instance are AttributeOrdredDict.
        .. note:: here the section added is an :class:`OrderedDictAttribute`

        """
        if section in self._sections.keys():
            raise ValueError("Section {} already in the dictionary".format(section))
        else:
            self._sections[section] = OrderedDictAttribute()
        
    def add_option(self, section, option, value=None):
        """add an option to an existing section (with a value)

        ::

            >>> c = DynamicConfigParser()
            >>> c.add_section("general")
            >>> c.add_option("general", "verbose", True)
        """
        assert section in self.sections(), "unknown section"
        self.set(section, option, value=value)
    
    
    # no need for those methods anymore
    #def set(self, section, option, value=None):
    #    ConfigParser.set(self, section, option, value=value)

    # no need for those methods anymore
    #def remove_option(self, section, option):
    #    """Remove an option from a section"""
    #    ConfigParser.remove_option(self, section, option)

    #def remove_section(self, section):
    #    """Remove a section"""
    #    ConfigParser.remove_section(self, section)

    def __str__(self):
        str_ = ""
        for section in self.sections():
            str_ += '[' + section + ']\n'
            for option in self.options(section):
                 data = self.get(section, option, raw=True)
                 str_ += option + ' = ' + str(data)+'\n'
            str_ += '\n\n'

        return str_

    def __getattr__(self, key):
        if self._sections.has_key(key):
            return self._sections[key]
        else:
            return getattr(ConfigParser, key)
            #.__dict__[key]
            # does not work probably because old-style class
            #return super(DynamicConfigParser, self).__getattribute__(key)
             

    def __eq__(self, data):
        # FIXME if you read file, the string "True" is a string
        # but you may want it to be converted to a True boolean value
        if sorted(data.sections()) != sorted(self.sections()):
            print("Sections differ")
            return False
        for section in self.sections():

            for option in self.options(section):
                try:
                    if str(self.get(section, option,raw=True)) != \
                        str(data.get(section,option, raw=True)):
                        print("option %s in section %s differ" % (option, section))
                        return False
                except:
                    return False
        return True

