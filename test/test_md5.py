from easydev.md5tools import md5
from easydev import TempFile


def test_md5():
    with TempFile() as temp:
        fh = open(temp.name, "w")
        fh.write("youpi")
        fh.close()
        assert md5(fh.name) == "538e957924f0770b415f473ce900d686"
