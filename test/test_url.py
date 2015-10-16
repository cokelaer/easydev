from easydev import isurl_reachable
from nose.plugins.attrib import attr


@attr('skip')
def test_isurl():
    assert isurl_reachable("www.google.com") == True
    assert isurl_reachable("http://www.google.com") == True
    assert isurl_reachable("https://fr.yahoo.com") == False # moved
    assert isurl_reachable("wrong.co.ujj") == False
    assert isurl_reachable("http://wrong.co.ujj") == False
    assert isurl_reachable("http://wrong.co") == False
