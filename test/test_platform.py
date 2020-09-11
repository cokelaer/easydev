import easydev
from easydev.platform import get_platform, is_windows
from easydev.platform import is_linux, is_mac


def test_platform(mocker):

    assert get_platform() in ['Linux', 'Windows', 'Mac']


    is_windows()
    is_linux()
    is_mac()

    """def func():
        raise Exception
    with patch("platform.linux_distribution", func):
        get_platform()
    """

    mocker.patch.object(easydev.platform, "get_platform")
    easydev.platform.get_platform.return_value = "Windows"
    assert is_linux() is False
    assert is_mac() is False
    assert is_windows() is True

    mocker.patch.object(easydev.platform, "get_platform")
    easydev.platform.get_platform.return_value = "Mac"
    assert is_linux() is False
    assert is_windows() is False
    assert is_mac() is True

