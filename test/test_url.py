from easydev import isurl


def test_isurl():
    assert isurl("www.google.org") == True
    assert isurl("http://www.google.org") == True
    assert isurl("wrong") == False
