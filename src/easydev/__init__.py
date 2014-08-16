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
from __future__ import print_function

__version__ = "$Rev$"

import pkg_resources
try:
    version = pkg_resources.require("easydev")[0].version
except:
    version = __version__

from . import xfree86
from .xfree86 import *


try:
    import colors
    from .colors import *
except:
    print("colors module depends on pylab, which does not seem to be installed. skipped")

import copybutton
from .copybutton import *

import decorators
from .decorators import *

import doc
from .doc import *

import easytest
from .easytest import *

import logging_tools
from .logging_tools import *

import sphinx_themes
from .sphinx_themes import *

import tools
from .tools import *

import multisetup

import paths
from .paths import *

import package
from .package import *

import config_tools
from .config_tools import *

import url
from .url import *

#import dependencies
from .dependencies import get_dependencies

import multicore
from .multicore import *

# use local import to not clash with setuptools itself.
from .setuptools import get_datafiles
