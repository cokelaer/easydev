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
#  Website: https://www.assembla.com/spaces/pyeasydev/wiki
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""Common tools to ease access to a common sphinx theme."""
import os
from os.path import join as pj

__all__ = ["get_path_sphinx_themes"]

def get_path_sphinx_themes():
    """Return the path where the sphinx themes can be found

    .. doctest::

        >>> from easydev import sphinx_themes
        >>> themes = sphinx_themes.get_path_sphinx_themes()
        >>> 'cno' in themes
        True

    """
    import easydev
    sharedir = easydev.get_shared_directory_path("easydev")
    sharedir = os.path.join(sharedir, "themes")
    return sharedir



