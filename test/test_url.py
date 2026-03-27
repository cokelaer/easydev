import http.client as httplib

import pytest

from easydev import isurl_reachable


@pytest.mark.network
def test_isurl_reachable_live():
    assert isurl_reachable("www.google.com") is True
    assert isurl_reachable("http://www.google.com") is True
    assert isurl_reachable("wrong.co.ujj") is False
    assert isurl_reachable("http://wrong.co.ujj") is False


def test_isurl_reachable_200(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status = 200
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.return_value = mock_response
    mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    assert isurl_reachable("www.example.com") is True


def test_isurl_reachable_302(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status = 302
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.return_value = mock_response
    mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    assert isurl_reachable("www.example.com") is True


def test_isurl_reachable_404(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status = 404
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.return_value = mock_response
    mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    assert isurl_reachable("www.example.com") is False


def test_isurl_reachable_request_exception(mocker):
    mock_conn = mocker.MagicMock()
    mock_conn.request.side_effect = Exception("Connection refused")
    mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    assert isurl_reachable("www.example.com") is False


def test_isurl_reachable_response_exception(mocker):
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.side_effect = Exception("Timeout")
    mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    assert isurl_reachable("www.example.com") is False


def test_isurl_strips_http_prefix(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status = 200
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.return_value = mock_response
    mock_cls = mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    isurl_reachable("http://www.example.com")
    mock_cls.assert_called_once_with("www.example.com", timeout=10)


def test_isurl_strips_https_prefix(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status = 200
    mock_conn = mocker.MagicMock()
    mock_conn.getresponse.return_value = mock_response
    mock_cls = mocker.patch("http.client.HTTPConnection", return_value=mock_conn)
    isurl_reachable("https://www.example.com")
    mock_cls.assert_called_once_with("www.example.com", timeout=10)
