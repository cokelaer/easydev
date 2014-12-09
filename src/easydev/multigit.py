# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2011-2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/easydev
#
##############################################################################
import glob
import sys
import os
from easydev.console import red, darkgreen, purple


class MultiGIT(object):
    """A multi git command line

    In a directory with plenty of git repositories, create this script
    and execute it as you would do with git::

        from easydev.multigit import MultiGIT
        import sys
        if __name__ == "__main__":
            dirs = ['easydev', 'bioservices']
            mg = MultiGIT(commands=sys.argv[1:], directories=dirs)

    For instance::

        python multigit.py pull


    """
    def __init__(self, commands, directories=None, curdir='.', verbose=True):

        """Simple utility to apply a git command to all local directories"""

        self.verbose = verbose
        # catch the multigit commands that is
        # --quiet (which is also a valid git option),
        #  --keep-going
        # --help, which is also a git option; replaces the git --help
        #  --directories
        #  --exclude-directories
        if '-h' in commands or '--help' in commands:
            MultiGIT.help()

        if "--quiet" in commands:
            self.verbose = False

        if "--directories" in commands:
            commands.remove("--directories")
            raise NotImplementedError

        if "--exclude-directories" in commands:
            commands.remove("--exclude-directories")
            raise NotImplementedError

        if "--keep-going" in commands:
            commands.remove("--keep-going")
            raise NotImplementedError

        self.commands = " ".join(commands)

        # look for all directories by default
        if directories is None:
            directories = glob.glob('*')
            directories = [x for x in directories if os.path.isdir(x)]
        self.directories = directories

        if ' -h' not in self.commands and ' --help' not in self.commands:
            self.run()

    def run(self):
        failed = []
        for directory in self.directories:
            if self.verbose:
                print(purple("Entering in {0}".format(directory)))
            code = "cd {0}; git {1}".format(directory, self.commands)
            try:
                if self.verbose:
                    print(code)
                status = os.system(code)
                if status == 0:
                    if self.verbose:
                        print((darkgreen('ok')))
                else:
                    if self.verbose:
                        print(red('Failed. Skipped'))
            except:
                failed.append(directory)
                if self.verbose:
                    print(red("Failed. Skipped"))
            finally:
                code = "cd .."
                os.system(code)
                if self.verbose:
                    print("")

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




if __name__ == "__main__":
    args = sys.argv[1:]  # 1 ignore the name of the calling program itself

    if len(args)==0:
        print(red("USAGE: python multigit.py pull"))
    else:
        MultiGIT(args)




