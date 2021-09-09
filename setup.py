import sys
import os
from setuptools import setup, find_packages
import glob

_MAJOR               = 0
_MINOR               = 12
_MICRO               = 0
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)

metainfo = {
    'authors': {'Cokelaer':('Thomas Cokelaer','thomas.cokelaer@pasteur.fr')},
    'version': version,
    'license' : 'new BSD',
    'download_url' :'http://github.com/cokelaer/easydev',
    'url' : "http://github.com/cokelaer/easydev",
    'description':'Common utilities to ease the development of Python packages' ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    'keywords' : ["multisetup", "logging", "config", "decorators",
        "multigit", "progressbar"],
    'classifiers' : [
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
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

    install_requires = ['colorama', 'pexpect', "colorlog"],
    extras_require = {
	    'profiler': ["line_profiler_test"]
    },
    tests_require=['pytest'],
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
            'browse=easydev.browser:main',
        ]
        },

)




