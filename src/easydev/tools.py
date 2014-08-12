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
"""toolkit to ease development"""
import subprocess


__all__ = ["shellcmd", "checkParam", "swapdict", "check_param_in_list",
    "check_range", "transform_into_list"]


def check_range(value, a, b, strict=False):
    """Check that a value lies in a given range

    :param value: value to test
    :param a: lower bound
    :param b: upper bound
    :return: nothing

    .. doctest::

        >>> from easydev.tools import check_range
        >>> check_range(1,0, 2)

    """
    if strict == True:
        if value <= a:
            raise ValueError(" {} must be greater (or equal) than {}".format(value, a))
        if value >= b:
            raise ValueError(" {} must be less (or less) than {}".format(value, b))
    elif strict == False:
        if value < a:
            raise ValueError(" {} must be greater than {}".format(value, a))
        if value > b:
            raise ValueError(" {} must be less than {}".format(value, b))

def checkParam(param, valid_values):
    """
    .. warning:: deprecated since 0.6.10 use :meth:`check_param_in_list` instead
    """
    print("easydev WARNING:: deprecated; use check_param_in_list instead.")
    check_param_in_list(param, valid_values)


def check_param_in_list(param, valid_values, name=None):
    """Checks that the value of param is amongst valid

    :param param: a parameter to be checked
    :param list valid_values: a list of values

    ::

        check_param_in_list(1, [1,2,3])
        check_param_in_list(mode, ["on", "off"])
    """
    if isinstance(valid_values, list) == False:
        raise TypeError("the valid_values second argument must be a list of valid values")

    if param not in valid_values:
        if name:
            msg = "Incorrect value provided for {} ({})".format(name, param)
        else:
            msg = "Incorrect value provided (%s)" % param
        msg += "    Correct values are %s" % valid_values
        raise ValueError(msg)


def shellcmd(cmd, show=False, verbose=False):
    """An alias to run system commands.

    Based on subprocess.Popen.

    :param str cmd: the command to call
    :param bool show: print the command
    :param bool verbose: print the output

    :return: the output as a string
    """
    if show:
        print(cmd)
    try:
        ret = subprocess.Popen([cmd], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)

        output = ret.stdout.read().strip()
        error = ret.stderr.read().strip()
        ret.wait()

        if len(error) > 0:
            raise Exception(error)

        if verbose == True:
            print output

        return output
    except Exception, err:
        #if verbose: print e
        raise Exception("Error:: Command (%s) failed. Error message is %s" % (cmd, err))



def swapdict(dic, check_ambiguity=True):
    """Swap keys for values in a dictionary

    ::

        >>> d = {'a':1}
        >>> swapdict(d)
        {1:'a'}

    """
    # this version is more elegant but slightly slower : return {v:k for k,v in dic.items()}
    if check_ambiguity:
        assert len(set(dic.keys())) == len(set(dic.values())), "values is not a set. ambiguities for keys."
    return dict(zip(dic.values(), dic.keys()))


def transform_into_list(data):
    import types
    if isinstance(data, list) or isinstance(data, tuple):
        return data #nothing to do
    elif isinstance(data, int) or isinstance(data,float) or isinstance(data,
            str):
        return [data]
    else:
        raise TypeError("Should be a list (or tuple) or single type (float, int, string)")










