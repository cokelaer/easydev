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
"""toolkit to ease development"""
import subprocess
import json

__all__ = ["shellcmd", "checkParam", "swapdict", "check_param_in_list",
    "check_range", "precision", "AttrDict", "DevTools"]


def precision(data, digit=2):
    """Return the value with only 2 digits

    ::

        >>> precision(2.123)
        2.12
        >>> precision(2123, digit=-2)
        2100

    """
    data = int(data*pow(10, digit))
    data /= pow(10., digit)
    return data


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
    if strict is True:
        if value <= a:
            raise ValueError(" {} must be greater (or equal) than {}".format(value, a))
        if value >= b:
            raise ValueError(" {} must be less (or less) than {}".format(value, b))
    elif strict is False:
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
    if isinstance(valid_values, list) is False:

        raise TypeError("the valid_values second argument must be a list of valid values. {0} was provided.".format(valid_values))

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

        if verbose is True:
            print(output)

        return output
    except Exception as err:
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


class AttrDict(dict):
    """dictionary-like object that exposes its keys as attributes.

    You can add values as attribute, or with ['key'] syntax

    .. doctest::

        >>> from easydev import AttrDict
        >>> a = AttrDict('value': 1)
        >>> a.value
        1
        >>>
        >>> a.unit = 'meter'
        >>> a.keys()
        ['value', 'meter']


    """
    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)
        self.__dict__ = self


class DevTools(object):
    """Aggregate of easydev.tools functions.

    """
    def check_range(self, value, a, b):
        """wrapper around :func:`easydev.check_range`"""
        check_range(value, a, b, strict=False)

    def check_param_in_list(self, param, valid_values):
        """wrapper around :func:`easydev.check_param_in_list`"""
        param = self.to_list(param)
        for name in param:
            check_param_in_list(name, list(valid_values))

    def swapdict(self, d):
        """wrapper around :func:`easydev.swapdict`"""
        return swapdict(d)

    def tolist(self, query):
        print('easydev tolist deprecated since 0.8.0. use to_list() instead')
        return self.to_list(query)

    def to_list(self, query):
        """Cast to a list if possible

        'a' ->['a']
        1 -> [1]
        """
        from easydev import codecs
        return codecs.to_list(query)

    def list2string(self, query, sep=",", space=False):
        from easydev import codecs
        return codecs.list2string(query, sep=sep, space=space)

    def to_json(self, dictionary):
        """Transform a dictionary to a json object"""
        return json.dumps(dictionary)
