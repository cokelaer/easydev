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

#from threading import Thread
import time
from multiprocessing import cpu_count, Process, Queue, Pool

__all__ = ["MultiProcessing"]

class MultiProcessing(object):
    """Class to run jobs in an asynchronous manner.

    You would use this class to run several jobs on a local computer that has
    several cpus.


    :: 

        t = MultiProcessing(maxcpu=2)
        t.add_job(func, func_args)
        t.run()
        t.results[0] # contain returned object from the function *func*.


    .. warning:: the function must be a function, not a method. This is inherent 
        to multiprocess in the multiprocessing module.
        
    .. warning:: the order in the results list may not be the same as the
        list of jobs. see :meth:`run` for details
        

    """
    def __init__(self, maxcpu=None, verbose=False):
        """

        :param maxcpu: default returned by multiprocessing.cpu_count()
        :param verbose:


        """
        if maxcpu == None:
            maxcpu = cpu_count()

        self.maxcpu = maxcpu
        self.reset()
        self.verbose = verbose

    def reset(self):
        """remove joves and results"""
        self.jobs = [] # a list of processes
        self.results = Queue() # the results to append

    def add_job(self, func, *args, **kargs):
        """add a job in the pool"""
        if self.verbose:
            print("Adding jobs in the queue..",)
        #self.counter += 1
        t = Process(target=func, args=args, kwargs=kargs)
        self.jobs.append(t)

    def _cb(self, results):
        if self.verbose:
            print("callback", results)
        self.results.append(results)
        #self.counter += 1

    def run(self, delay=0.1):
        """Run all the jobs in the Pool until all have finished.

        Jobs that have been added to the job list in :meth:`add_job`
        are now processed in this method by using a Pool. Here, we add
        all jobs using the apply_async method from multiprocess module.
        
        In order to ensure that the jobs are run sequentially in the same
        order as in :attr:`jobs`, we introduce a delay between 2 calls
        to apply_async (see http://docs.python.org/2/library/multiprocessing.html)
        
        A better way may be t use a Manager but for now, this works.
        
        """
        self.results = []
        #self.counter = 0
        self.po = Pool(self.maxcpu)

        for process in self.jobs:
            self.po.apply_async(process._target, process._args, 
                    process._kwargs, callback=self._cb)
            time.sleep(delay) # to ensure that the results have smae order as jobs
            
        self.po.close()
        self.po.join()
        #print "\n", self.counter    
        del self.po # delete to allow to save the object using pickle since Pool cannot be pickled
        self.finished = True


    


