# -*- coding: utf-8 -*-
__revision__ = "$Id$"
import sys
import os
from setuptools import setup, find_packages
import glob

_MAJOR               = 0
_MINOR               = 9
_MICRO               = 30
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)

metainfo = {
    'authors': {'Cokelaer':('Thomas Cokelaer','cokelaer@ebi.ac.uk')},
    'version': version,
    'license' : 'GPL',
    'download_url' : ['http://pypi.python.org/pypi/easydev'],
    'url' : ["http://packages.python.org/easydev/"],
    'description':'Common utilities to ease the development of Python packages' ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    'keywords' : ["package", "multisetup", "logging", "config", "decorators",
        "multigit", "progressbar"],
    'classifiers' : [
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ]
    }


setup(
    name             = 'easydev',
    version          = version,
    maintainer       = metainfo['authors']['Cokelaer'][0],
    maintainer_email = metainfo['authors']['Cokelaer'][1],
    author           = metainfo['authors']['Cokelaer'][0],
    author_email     = metainfo['authors']['Cokelaer'][1],
    long_description = open("README.rst").read(),
    keywords         = metainfo['keywords'],
    description = metainfo['description'],
    license          = metainfo['license'],
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    download_url     = metainfo['download_url'],
    classifiers      = metainfo['classifiers'],

    # package installation
    packages = ['easydev', "easydev.share" ],
    # using pip, files inside ./easydev/share that are non Python will be
    # included as well. For a distribution (using setup sdist), the MANIFEST
    # must be updated accordingly
    include_package_data = True,
    package_data = {"easydev.share": [
                    "themes/standard/*html",
                    "themes/standard/static/*",
                    "themes/cno/*html", 
                    "themes/cno/static/*", 
                    "copybutton.js"]},

    install_requires = ['colorama', 'pexpect'],
    extras_require = {
	    'profiler': ["line_profiler_test"]
    },
    # somehow, the google_head.html is found in themes/standard and themese/cno
    # directories thanks to the contents of datafiles variable but the ones from
    # themes/standard directory are not copied inside the distribution ?
    # using the MANIFEST.in solve the issue. However, data_files=datafiles is
    # still required for python setup.py install or pip install to copy the
    # share directory in the proper place. sure there will be a neat solution
    # one day
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'easydev_buildPackage=easydev.package:buildPackage',
            'multigit=easydev.multigit:main_func',
            'browse=easydev.browser:main',
            'ibrowse=easydev.browser:main',
        ]
        },

)




