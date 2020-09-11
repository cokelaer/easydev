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
import colorlog

__all__ = ["Logging"]


colors = {
    'DEBUG':    'cyan',
    'INFO':     'green',
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'bold_red'}



class Logging(object):
    """logging utility.

    ::

        >>> l = Logging("root", "INFO")
        >>> l.info("test")
        INFO:root:test
        >>> l.level = "WARNING"
        >>> l.info("test")

    """
    def __init__(self, name="root", level="WARNING"):
        self.default = name
        self._name = name
        self.formatter = colorlog.ColoredFormatter(
             "%(log_color)s%(levelname)-8s[%(name)s]: %(reset)s %(blue)s%(message)s",
             datefmt=None,
             reset=True,
             log_colors=colors,
             secondary_log_colors={},
             style='%'
        )
        self._set_name(name)


    def _set_name(self, name):
        self._name = name
        logger = colorlog.getLogger(self._name)
        if len(logger.handlers) == 0:
            handler = colorlog.StreamHandler()
            handler.setFormatter(self.formatter)
            logger.addHandler(handler)
            if self.level == 0:
                self.level = "WARNING"
            else:
                self._set_level(self.level)
    def _get_name(self):
        return self._name
    name = property(_get_name, _set_name)

    def _set_level(self, level):
        if isinstance(level, bool):
            if level is True:
                level = "INFO"
            if level is False:
                level = "ERROR"
        assert level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],\
            "you provided {}".format(level)
        logging_level = getattr(colorlog.logging.logging, level)
        colorlog.getLogger(self.name).setLevel(level)

    def _get_level(self):
        level = colorlog.getLogger(self.name).level
        if level == 10:
            return "DEBUG"
        elif level == 20:
            return "INFO"
        elif level == 30:
            return "WARNING"
        elif level == 40:
            return "ERROR"
        elif level == 50:
            return "CRITICAL"
        else:
            return level
    level = property(_get_level, _set_level)

    def debug(self, msg):
        colorlog.getLogger(self.name).debug(msg)
    def info(self, msg):
        colorlog.getLogger(self.name).info(msg)
    def warning(self, msg):
        colorlog.getLogger(self.name).warning(msg)
    def critical(self, msg):
        colorlog.getLogger(self.name).critical(msg)
    def error(self, msg):
        colorlog.getLogger(self.name).error(msg)
















