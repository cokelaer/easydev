from math import sqrt
from threading import Thread
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


    """
    def __init__(self, maxcpu=None, verbose=False):
        """

        :param maxcpu: default returned by multiprocessing.cpu_count()
        :param verbose:


        """
        maxcpu = cpu_count()
        #self.counter = 0
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
            print "Adding jobs in the queue..",
        #self.counter += 1
        t = Process(target=func, args=args, kwargs=kargs)
        self.jobs.append(t)

    def _cb(self, results):
        if self.verbose:
            print "callback", results
        self.results.append(results)
        #self.counter += 1

    def run(self):
        """Run all the jobs in the Pool until all have finished.


        """
        self.results = []
        #self.counter = 0
        self.po = Pool(self.maxcpu)

        for process in self.jobs:
            self.po.apply_async(process._target, process._args, 
                process._kwargs, callback=self._cb)
        self.po.close()
        self.po.join()
        #print "\n", self.counter    
        del self.po # delete to allow to save the object using pickle since Pool cannot be pickled
        self.finished = True


    


