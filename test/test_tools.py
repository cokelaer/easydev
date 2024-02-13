from easydev import TempFile
from easydev import tools as tools2
from easydev.tools import *


def test_check_range():
    check_range(1, 0, 1)
    check_range(0, 0, 1)
    check_range(0.5, 0, 1)

    try:
        check_range(1, 0, 1, strict=True)
        assert False
    except:
        assert True
    try:
        check_range(0, 0, 1, strict=True)
        assert False
    except:
        assert True

    try:
        check_range(10, 0, 1, strict=False)
        assert False
    except:
        assert True
    try:
        check_range(-10, 0, 1, strict=False)
        assert False
    except:
        assert True


def test_swapdict():
    assert {1: "a"} == swapdict({"a": 1})

    # if the are non-unique values, we can catch the error or no:
    try:
        swapdict({"a": 1, "b": 1})
        assert False
    except:
        assert True
    swapdict({"a": 1, "b": 1}, check_ambiguity=False)


def test_tools():
    shellcmd("ls")
    shellcmd("ls", show=False)
    shellcmd("ls", show=True)
    output = shellcmd("ls", verbose=True)
    shellcmd("lssssssss", verbose=True, ignore_errors=True)

    execute("ls")


def test_tools2():
    try:
        shellcmd("lsss", verbose=False)
        assert False
    except:
        assert True


def test_checkParams():
    checkParam(1, [1, 2])
    try:
        checkParam(0, [1, 2])
        assert False
    except:
        assert True

    try:
        checkParam(0, 0)
        assert False
    except TypeError:
        assert True


def test_check_param_in_list():
    check_param_in_list(1, [0, 1, 5], "test")
    try:
        check_param_in_list(10, [0, 1, 5])
        assert False
    except:
        assert True
    try:
        check_param_in_list(10, [0, 1, 5], "testt")
        assert False
    except:
        assert True


def test_precision():
    assert tools2.precision(2.123) == 2.12
    assert tools2.precision(2.123, 1) == 2.1
    assert tools2.precision(2.123, 3) == 2.123
    assert tools2.precision(2123, -2) == 2100


def test_attrdict():

    a = AttrDict(value=1)
    assert a.value == 1
    assert "value" in list(a.keys())
    assert 1 in (a.values())

    a.description = "test"
    assert a["description"] == "test"

    a["output"] = "txt"
    assert a.output == "txt"

    d = {"a": {"b": 1}, "aa": 2}
    ad = AttrDict(**d)
    assert ad.a.b == 1
    ad.a.b = 2
    assert ad.a.b == 2

    ad["d"] = 4
    assert ad.d == 4

    try:
        ad.update(1)
        assert False
    except:
        assert True

    # check json capabilities
    fh = TempFile()
    js = ad.to_json()
    ad.to_json(filename=fh.name)
    ad.from_json(fh.name)
    fh.delete()


def test_devtools():
    d = DevTools()
    d.check_param_in_list(1, [1, 2])
    d.check_range(1, 0, 2)
    assert d.list2string(["a", "b"]) == "a,b"
    assert d.swapdict({"a": 1}) == {1: "a"}
    d.to_json({"a": 1})
    assert d.to_list("a") == ["a"]
    import os
    import tempfile

    d.mkdirs(tempfile.mkdtemp() + os.sep + "test")
    try:
        d.check_exists("ttttttttttt")
        assert False
    except:
        assert True
    d.mkdir(tempfile.mkdtemp())


def test_mkdirs():
    import os
    import tempfile

    mkdirs(tempfile.mkdtemp() + os.sep + "test")
    try:
        mkdirs(tempfile.mkdtemp() + os.sep + "test")
        assert False
    except:
        assert True

    # without / , was not working but is now part of the API
    mkdirs(tempfile.mkdtemp())


def test_touch():
    with TempFile() as fh:
        fh.name
        touch(fh.name)
