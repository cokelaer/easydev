from easydev.platform import get_platform, linux_distribution, is_windows
from easydev.platform import is_linux, is_mac

from unittest.mock import patch



def test_platform():

    assert get_platform() in ['Linux', 'Windows', 'Mac']

    linux_distribution()

    is_windows()
    is_linux()
    is_mac()



    def func():
        raise Exception
    with patch("platform.linux_distribution", func):
        get_platform()
