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
#  Documentation: http://easydev-python.readthedocs.io
#
##############################################################################

import importlib.metadata

__all__ = ["get_dependencies"]


def get_dependencies(pkgname):
    """Return dependencies of a package as a sorted list

    :param str pkgname: package name
    :return: list (empty list if no dependencies)
    """
    try:

        res = importlib.metadata.requires(pkgname)
        res = [x.split()[0] for x in res]
        res = list(set(res))
        res.sort()
        return res
    except Exception:
        return []
