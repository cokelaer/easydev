# -*- python -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2012-2013
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: https://pypi.python.org/pypi/easydev
#
##############################################################################
# $Id: config.py 2002 2012-08-06 16:19:09Z cokelaer $
"""

.. testsetup::

    from easydev.config_tools import *

"""
from ConfigParser import ConfigParser
import os
from collections import OrderedDict

__all__ = ["DynamicConfigParser", "ConfigExample"]


class DictAttribute(OrderedDict):
    def __init__(self, *args, **kwds):
        super(DictAttribute, self).__init__(*args, **kwds)

    def __getattr__(self, attr):
        if self.has_key(attr):
            return super(DictAttribute, self).__getitem__(attr)
        else:
            return super(DictAttribute, self).__getattr__(attr)
    def __setattr__(self, attr, value):
        if self.has_key(attr):
            return super(DictAttribute, self).__setitem__(attr, value)
        else:
            return super(DictAttribute, self).__setattr__(attr, value)

    
                     

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
        >>> config.read(filename)


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

    """
    def __init__(self, config_or_filename=None):
        ConfigParser.__init__(self)
        self._sections = DictAttribute()

        self._config = None
        # set the sections and options
        if type(config_or_filename) == str:
            self.load_ini(config_or_filename)
        elif isinstance(config_or_filename, ConfigParser):
            config = config_or_filename
            self.replace_config(config)
        elif config_or_filename == None:
            pass
        else:
            raise TypeError("config_or_filename must be a valid filename or valid ConfigParser instance")


    def load(self, filename):
        self.load_ini(filename)

    def load_ini(self, filename):
        """Load a new config from a filename (remove all previous sections)"""
        config = ConfigParser()
        try:
            config.read(filename)
        except IOError, e:
            print e
        self.replace_config(config)

    def replace_config(self, config):
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
        """Alias to get options of a section

        One would normally do::

            for option in config.options(section):
                config.get(section, option, raw=True)

        taking care of types as well.

        """
        return getattr(self, section).__dict__

    def _section2dict(self, section):
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
        """

        :param str filename: a valid filename
  
          >>> config = ConfigParams('config.ini') #doctest: +SKIP
          >>> config.save('config2.ini') #doctest: +SKIP
   
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


        """
        if section in self._sections.keys():
            raise ValueError()
        else:
            self._sections[section] = DictAttribute()
        

    def add_option(self, section, option, value=None):
        """add an option in an existing section (with a value)

        ::

            >>> c = DynamicConfigParser()
            >>> c.add_section("general")
            >>> c.add_option("general", "verbose", True)
        """
        assert section in self.sections(), "unknown section"
        self.set(section, option, value=value)

    def set(self, section, option, value=None):
        ConfigParser.set(self, section, option, value=value)

    def remove_option(self, section, option):
        """Remove an option from a section"""
        ConfigParser.remove_option(self, section, option)

    def remove_section(self, section):
        """Remove a section"""
        ConfigParser.remove_section(self, section)

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
            return super(DynamicConfigParser, self).__getattr__(attr)

    def __eq__(self, data):
        if data.sections() != self.sections():
            print("sections differ")
            return False
        for section in self.sections():
            try:
                if section not in data.sections():
                    print("sections differ2")
                    return False
            except:
                print "%s not in RHS config file" % section
                return False
            for option in self.options(section):
                try:
                    if str(self.get(section, option,raw=True)) != \
                        str(data.get(section,option, raw=True)):
                        print("option %s in section %s differ" % (option, section))
                        return False
                except:
                    return False
        return True

