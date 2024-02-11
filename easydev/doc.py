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
"""Module related to documentation


.. testsetup::

    from easydev.doc import *

"""
__all__ = ["underline"]


def underline(text, symbol="="):
    """Underlines a string with a specific character

    :param str text: the text to underline
    :param str symbol: the character to be used to underline the text
    :return: underlined text.

    .. doctest::

        >>> print(underline("test"))
        test
        ====

    """
    length = len(text)
    return text + "\n" + length * symbol
