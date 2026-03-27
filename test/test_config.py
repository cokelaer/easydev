import pytest

from easydev import CustomConfig
from easydev.config_tools import DynamicConfigParser

from . import test_dir

# --- CustomConfig ---


def test_config_custom():
    c = CustomConfig("dummy")
    c.init()
    assert c.user_config_dir is not None
    c.remove()


# --- DynamicConfigParser loading ---


def test_config_loads_sections(dynamic_config):
    assert "General" in dynamic_config.sections()
    assert "GA" in dynamic_config.sections()


def test_config_remove_section(dynamic_config):
    dynamic_config.remove_section("General")
    assert "General" not in dynamic_config.sections()


def test_config_str(dynamic_config):
    s = str(dynamic_config)
    assert "GA" in s


def test_config_from_configparser(dynamic_config):
    dc2 = DynamicConfigParser(dynamic_config)
    assert dc2.sections() == dynamic_config.sections()


def test_config_invalid_type_raises():
    with pytest.raises(TypeError):
        DynamicConfigParser(234)


def test_config_read_missing_file_raises():
    dc = DynamicConfigParser()
    with pytest.raises(IOError):
        dc.read("file_that_does_not_exist.ini")


# --- add_option / get_options ---


def test_config_add_and_get_option():
    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "popsize", 5)
    opts = dc.get_options("GA")
    assert opts["popsize"] == 5


def test_config_add_option_unknown_section_raises():
    dc = DynamicConfigParser()
    with pytest.raises(AssertionError):
        dc.add_option("NonExistent", "key", "val")


# --- attribute-style access ---


def test_config_attribute_access(dynamic_config):
    assert dynamic_config.GA is not None


def test_config_attribute_set():
    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)
    dc.GA.test = 2
    dc["GA"]["test"] = 4
    del dc["GA"]["test"]


# --- save and reload ---


def test_config_save_and_reload(tmp_path):
    outfile = str(tmp_path / "out.ini")
    dc = DynamicConfigParser(f"{test_dir}/data/config.ini")
    dc.save(outfile)
    dc2 = DynamicConfigParser(outfile)
    assert dc == dc2


def test_config_save_twice_no_error(tmp_path, dynamic_config):
    outfile = str(tmp_path / "out.ini")
    dynamic_config.save(outfile)
    dynamic_config.save(outfile)  # second save should not raise


# --- delete section ---


def test_config_delete_section():
    cfg = DynamicConfigParser(f"{test_dir}/data/config.ini")
    dc = DynamicConfigParser(cfg)
    del dc["GA"]
    assert "GA" not in dc.sections()
    assert "General" in dc.sections()


# --- equality ---


@pytest.mark.parametrize(
    "same_sections,same_values,expected_eq",
    [
        (False, True, False),
        (True, False, False),
        (True, True, True),
    ],
)
def test_config_equality(same_sections, same_values, expected_eq):
    dc1 = DynamicConfigParser()
    dc1.add_section("GA")
    dc1.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    if same_sections:
        dc2.add_section("GA")
        dc2.add_option("GA", "test", 1 if same_values else 2)
    else:
        dc2.add_section("GA2")
        dc2.add_option("GA2", "test", 1)

    assert (dc1 == dc2) == expected_eq


# --- section2dict type coercion ---


def test_section2dict_types():
    dc = DynamicConfigParser()
    dc.add_section("S")
    dc.add_option("S", "flag", "True")
    dc.add_option("S", "count", "42")
    dc.add_option("S", "name", "hello")
    opts = dc.get_options("S")
    assert opts["flag"] is True
    assert opts["count"] == 42
    assert opts["name"] == "hello"
