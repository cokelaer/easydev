# -*- coding: utf-8 -*-
__revision__ = "$Id: setup.py 3170 2013-01-16 14:57:19Z cokelaer $"
import sys
import os
from setuptools import setup, find_packages
import glob

_MAJOR               = 0
_MINOR               = 7
_MICRO               = 0
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
    'keywords' : ['sphinx', "package", "multisetup", "logging", "config",
        "hex2web", "web2hex", "hex2rgb", "rgb2hex", "rgb2hsv", "hsv2rgb", 
        "rgb2hls", "hls2rgb", "color", "pypi downloads" , "decorators"],
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


# TODO: files in share/data. Need a smarter mechanism (recursive)
datafiles = []
datadirs = [
        os.path.join('share'), 
        os.path.join('share', 'themes'), 
        os.path.join('share', 'themes', 'cno'),
        os.path.join('share', 'themes', 'cno', 'static'),
        os.path.join('share', 'themes', 'standard'),
        os.path.join('share', 'themes', 'standard', 'static')]

for datadir in datadirs:
    datafiles.append(
        (
            datadir, 
            [f for f in glob.glob(os.path.join(datadir, '*')) if not os.path.isdir(f)]
        )
    )


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
    package_dir = {'':'src'},
    packages = ['easydev'],

    # sphinx is not stricly speaking required but this is very useful to build documentation
    # once installed, one can just build the doc himself
    install_requires = ['sphinx', 'ordereddict'],

    # ordereddict is for python2.6 and below 

    # somehow, the google_head.html is found in themes/standard and themese/cno
    # directories thanks to the contents of datafiles variable but the ones from
    # themes/standard directory are not copied inside the distribution ?
    # using the MANIFEST.in solve the issue. However, data_files=datafiles is
    # still required for python setup.py install or pip install to copy the
    # share directory in the proper place. sure there will be a neat solution
    # one day 
    data_files = datafiles,

    entry_points = {
        'console_scripts': [
            'easydev_buildPackage=easydev.package:buildPackage',
        ]
        },


    use_2to3 = True, # causes issue with nosetests
    #use_2to3_on_doctests = False.
)




