import pytest

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

    with TempFile() as fh:
        pass


def test_list_almost_equal():
    with pytest.warns(FutureWarning):
        assert_list_almost_equal([1, 2], [1, 2])
    # legacy: no tolerance means nothing is compared
    with pytest.warns(FutureWarning):
        assert_list_almost_equal([1, 2], [1, 3])

    assert_list_almost_equal([1, 1], [1, 0.9999], places=3)
    assert_list_almost_equal([1, 1], [1, 0.9999], deltas=1e-4)
    with pytest.raises(ValueError):
        assert_list_almost_equal([1, 1], [1, 0.9999], deltas=1e-5)
    with pytest.raises(AssertionError):
        assert_list_almost_equal([1, 1], [1, 0.9999], deltas=1e-5)


test_list_almost_equal()
