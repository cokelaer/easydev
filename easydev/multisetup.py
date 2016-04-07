# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2013
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://github.com/cokelaer/easydev
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""Calling setup.py recursively and/or in multi python packages.

The commands are similar to those expected by setup.py. In addition,
there are a few commands dedicated to multisetup (see --help).

:Example:

    .. doctest::
        :options: +SKIP

        >>> python multisetup install --quiet
        >>> python multisetup install sdist --dist-dir ../dist
        >>> python multisetup --keep-going install sdist --dist-dir ../dist


Based on OpenAlea.Misc http://openalea.gforge.inria.fr

"""

__license__ = "GPLv3"
__revision__ = "$Id$"

import sys
import os
from subprocess import PIPE, Popen


try:
    from easydev.console import bold, red, green, \
        color_terminal, nocolor, underline, purple
except ImportError:
    pass


"""
  args = sys.argv[1:]
    if  len(args) == 1 and args[0] in ['-h', '--help']:
        Multisetup.help()
    else:
        if 'develop -u' in args:
            dirs.reverse()
"""

class Multisetup(object):
    """The main base class to build Multisetup instances


    In practice, you create a python script with this kind of code::

        if __name__ == "__main__"
            from easydev.multisetup import Multisetup
            import sys
            packages = ['pkg1', 'pkg2']
            mysetup = Multisetup(commands=sys.argv[1:], packages=packages)
            mysetup.run()


    """
    def __init__(self, commands, packages=None, curdir='.', verbose=True):
        """.. rubric:: Constructor

        :param commands: list of user commands or command (see :meth:`parse_commands`)
           accepted commands are --packages, --exclude-packages, -quiet, --keep-going
        :param list packages: list of packages to process
        :param str curdir: current directory default is .
        :param bool verbose: verbose option

        :type commands: a string or list of strings

        The argument `commands` must be a list of strings combining arguments
        from multisetup and setup.

        :Examples:

        .. doctest::
            :options: +SKIP

            >>> Multisetup("install --keep-going", ['pkg1', 'pkg2'], '.', verbose=True)
            >>> Multisetup(["install","--keep-going"], ['pkg1', 'pkg2'], '.', verbose=True)

        """
        if len(commands) == 1 and commands[0] in ['-h', '--help']:
            Multisetup.help()

        if 'develop -u' in " ".join(commands):
            packages.reverse()

        # default
        self.curdir = os.path.abspath(curdir)

        if isinstance(commands, list):
            self.commands = list(commands)

        elif isinstance(commands, str):
            self.commands = list(commands.split(" "))
        else:
            raise TypeError("commands argument must be a list of arguments or a string")

        self.packages = list(packages)
        self.verbose = verbose
        self.force = False

        # parsing user arguments
        self.parse_packages()

        # self.parse_intern_commands()
        self.parse_commands()


    @classmethod
    def help(cls):
        """help: to get more help and usage
        """
        print("""

        MultiSetup allows to build and install all the packages found in this
        directory usinf the same commands and setuptools.

        Examples:
        ---------

            # Developer mode : Installation of the pks from svn
            >>> python multisetup.py develop

            # User mode: Installation of the packages on the system as root
            >>> python multisetup.py install

            # Administrator mode: Create distribution of the packages
            >>> python multisetup.py nosetests -w test install bdist_egg -d ../dist sdist -d ../dist

        Common commands:
          multisetup.py sdist -d ./dist   will create a source distribution underneath 'dist/'
          multisetup.py install           will install the package

        Global options:
          --quiet                        do not show setup outputs [default=False]
          -k, --keep-going               force the commands running[default=False]
          -h, --help                     show detailed help message
         --packages                      list of packages to run
                                         [default: none]
          --exclude-packages             list of packages to not run

        print "usage: multisetup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
        """)


    def parse_packages(self):
        """Search and remove package(S) from multisetup command (e.g., --package)

        .. todo:: known issue: python multisetup.py --packages with two
            packages will be confused by following commands. Must be put
            at the end of the command
        """
        if '--packages' in self.commands:
            index = self.commands.index('--packages')
            self.commands.remove('--packages')
            self.packages = set()
            found = True
            while found is True:
                try: #test is no more argument
                    self.commands[index]
                except: # then breaks
                    break
                # otherwise if next argument starts with -, break
                if self.commands[index].startswith('-'):
                    break
                # or carry on to gather package names
                else:
                    self.packages.add(self.commands[index])
                    self.commands.remove(self.commands[index])
                    continue
            #self.commands.pop(index)

        if '--exclude-packages' in self.commands:
            # keep track of --exclude-package index
            index = self.commands.index('--exclude-packages')
            # remove it from the commands
            self.commands.remove('--exclude-packages')
            # remove all packages provided afterwards until next arguments is found
            found = True
            while found is True:
                # look for next argument/package that may be the end of the command
                try:
                    package_to_remove = self.commands[index]
                except:
                    break
                # if this is a valid package name
                if package_to_remove in self.packages:
                    # remove it from the package list
                    self.packages.remove(package_to_remove)
                    # and from the command line
                    self.commands.remove(package_to_remove)
                    # until we found another package
                    continue
                # otherwise, it is an argument that
                else:
                    #starts with a - sign
                    if package_to_remove.startswith('-'):
                        break
                    # or is invalid
                    raise ValueError('--exclude-packages error: package %s not found in package list' \
                        % self.commands[index])

            #self.commands.pop(index)


    def parse_commands(self):
        """Search and remove multisetup options

        Get the user command line arguments (self.commands) that are dedicated
        to multisetup such as --help, --quiet, --keep-going so that the
        remaining commands are fully comptatible with setuptools.
        """

        if '--quiet' in self.commands:
            self.verbose = False
            self.commands.remove('--quiet')

        if '-k' in self.commands:
            self.force = True
            self.commands.remove('-k')

        if '--keep-going' in self.commands:
            self.force = True
            self.commands.remove('--keep-going')

        L = len(self.commands)
        i = 0
        while (i < L):
            if self.commands[i].startswith('-'):
                try:
                    self.commands[i-1] = self.commands[i-1] + ' ' + self.commands[i] + ' ' + self.commands[i+1]
                    self.commands.pop(i)
                    self.commands.pop(i)
                except:
                    self.commands[i-1] = self.commands[i-1] + ' ' + self.commands[i]
                    self.commands.pop(i)
            else:
                i += 1
            L = len(self.commands)


    def run(self, color=True):
        """Executes 'python setup.py' with the user commands on all packages. """
        if color:
            try:
                from easydev.console import bold, red, green, \
                    color_terminal, nocolor, underline, purple
            except:
                try:
                    sys.path.insert(0, os.path.join('deploy', 'src',  'deploy'))
                    from console import bold, red, green, \
                        color_terminal, nocolor, underline, purple
                except:
                    pass
            if not color_terminal():
                # Windows' poor cmd box doesn't understand ANSI sequences
                nocolor()
        else:
            bold = purple = red = green = underline = str

        print(bold("Running multisetup version %s" % __revision__.split()[2]))

        #project_dir = self.curdir.basename()
        directories = [package for package in self.packages]


        print('Will process the following directories: ',)
        for directory in directories:
            print(bold(directory)),
            #print bold(directory.basename()),
        print('')


        try:
            for directory in directories:
                try:
                    os.chdir(directory)
                    print(underline('Entering %s package'
                          % os.path.basename(directory)))
                          #          % directory.basename())
                except OSError as err:
                    print(underline('Entering %s package'
                              % os.path.basename(directory)))
                    print(red("cannot find this directory (%s)"
                              % os.path.basename(directory)))
                    print(err)

                print('Python exec : ' , sys.executable)

                #print underline('Entering %s package' % directory.basename())
                for cmd in self.commands:
                    setup_command = '%s setup.py %s ' % (sys.executable,cmd)
                    print("\tExecuting " + setup_command + '...processing',)


                    #Run setup.py with user commands
                    outputs = None
                    errors = None
                    if self.verbose:
                        process = Popen(setup_command,
                                        shell=True)
                        status = process.wait()
                    else:
                        process = Popen(setup_command, stdout=PIPE, stderr=PIPE,
                                        shell=True)
                        #status = process.wait()
                        outputs, errors = process.communicate()
                    if process.returncode == 0:
                        print(green('done'))
                    else:
                        if not self.verbose:
                            print(red('\tFailed. ( error code %s) ' %
                                  (process.returncode)))
                            os.chdir(self.curdir)

                        if not self.force:
                            raise RuntimeError()

                    if 'pylint' in cmd:
                        if outputs is not None:
                            for x in outputs.split('\n'):
                                if x.startswith('Your code has been'):
                                    print(purple('\t%s' % x))
                    if 'nosetests' in cmd:
                        if errors is not None:
                            for x in errors.split('\n'):
                                if x.startswith('TOTAL'):
                                    res = x.replace('TOTAL', 'Total coverage')
                                    res = " ".join (res.split())
                                    print(purple('\t%s' % res))
                                if x.startswith('Ran'):
                                    print(purple('\t%s' % x))
                                if x.startswith('FAILED'):
                                    print(purple('\t%s' % x))
                        else:
                            print(purple('all right'))

                os.chdir(self.curdir)

        except RuntimeError:
            sys.exit()

        os.chdir(self.curdir)



