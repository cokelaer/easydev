from easydev.multicore import MultiProcessing


def func(n=400, *args, **kargs):
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

def test_func():
    t = MultiProcessing()
    t.add_job(func, 400)
    t.add_job(func, 300)
    t.add_job(func, 200)
    t.add_job(func, 100)
    t.run()
    print t.results




