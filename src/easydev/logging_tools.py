# -*- python -*-
#
#  This file is part of XXX software
#
#  Copyright (c) 2011-2012 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://www.ebi.ac.uk/~cokelaer/XXX
#
##############################################################################
import logging


class Logging(object):
    """logging utility.

    When using the logging utility, it seems to work like a singleton.
    So, once logging level is set, you can not set it again easily. 
    Here is a class that allows to do that. 

    .. warning:: this is a bit of hack.Maybe this is not a proper solution but
        it seems to do the work.

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
            "CRITICAL", "ERROR"]
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
        valid_level = ["INFO", "DEBUG", "WARNING", "CRITICAL", "ERROR"]
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
        doc="One of INFO, DEBUG, WARNING, CRITICAL, ERROR")
    level = property(_get_level, _set_level, 
        doc="One of INFO, DEBUG, WARNING, CRITICAL, ERROR")

