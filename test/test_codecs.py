import pytest

from easydev import codecs


@pytest.mark.parametrize(
    "data,expected",
    [
        (1, [1]),
        (1.0, [1.0]),
        ("1", ["1"]),
        ([1], [1]),
        ([1, 2], [1, 2]),
    ],
)
def test_tolist(data, expected):
    assert codecs.tolist(data) == expected


def test_tolist_tuple():
    assert sorted(codecs.tolist((1, 2))) == [1, 2]


def test_tolist_set():
    result = codecs.tolist({1})
    assert 1 in result


def test_tolist_numpy():
    pytest.importorskip("numpy")
    import numpy as np

    x = np.array([1, 2])
    assert codecs.tolist(x) == [1, 2]


@pytest.mark.parametrize(
    "data,sep,space,expected",
    [
        ([1, 2], ",", True, "1, 2"),
        ([1, 2], ";", True, "1; 2"),
        ([1, 2], ";", False, "1;2"),
        (1, ",", True, "1"),
        (["a", "b"], ",", False, "a,b"),
    ],
)
def test_list2string(data, sep, space, expected):
    assert codecs.list2string(data, sep=sep, space=space) == expected
