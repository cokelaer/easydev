from easydev import isurl, isurl_reachable


def test_isurl():
    assert isurl_reachable("www.google.com") == True
    assert isurl_reachable("http://www.google.com") == True
    assert isurl_reachable("wrong.co.ujj") == False
    assert isurl("http://wrong.co.ujj") == False

    # 
    assert isurl("http://wrong") == False
