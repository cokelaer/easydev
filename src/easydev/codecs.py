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
# $:Id $
"""various type convertors (e.g., list to string)"""


__all__ = ["tolist", "transform_into_list", "list2string"]


def transform_into_list(data):
    """deprecated. use :meth:`tolist`"""
    print("deprecated (easydev). Please use tolist()")
    return tolist(data)


def tolist(data, verbose=True):
    """Transform an object into a list if possible

    :param data: a list, tuple, or simple type (e.g. int)
    :return: a list

    - if the object is list or tuple, do nothing
    - if the object is not a list, we assume this is a primitive type and a list
      of length 1 is returned, the item being the parameter provided.

    ::

        >>> from easydev import transform_to_list
        >>> tolist(1)
        [1]
        >>> tolist([1,2])
        [1,2]


    """
    if isinstance(data, list) or isinstance(data, tuple):
        return data #nothing to do
    elif isinstance(data, float):
        return [data]
    elif isinstance(data, int):
        return [data]
    elif isinstance(data, str):
        return [data]
    else:
        try:
            data = data.tolist()
            return data
        except:
            if verbose:
                print("not known type. cast to list")
            return list(data)





def list2string(data, sep=",", space=True):
    """Transform a list into a string

    :param list data: list of items that have a string representation.
        the input data could also be a simple object, in which case
        it is simply returned with a cast into a string
    :param str sep: the separator to be use

    ::

        >>> list2string([1, 2]
        "1, 2"
        >>> list2string([1, 2], sep=;)
        "1; 2"
        >>> list2string([1, 2], sep=;, space=False)
        "1;2"
        >>> list2string(1, sep=;, space=False)
        "1"

    .. note:: the cast is performed with str()
    """
    data = tolist(data)
    if space is True:
        sep = sep + " "
    res = sep.join([str(x) for x in data])
    return res








