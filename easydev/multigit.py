# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/cokelaer/easydev
#
##############################################################################
import glob
import sys
import os
from easydev.console import red, darkgreen, purple


# could use argparse

class MultiGIT(object):
    """A multi git command line

    You can either use MultiGIT as an executable (installed with easydev) and type the following
    command in a shell::

        multigit --help

    or create a script as follows in the repository that contains the git repositories::

        from easydev.multigit import MultiGIT
        import sys
        if __name__ == "__main__":
            dirs = ['easydev', 'bioservices']
            mg = MultiGIT(commands=sys.argv[1:], directories=dirs)

    You can then call the local script (e.g. for the pull command)::

        python multigit.py pull

    This would be equivalent to calling the executable as follows::

        multigit pull --directories easydev bioservices

    """
    def __init__(self, commands, directories=None, curdir='.', verbose=True):

        """Simple utility to apply a git command to all local directories"""

        self.verbose = verbose
        self.commands = commands
        # catch the multigit commands that is
        # --quiet (which is also a valid git option),
        # --help, which is also a git option; replaces the git --help
        #  --directories
        #  --exclude-directories
        if '-h' in self.commands or '--help' in self.commands:
            MultiGIT.help()
            sys.exit()

        if "--quiet" in self.commands:
            self.verbose = False

        if "--directories" in self.commands:
            directories = self._get_arguments('--directories')
            self.commands.remove("--directories")
            for this in directories:
                self.commands.remove(this)

        if "--exclude-directories" in self.commands:
            exclude_directories = self._get_arguments('--exclude-directories')
            self.commands.remove("--exclude-directories")
            for this in exclude_directories:
                self.commands.remove(this)
        else:
            exclude_directories = []

        # look for all directories by default
        if directories is None:
            directories = glob.glob('*')
            directories = [x for x in directories if os.path.isdir(x)]
        self.directories = [x for x in directories if x not in exclude_directories]


        self.commands = " ".join(self.commands)
        cmds = self.commands
        if len(cmds) == 0:
            print("No commands provided...")
            MultiGIT.help()
        else:
            if ' -h' not in cmds and ' --help' not in cmds:
                self.run()

    def _get_arguments(self, cmd):
        # identify
        index = self.commands.index(cmd)
        args = []
        for this in self.commands[index+1:]:
            if this.strip().startswith('-'):
                break
            else:
                args.append(this.strip())
        return args

    def run(self):
        """call the git commands """
        results = {'failure': [], 'success': []}

        for directory in self.directories:
            if self.verbose:
                print(purple("Entering in {0}".format(directory)))
            code = "cd {0}; git {1}".format(directory, self.commands)

            try:
                if self.verbose:
                    print(code)
                status = os.system(code)
                if status == 0:
                    results['success'].append(directory)
                    self._print_status('ok')

                else:
                    print(directory + " failed\n")
                    results['failure'].append(directory)
                    self._print_error("Failed. Skipped")
            except:
                print(directory + "failed\n")
                results['failure'].append(directory)
                self._print_error("Failed. Skipped")
            finally:
                code = "cd .."
                os.system(code)
                if self.verbose:
                    print("")
            if self.commands == 'help':
                break
        if len(results['failure']):
            print("Failed repos: " + str(results['failure']))

    def _print_status(self, msg):
        if self.verbose is False:
            return
        try:
            print(darkgreen(msg))
        except:
            print(msg)
    def _print_error(self, msg):
        if self.verbose is False:
            return
        try:

            print(red(msg))
        except:
            print(msg)

    @classmethod
    def help(cls):
        """help: to get more help and usage
        """
        print("""

        MultiGIT allows to apply git commands on a set of directories.
        This could be quite useful if you keep all your GIT repositories within
        a single directory for instance to pull new commits systematically

        Examples:
        ---------

            >>> python multigit.py pull --directories test,easydev,requests

        Global options:
          --quiet                 do not show setup outputs [default=False]

        Options not yet implemented:

          --keep-going            force the commands running[default=False]
          --help               show detailed help message
          --directories           list of directories to look at [default: all]
          --exclude-directories   list of directories to ignore

        print "usage: multigit.py pull --directories
        """)


def main_func(args=None):
    if args:
        pass
    else:
        args = sys.argv[1:]  # 1 ignore the name of the calling program itself

    if len(args) == 0:
        print(red("USAGE: python multigit.py pull"))
    else:
        MultiGIT(args)


if __name__ == "__main__":
    args = sys.argv[1:] # 1 ignore the name of the calling program itself
    main_func(args)




