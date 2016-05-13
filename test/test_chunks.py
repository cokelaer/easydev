from easydev import split_into_chunks








def test_chunks():

    assert list(split_into_chunks([0,1,2,3,4,5,6], 2)) == [[0, 2, 4, 6], [1, 3, 5]]
    assert list(split_into_chunks([0,1,2,3,4,5], 2)) == [[0, 2, 4], [1, 3, 5]]

test_chunks()
