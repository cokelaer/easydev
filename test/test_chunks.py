import pytest

from easydev import split_into_chunks


@pytest.mark.parametrize(
    "items,n,expected",
    [
        ([0, 1, 2, 3, 4, 5, 6], 2, [[0, 2, 4, 6], [1, 3, 5]]),
        ([0, 1, 2, 3, 4, 5], 2, [[0, 2, 4], [1, 3, 5]]),
        ([1, 1, 2, 2, 3, 3], 3, [[1, 2], [1, 3], [2, 3]]),
        ([1, 2, 3, 4], 4, [[1], [2], [3], [4]]),
    ],
)
def test_split_into_chunks(items, n, expected):
    assert list(split_into_chunks(items, n)) == expected


def test_split_into_chunks_empty():
    assert list(split_into_chunks([], 3)) == []


def test_split_into_chunks_single_item():
    assert list(split_into_chunks([42], 3)) == [[42]]


def test_split_into_chunks_more_chunks_than_items():
    result = list(split_into_chunks([1, 2], 5))
    assert result == [[1], [2]]
