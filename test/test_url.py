from easydev import isurl


def test_isurl():
    assert isurl("www.google.com") == True
    assert isurl("http://www.google.com") == True
    assert isurl("wrong") == False
