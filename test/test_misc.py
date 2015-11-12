from easydev.misc import get_home, cmd_exists, in_ipynb
#from mock import patch
import nose.tools
import subprocess
import os.path


def test_get_home():
    get_home()


    #with patch.object(os.path, 'expanduser') as mymock:
    #    mymock.side_effect = ImportError
    #    get_home()


def test_cmd_exists():
    assert cmd_exists('dummy_dummy') == False
    assert cmd_exists('ls') == True

    #with patch.object(subprocess, 'call') as mymock:
    #    mymock.side_effect = Exception
    #    cmd_exists('ls')


def test_in_ipynb():
    assert in_ipynb() == False
