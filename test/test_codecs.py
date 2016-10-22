from easydev import codecs


def test_tolist():
    assert codecs.tolist(1) == [1]
    assert codecs.tolist(1.) == [1.]
    assert codecs.tolist('1') == ['1']
    assert codecs.tolist([1]) == [1]
    assert codecs.tolist([1, 2]) == [1, 2]

    try:
        import numpy as np
        x = np.array([1, 2])
        assert codecs.tolist(x) == [1, 2]
    except:
        pass

    assert sorted(codecs.tolist((1, 2))) == [1, 2]
    
    codecs.tolist(set([1]))


def test_tostring():
    assert codecs.list2string([1, 2]) == "1, 2"
    assert codecs.list2string([1, 2], sep=";") == "1; 2"
    assert codecs.list2string([1, 2], sep=';', space=False) == "1;2"
    assert codecs.list2string(1) == "1"
