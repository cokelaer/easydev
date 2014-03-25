# keep nose inside the functions to avoid dependencies

__all__ = ["assert_list_almost_equal", "trysetattr"]


def assert_list_almost_equal(first, second, places=None):
    """Combined version nose.tools.assert_almost_equal and assert_list_equal

    This function checks that 2 lists contain identical items.
    The equality between pair of items is checked with assert_almost_equal
    function, which means you can check for the places argument

    .. note:: there may be already some tools to 
        check that either in nosetests or unittest
        but could not find.

    .. doctest::

        >>> from easydev.easytest import assert_list_almost_equal as assert_list
        >>> assert_list([0,0,1], [0,0,0.9999], places=3)

    
    """
    from nose.tools import assert_almost_equal
    for x,y in zip(first, second):
        assert_almost_equal(x,y, places=places)


def trysetattr(this, attrname, value, possible):
    """A common test pattern: try to set a non-writable attribute
    
    ::
    
        class A(object):
            def __iinit__(self):
                self._a = 1
                self._b = 2
            def _get_a(self):
                return self._a
            def _set_a(self, value):
                self._a = value
            a = property(_get_a, _get_b)
            def _get_b(self):
                return self._b
            b = property(_get_b)

        >>> o = A()
        >>> trysetattr(A, "a", 1, possible=True)
        >>> trysetattr(A, "b", 1, False)
        AssertionError
    
    """
    if possible == True:
        a1 = True
        a2 = False
    else:
        a1 = False
        a2 = True
    try:
        setattr(this, attrname, value)
        assert a1    # if the setattr is possible, this should be True
    except:
        assert a2

