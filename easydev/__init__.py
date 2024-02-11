# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2024
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the BSD3 License.
#
#  Website: https://github.com/cokelaer/easydev
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
from importlib import metadata


def get_package_version(package_name):
    try:
        version = metadata.version(package_name)
        return version
    except metadata.PackageNotFoundError:
        return f"{package_name} not found"


version = get_package_version("easydev")

from . import (
    browser,
    chunks,
    codecs,
    config_tools,
    copybutton,
    decorators,
    doc,
    easytest,
    logging_tools,
    misc,
    multicore,
    options,
    paths,
    sphinx_themes,
    tools,
    url,
)
from .browser import browse as onweb
from .chunks import *
from .codecs import *
from .config_tools import *
from .copybutton import *
from .decorators import *

# import dependencies
from .dependencies import get_dependencies
from .doc import *
from .easytest import *
from .logging_tools import *
from .md5tools import md5
from .misc import *
from .multicore import *
from .options import *
from .paths import *
from .profiler import do_profile
from .progressbar import Progress, TextProgressBar, progress_bar
from .sphinx_themes import *
from .timer import Timer
from .tools import *
from .url import *
