from math import sqrt
from threading import Thread
from multiprocessing import cpu_count, Process, Queue, Pool

__all__ = ["MultiProcessing", "test_func"]

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


    
def test_func(n=400, *args, **kargs):
    """A simple test function to play with MultiProcessing class

    :param n: 400 takes about 5 seconds

    """
    print "inside func", args, kargs
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                sqrt(float(i))
    d = {'id':n}
    return d

"""
def test():
    t = MultiProcessing()
    t.add_job(func, 400)
    t.add_job(func, 300)
    t.add_job(func, 200)
    t.add_job(func, 100)
    t.run()
    print t.results

def test2():
    t = MultiProcessing()

    model = "../../results_test/model.sif"
    midas = "../../results_test/MD_CD3+CD4-CD45RO-_donor1_CD3-CD28-CD2__row_and_exp.csv"
    method = "essm"

    t.add_job(tcellanalysis, model, midas, method)
    t.add_job(tcellanalysis, model, midas, method)
    t.run()
    print t.results
    return t
"""


