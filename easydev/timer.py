# -*- coding: utf-8 -*-
#
#  This file is part of Easydev software
#
#  Copyright (c) 2016 - Easydev
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/cokelaer/easydev
#
##############################################################################
import time


class Timer():
    """Timer working with *with* statement


    ::

        times = []
        with Timer(times):
            # do something
            import time
            time.sleep(0.1)
        with Timer(imes):
            # do something else
            time.sleep(0.2)

        

    """
    def __init__(self, times):
        self.times = times

    def __enter__(self):
        self.t1 = time.time()

    def __exit__(self, type, value, traceback):
        self.t2 = time.time()
        self.times.append(self.t2-self.t1)

