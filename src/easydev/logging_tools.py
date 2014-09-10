# -*- python -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2012-2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://github.com/cokelaer/easydev
#
##############################################################################
import logging

__all__ = ["Logging"]


class Logging(object):
    """logging utility.

    When using the logging utility, it works like a singleton.
    So, once logging level is set, you cannot set it again easily.
    Here is a class that allows to do that.

    .. warning:: this is a bit of a hack. Maybe this is not a proper solution but
        it seems to do the job.

    ::

        >>> l = Logging("INFO")
        >>> l.info("test")
        INFO:root:test
        >>> l.level = "WARNING"
        >>> l.info("test")


    """
    # I think that we can not inherit from logging.
    def __init__(self, level):
        """.. rubric:: constructor

        :param str level: valid levels are ["INFO", "DEBUG", "WARNING",
            "CRITICAL", "ERROR"]. If set to True, level is internally set to
            INFO. If set to False, level is seet internally to ERROR.
        """
        self._debugLevel = None
        self.debugLevel = level
        self.logging = logging
        self.info = logging.info
        self.warning = logging.warning
        self.critical = logging.critical
        self.error = logging.error
        self.debug = logging.debug

    def _set_level(self, level):
        valid_level = [True, False, "INFO", "DEBUG", "WARNING", "CRITICAL", "ERROR"]
        if level is True:
            level = "INFO"
        if level is False:
            level = "ERROR"
        if level in valid_level:
            self._debugLevel = level
        else:
            raise ValueError("The level of debugging must be in %s " %valid_level)
        # I'm not sure this is the best solution, but basicConfig can be called
        # only once and populatse root.handlers list with one instance of
        # logging.StreamHandler. So, I reset it before calling basicConfig
        # that it is effectively changing the logginh behaviour
        logging.root.handlers = []
        logging.basicConfig(level=self._debugLevel)
    def _get_level(self):
        return self._debugLevel
    debugLevel = property(_get_level, _set_level,
        doc="Read/Write access to the debug level. Must be one of INFO, DEBUG, WARNING, CRITICAL, ERROR")
    level = property(_get_level, _set_level,
        doc="alias to :attr:`~easydev.logging_tools.Logging.debugLevel` (Read-only access)")

    # Used copy/deepcopy module
    def __copy__(self):
        print("WARNING: easydev.logging_tools.__copy__ deprecated. use copy() instead")
        s = Logging(self.level)
        return s

    def __deepcopy__(self, memo):
        s = Logging(self.level)
        return s



