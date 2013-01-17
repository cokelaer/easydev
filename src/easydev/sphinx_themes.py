# -*- python -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2012 - EBI
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv2 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-2.0.html
#
#  website: http://www.ebi.ac.uk/~cokelaer/easydev
#
##############################################################################
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



