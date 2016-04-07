from easydev.paths import *
import os


def test_get_share_directory_path():
    get_shared_directory_path("easydev")
    try:
        get_shared_directory_path("dummydummy")
        assert False
    except:
        assert True


def test_get_share_directories():
    a = get_shared_directories("easydev", "themes")

def test_get_share_file():
    f = get_share_file("easydev", os.sep.join(["themes", "standard"]), "theme.conf")


def test_gsf():
    f = gsf("easydev", os.sep.join(["themes", "standard"]), "theme.conf")
    try:
        f = gsf("easydev", os.sep.join(["themes", "standard"]), "theme.conf.dummy")
        assert False
    except:
        assert True
