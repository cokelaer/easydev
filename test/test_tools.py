import pytest

from easydev import TempFile
from easydev import tools as tools2
from easydev.tools import (
    AttrDict,
    DevTools,
    check_param_in_list,
    check_range,
    checkParam,
    execute,
    mkdirs,
    precision,
    shellcmd,
    swapdict,
    touch,
)

# --- check_range ---


@pytest.mark.parametrize(
    "value,a,b",
    [
        (0.5, 0, 1),
        (0, 0, 1),
        (1, 0, 1),
        (0, -5, 5),
    ],
)
def test_check_range_valid(value, a, b):
    check_range(value, a, b)


@pytest.mark.parametrize(
    "value,a,b,strict",
    [
        (1, 0, 1, True),  # equal to upper bound with strict
        (0, 0, 1, True),  # equal to lower bound with strict
        (10, 0, 1, False),  # above range
        (-1, 0, 1, False),  # below range
    ],
)
def test_check_range_invalid(value, a, b, strict):
    with pytest.raises(ValueError):
        check_range(value, a, b, strict=strict)


# --- swapdict ---


def test_swapdict_basic():
    assert swapdict({"a": 1}) == {1: "a"}


def test_swapdict_multiple():
    assert swapdict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_swapdict_ambiguous_raises():
    with pytest.raises(AssertionError):
        swapdict({"a": 1, "b": 1})


def test_swapdict_ambiguous_no_check():
    result = swapdict({"a": 1, "b": 1}, check_ambiguity=False)
    assert result[1] in ("a", "b")


# --- shellcmd ---


def test_shellcmd_returns_output():
    output = shellcmd("echo hello")
    assert b"hello" in output


def test_shellcmd_show(capsys):
    shellcmd("echo showcmd", show=True)
    captured = capsys.readouterr()
    assert "echo showcmd" in captured.out


def test_shellcmd_verbose(capsys):
    shellcmd("echo verboseout", verbose=True)
    captured = capsys.readouterr()
    assert "verboseout" in captured.out


def test_shellcmd_ignore_errors():
    shellcmd("lssssssss", verbose=True, ignore_errors=True)


def test_shellcmd_raises_on_bad_command():
    with pytest.raises(Exception):
        shellcmd("lsss", verbose=False)


# --- execute ---


def test_execute():
    execute("echo hello")


# --- check_param_in_list ---


@pytest.mark.parametrize(
    "param,valid",
    [
        (1, [1, 2]),
        ("a", ["a", "b"]),
        (0, [0, 1]),
    ],
)
def test_check_param_in_list_valid(param, valid):
    check_param_in_list(param, valid)


@pytest.mark.parametrize(
    "param,valid",
    [
        (0, [1, 2]),
        ("c", ["a", "b"]),
    ],
)
def test_check_param_in_list_invalid(param, valid):
    with pytest.raises(ValueError):
        check_param_in_list(param, valid)


def test_check_param_in_list_with_name_in_message():
    with pytest.raises(ValueError, match="myvar"):
        check_param_in_list(10, [1, 2], name="myvar")


def test_check_param_in_list_non_list_raises():
    with pytest.raises(TypeError):
        check_param_in_list(0, 0)


# --- checkParam (deprecated) ---


def test_checkParam_valid():
    checkParam(1, [1, 2])


def test_checkParam_invalid():
    with pytest.raises(ValueError):
        checkParam(0, [1, 2])


def test_checkParam_non_list_raises():
    with pytest.raises(TypeError):
        checkParam(0, 0)


# --- precision ---


@pytest.mark.parametrize(
    "data,digit,expected",
    [
        (2.123, 2, 2.12),
        (2.123, 1, 2.1),
        (2.123, 3, 2.123),
        (2123, -2, 2100),
    ],
)
def test_precision(data, digit, expected):
    assert tools2.precision(data, digit) == expected


# --- AttrDict ---


def test_attrdict_attribute_access():
    a = AttrDict(value=1)
    assert a.value == 1
    assert "value" in list(a.keys())
    assert 1 in a.values()


def test_attrdict_set_via_attribute():
    a = AttrDict(value=1)
    a.description = "test"
    assert a["description"] == "test"


def test_attrdict_set_via_key():
    a = AttrDict(value=1)
    a["output"] = "txt"
    assert a.output == "txt"


def test_attrdict_nested():
    ad = AttrDict(**{"a": {"b": 1}, "aa": 2})
    assert ad.a.b == 1
    ad.a.b = 2
    assert ad.a.b == 2
    ad["d"] = 4
    assert ad.d == 4


def test_attrdict_update_invalid_type_raises():
    ad = AttrDict(x=1)
    with pytest.raises(TypeError):
        ad.update(1)


def test_attrdict_to_json_string():
    ad = AttrDict(x=1, y=2)
    js = ad.to_json()
    assert "x" in js
    assert "1" in js


def test_attrdict_json_roundtrip(tmp_path):
    ad = AttrDict(x=1, y=2)
    path = str(tmp_path / "test.json")
    ad.to_json(filename=path)
    ad2 = AttrDict()
    ad2.from_json(path)
    assert ad2["x"] == 1
    assert ad2["y"] == 2


# --- DevTools ---


def test_devtools_param_list():
    d = DevTools()
    d.check_param_in_list(1, [1, 2])


def test_devtools_check_range():
    d = DevTools()
    d.check_range(1, 0, 2)


def test_devtools_list2string():
    d = DevTools()
    assert d.list2string(["a", "b"]) == "a,b"


def test_devtools_swapdict():
    d = DevTools()
    assert d.swapdict({"a": 1}) == {1: "a"}


def test_devtools_to_json():
    d = DevTools()
    result = d.to_json({"a": 1})
    assert "a" in result


def test_devtools_to_list():
    d = DevTools()
    assert d.to_list("a") == ["a"]


def test_devtools_mkdirs(tmp_path):
    d = DevTools()
    d.mkdirs(str(tmp_path / "new_subdir"))


def test_devtools_mkdir(tmp_path):
    d = DevTools()
    d.mkdir(str(tmp_path / "another"))
    d.mkdir(str(tmp_path / "another"))  # calling again should not raise


def test_devtools_shellcmd():
    d = DevTools()
    out = d.shellcmd("echo devtools")
    assert b"devtools" in out


def test_devtools_check_exists_missing_raises():
    d = DevTools()
    with pytest.raises(ValueError):
        d.check_exists("this_file_does_not_exist")


# --- mkdirs ---


def test_mkdirs_creates_directory(tmp_path):
    target = str(tmp_path / "subdir" / "nested")
    mkdirs(target)
    import os

    assert os.path.isdir(target)


def test_mkdirs_existing_dir_no_raise(tmp_path):
    target = str(tmp_path / "subdir")
    mkdirs(target)
    mkdirs(target)  # second call must not raise


def test_mkdirs_no_sep(tmp_path):
    # path without trailing separator should still work
    mkdirs(str(tmp_path / "plain"))


# --- touch ---


def test_touch_creates_file(tmp_path):
    f = tmp_path / "new.txt"
    touch(str(f))
    assert f.exists()


def test_touch_updates_existing_file(tmp_path):
    f = tmp_path / "existing.txt"
    f.write_text("hello")
    touch(str(f))
    assert f.exists()
