# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2012-2014 - EBI
#
#  File author(s): Thomas Cokelaer (cokelaer, gmail.com)
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://thomas-cokelaer.info
#
##############################################################################
# $Id: tools.py 2963 2012-12-17 14:31:26Z cokelaer $
"""Handy decorators"""
__all__ = ['require']


# decorator with arguments and optional arguments for a method
def require(*args_deco, **kwds_deco):
    """Decorator for class method to check if an attribute exist

    .. doctest::

        from easydev.decorators import require

        class Test(object):
            def __init__(self):
               self.m = 1
            @require('m', "set the m attribute first")
            def print(self):
                print self.m
        t = Test()
        t.print()


    """
    if len(args_deco) != 2:
        raise ValueError("require decorator expects 2 parameter. First one is" +
                "the required attribute. Second one is an error message.")
    attribute = args_deco[0]
    msg = args_deco[1]

    if len(attribute.split('.'))>2:
        raise AttributeError('This version of require decorator introspect only 2 levels')

    def decorator(func):
        # func: function object of decorated method; has
        # useful info like f.func_name for the name of
        # the decorated method.

        def newf(*args, **kwds):
            # This code will be executed in lieu of the
            # method you've decorated.  You can call the
            # decorated method via f(_args, _kwds).
            names = attribute.split('.')

            if len(names) == 1:
                if hasattr(args[0], attribute):
                   return func(*args, **kwds)
                else:
                   raise AttributeError('%s not found. %s' % (names, msg))
            elif len(names) == 2:
                if hasattr(getattr(args[0], names[0]), names[1]):
                    return func(*args, **kwds)
                else:
                   raise AttributeError('%s not found. %s' % (names, msg))

        newf.__name__ = func.__name__
        newf.__doc__ = func.__doc__
        return newf

    return decorator







