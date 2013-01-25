# -*- python -*-
#
#  Copyright 2011 EBI
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
"""Common tools to get the correct filename and pathname. """
import pkg_resources
try:
    version = pkg_resources.require("easydev")[0].version
except:
    version = "unknown but installed somehow..."

import copybutton
from copybutton import *

import doc
from doc import *

import logging_tools
from logging_tools import *

import sphinx_themes
from sphinx_themes import *


import tools
from tools import *

import multisetup



import paths
from paths import *

