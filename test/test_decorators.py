import pytest

from easydev.decorators import _require, ifpandas, ifpylab, requires


class A:
    def create(self):
        self.a = 1
        self.b = 1

    @requires("a", "what to do")
    def get_a(self):
        return self.a

    @requires(["a", "b"], "what to do")
    def get_sum(self):
        return self.a + self.b

    @_require("a", "what to do")
    def get_a_low(self):
        return self.a


def test_requires_missing_raises():
    a = A()
    with pytest.raises(AttributeError):
        a.get_a()


def test_requires_list_missing_raises():
    a = A()
    with pytest.raises(AttributeError):
        a.get_sum()


def test_requires_after_create():
    a = A()
    a.create()
    assert a.get_a() == 1
    assert a.get_sum() == 2


def test_require_single_missing_raises():
    a = A()
    with pytest.raises(AttributeError):
        a.get_a_low()


def test_require_single_present():
    a = A()
    a.a = 5
    assert a.get_a_low() == 5


def test_requires_invalid_first_arg_raises():
    with pytest.raises(TypeError):

        @requires(123, "msg")
        def f(self):
            pass


def test_require_too_many_dotted_levels_raises():
    with pytest.raises(AttributeError):

        @_require("a.b.c", "msg")
        def f(self):
            pass


def test_require_wrong_arg_count_raises():
    with pytest.raises(ValueError):

        @_require("only_one_arg")
        def f(self):
            pass


@ifpandas
def test_deco_pandas():
    pass


@ifpylab
def test_deco_pylab():
    pass
