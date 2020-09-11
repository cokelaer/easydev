# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2017
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://github.com/cokelaer/easydev
#  Documentation: http://easydev-python.readthedocs.io
#
##############################################################################
import os
from easydev.logging_tools import Logging

__all__ = ["PackageBuilder"]



setup_template1 = """# -*- coding: utf-8 -*-
__revision__ = "$Id$" # for the SVN Id
import sys
import os
from setuptools import setup, find_packages
import glob

_MAJOR               = %(MAJOR)s
_MINOR               = %(MINOR)s
_MICRO               = %(MICRO)s
version              = '%%d.%%d.%%d' %% (_MAJOR, _MINOR, _MICRO)
release              = '%%d.%%d' %% (_MAJOR, _MINOR)

metainfo = {
    'authors': {"main": ("%(author)s", "%(email)s")},
    'version': version,
    'license' : 'GPL',
    'download_url' : ['http://pypi.python.org/pypi/%(name)s'],
    'url' : ["http://pythonhosted.org/%(name)s/"],
    'description': "%(description)s" ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    'keywords' : [''],
    'classifiers' : [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics']
    }

# files in share/data
datadir = os.path.join('share','data')
datafiles = [(datadir, [f for f in glob.glob(os.path.join(datadir, '*'))])]

"""


setup_template2 = """
setup(
    name             = "%(name)s",
    version          = version,
    maintainer       = metainfo['authors']['main'][0],
    maintainer_email = metainfo['authors']['main'][1],
    author           = metainfo['authors']['main'][0],
    author_email     = metainfo['authors']['main'][1],
    long_description = open("README.txt").read(),
    keywords         = metainfo['keywords'],
    description      = metainfo['description'],
    license          = metainfo['license'],
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    download_url     = metainfo['download_url'],
    classifiers      = metainfo['classifiers'],

    # package installation
    package_dir = {'':'src'},
    packages = ["%(pkgname)s"],

    install_requires = %(install_require)s,

    # uncomment if you have share/data files
    #data_files = datafiles,

    #use_2to3 = True, # causes issue with nosetests
)
"""

setup_template3 = """
namespace = '%(namespace)s'

# messy but works for namespaces under Python 2.7
pkgs = [pkg for pkg in find_packages("src")]
top_pkgs = [pkg for pkg in pkgs if  len(pkg.split('.')) < 2]
package_dir = {"": "src"}
for pkg in top_pkgs:
    package_dir[namespace + "." + pkg] = "src" + os.sep + pkg

setup(
    name             = "%(name)s",
    version          = version,
    maintainer       = metainfo['authors']['main'][0],
    maintainer_email = metainfo['authors']['main'][1],
    author           = metainfo['authors']['main'][0],
    author_email     = metainfo['authors']['main'][1],
    long_description = open("README.txt").read(),
    keywords         = metainfo['keywords'],
    description      = metainfo['description'],
    license          = metainfo['license'],
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    download_url     = metainfo['download_url'],
    classifiers      = metainfo['classifiers'],

    # package installation
    package_dir = package_dir,
    packages = find_packages("src"),
    namespace_packages = [namespace],

    install_requires = %(install_require)s,
    # uncomment if you have share/data files
    #data_files = datafiles,

    #use_2to3 = True, # causes issue with nosetests
)
"""


namespace_init_template = """try:
    __import__('pkg_resources').declare_namespace(__name__)
except:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
"""

namespace_init_pkg_template = """# Redirect path
import os
cdir = os.path.dirname(__file__)
pdir = os.path.join(cdir, "../../%(pkgname)s")
pdir = os.path.abspath(pdir)

__path__ = [pdir] + __path__[:]

from %(namespace)s.%(pkgname)s.__init__ import *
del cdir
del pdir
"""


setup_cfg_template = """
[build_sphinx]
source_dir = doc/source
build_dir  = doc/build
all_files  = 1

[nosetests]
where=test
with_coverage=
cover_package=%(name)s
cover_erase=
verbosity=2
;cover_html=
;cover_html_dir=html
logging_level=ERROR

[upload_docs]
upload_dir=doc/build/html/
"""



