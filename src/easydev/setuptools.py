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
#  Website: https://github.com/cokelaer/easydev
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""Utilities to help designing the setuptools

unfortunately, this means that easydev must be installed before hand.
May not be very useful.

"""
import os
import fnmatch

__all__ = ["get_datafiles"]


def get_datafiles(directory="share", match="*"):
    """builds list of data files to be with data_files in setuptools


    A typical task in a setup.py file is to set the path and name of a list
    of data files to provide with the package. For instance files in share/data
    directory. One difficulty is to find those files recursively. This can be
    achieved with os.walk or glob. Here is a simple function that perform this
    task.

    .. todo:: exclude pattern
    """
    datafiles = []
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, match):
            matches.append(os.path.join(root, filename))
            this_filename = os.path.join(root, filename)
            datafiles.append((root, [this_filename]))
    return datafiles
