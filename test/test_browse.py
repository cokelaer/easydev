from easydev.browser import browse 
from nose.plugins.attrib import attr


@attr('notravis')
def test_browse():
    browse("http://pypi.python.org", verbose=True)
    browse("pypi.python.org", verbose=True)
    browse(".", verbose=True)


