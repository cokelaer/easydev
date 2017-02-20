from easydev import browser

try:
    from unittest.mock import patch
except:
    from mock import patch


def test_browse(mocker):
    def func(*args, **kwargs):
        pass
    with patch('webbrowser.open', func):
        with patch('webbrowser.open_new', func):
            browser.browse("http://pypi.python.org", verbose=True)
            browser.browse("pypi.python.org", verbose=True)
            browser.browse(".", verbose=True)


def test_browse_module(mocker):
    from easydev.browser import main
    def func(*args, **kwargs):
        pass
    with patch('webbrowser.open', func):
        main(["browse", "--help"])
        main(["browse", "." ])
        main(["browse", "http://www.uniprot.org" ])