class PackageBuilder(object):
    """simple class to automatically build a package layout

    .. doctest::
        :options: +SKIP

        >>> from easydev import PackageBuilder
        >>> p = PackageBuilder(name="testpackage")
        >>> p.buildPackage()

    For the time being, this example creates the following layout::

        pkg/
        |-- doc
        |   |-- source
        |   |-- _static
        |-- README.txt
        |-- setup.py
        |-- share
        |     |-- data
        |-- src
        |     |-- pkg
        |         |-- __init__.py
        |-- test

    You can avoid the shared directory creation.
    The namespace is not implemented so far.
    The doc directory is empty so far.

    The version is set to 0.0.1

    Metainfo in the setup file need to be filed but the package should already be functional.

    New modules can be added inside the src/pkgname directory.
    """
    def __init__(self, name, share=True, namespace=None):
        """.. rubric:: Constructor


        :param str name:
        :param str share:
        """
        self.pkgname = name   # can be only the pkg name without namespace
        self.name = name      # can be pkg or namespace.pkg
        self.share = share
        self.namespace = namespace

        self.metainfo = {
                "pkgname": self.pkgname,
                "name":self.pkgname,
                "version": "version",
                "MINOR": '0',
                "MAJOR": '0',
                "MICRO": '1',
                "install_require": '[]',
                "description": "Put a short description here",
                "author": "yourname",
                "email": "email@whatever.org",
                "namespace": self.namespace,
        }
        if self.namespace:
            self.metainfo["name"] = ".".join([self.namespace, self.pkgname])
            self.metainfo["url"] = os.sep.join([self.namespace, self.pkgname])
        self.logging = Logging("INFO")
                    #self.init()

    def init(self, force=False):
        self.logging.info("Creating the package directory")
        if os.path.isdir(self.pkgname):
            self.logging.warning("Directory %s already exists." % self.pkgname)
            self.logging.warning("You are about to delete this directory %s. " % self.pkgname)
            if force==True:
                res = "y"
            else:
                res = raw_input("Do you wish to proceed (y/n)?")
            if res == "y":
                import shutil
                shutil.rmtree(self.pkgname)
                os.mkdir(self.pkgname)
                return True
            else:
                return False
        else:
            os.mkdir(self.pkgname)
            return True

    def create_namespace(self): #pragma: no cover
        if self.namespace == None:
            self.logging.warning("namespace is not set, cannot create namespace directories")
            return

        dir1 = "src" + os.sep + self.namespace
        dir2 = "src" + os.sep + self.namespace + os.sep + self.pkgname

        self._mkdir(dir1)
        self._mkdir(dir2)
        f = open(self.pkgname + os.sep + dir1 + os.sep + "__init__.py", "w")
        f.write(namespace_init_template)
        f.close()

        f = open(self.pkgname + os.sep + dir2 + os.sep + "__init__.py", "w")
        f.write(namespace_init_pkg_template % self.metainfo)
        f.close()

    def create_setup(self):
        """Creates a setup.py file"""
        self.logging.info("Creating the setup.py file (you will need to update the metadata!")
        filename = self.pkgname + os.sep + "setup.py"
        f = open(filename, "w")
        f.write(setup_template1 % self.metainfo)
        if self.namespace == None:
            f.write(setup_template2 % self.metainfo)
        else:
            f.write(setup_template3 % self.metainfo)
        f.close()

        # config file
        filename = self.pkgname + os.sep + "setup.cfg"
        f = open(filename, "w")
        f.write("# a setup configuration")
        f.write(setup_cfg_template % self.metainfo)
        f.close()

    def create_readme(self):
        """Creates a README file"""
        self.logging.info("Creating a README file")
        filename = self.pkgname + os.sep + "README.txt"
        f = open(filename, "w")
        f.write("""Provide some information to users about this package.""")
        f.close()

    def create_sphinx_directory(self):
        """Create layout for sphinx documentation"""
        self._mkdir("doc")
        self._mkdir("doc" + os.sep + "source")
        self._mkdir("doc" + os.sep + "_static")

    def create_test_directory(self):
        """Create a test directory"""
        self._mkdir("test")

    def _mkdir(self, name):
        filename = self.pkgname + os.sep
        self.logging.info("Creating a directory %s " % (filename + name))
        os.mkdir(filename + name)

    def create_src_directory(self):
        """Create a source directory and empty __init__ file"""
        self._mkdir("src")
        dirname = "src" + os.sep + self.pkgname
        self._mkdir(dirname)
        dirname = self.pkgname + os.sep + dirname
        self.logging.info("Create %s/__init__ file " % dirname)
        f = open(dirname + os.sep + "__init__.py", "w")
        f.write("""__version__ = "$Rev: 10 $"
import pkg_resources
try:
    version = pkg_resources.require("%(name)s")[0].version
except:
    version = __version__
""" % self.metainfo)

        f.close()

    def create_share_directory(self):
        """Create share/data directory if required"""
        self._mkdir("share")
        self._mkdir("share" + os.sep + "data")

    def buildPackage(self, force=False):
        """Builds the entire package

        This function removes the directory "pkgname" if it exists,
        to create it back (empty), and then calsl the methods starting with "create" word.
        """
        res = self.init(force=force)
        if res == False:
            return
        self.create_setup()
        self.create_readme()
        self.create_sphinx_directory()
        self.create_test_directory()
        self.create_src_directory()
        if self.share:
            self.create_share_directory()
        if self.namespace:
            self.create_namespace()


import argparse
class OptionsBuildPackage(argparse.ArgumentParser):
    """Options Parser for BuildPackage

    """
    def  __init__(self, args, version="1.0", prog="easydev_buildPackage"):
        usage = """USAGE: %s --pkgname pkgName""" % prog
        super(OptionsBuildPackage, self).__init__(usage=usage, prog=prog)
        self.add_general_options()
        self.options = self.parse_args(args)
        self.version = version

    def add_general_options(self):
        #self.add_argument('--version',
        #        action='version', version=self.version)
        self.add_argument("--pkgname", dest="pkgname",
            help="Name of the package to be created")
        self.add_argument("--package", dest="pkgname",
            help="Name of the package to be created")
        self.add_argument("--namespace", dest="namespace", default=None,
            help="If provided, creates a namespace.")
        self.add_argument("--no-share-directory", action="store_false",
            help="if five, the share directory is not created")
        self.add_argument("--verbosity", dest="verbosity", default="INFO",
            help="set verbosity to INFO, WARNING or ERROR")

def buildPackage():
    """The executable easydev_buildPackage """
    import sys
    if len(sys.argv) > 1:
        parser = OptionsBuildPackage(sys.argv[1:])

        p = PackageBuilder(
            name=parser.options.pkgname,
            share=parser.options.no_share_directory,
            namespace=parser.options.namespace)
        p.logging.debugLevel = parser.options.verbosity
        p.buildPackage()
    else:
        parser = OptionsBuildPackage(["--help"])

