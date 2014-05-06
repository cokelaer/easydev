from easydev.easytest import *

class A(object):
    pass


def test_trysetattr():
    trysetattr(A, "test", 1, possible=True)
    try:
        trysetattr(A, "test", 1, possible=False)
        assert False
    except:
        assert True


def test_tempfile():
    f = TempFile()
    f.name
    f.delete()
