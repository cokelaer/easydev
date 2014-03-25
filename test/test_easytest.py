from easydev.easytest import *

class A(object):
    pass


def test_trysetattr():
    trysetattr(A, "test", 1, possible=True)

