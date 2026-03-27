import copy

import pytest

from easydev import Logging


def test_logging_messages():
    l = Logging("test_messages", "WARNING")
    l.info("test")
    l.debug("test")
    l.warning("test")
    l.error("test")
    l.critical("test")


@pytest.mark.parametrize("level", ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
def test_logging_level_string(level):
    l = Logging("test_level_str_{}".format(level))
    l.level = level
    assert l.level == level


@pytest.mark.parametrize(
    "numeric,expected",
    [
        (10, "DEBUG"),
        (20, "INFO"),
        (30, "WARNING"),
        (40, "ERROR"),
        (50, "CRITICAL"),
    ],
)
def test_logging_level_numeric(numeric, expected):
    l = Logging("test_level_num_{}".format(numeric))
    l.level = numeric
    assert l.level == expected


def test_logging_level_bool_true():
    l = Logging("test_level_bool_true")
    l.level = True
    assert l.level == "INFO"


def test_logging_level_bool_false():
    l = Logging("test_level_bool_false")
    l.level = False
    assert l.level == "ERROR"


def test_logging_name_property():
    l = Logging("test_name_prop")
    l.name = "renamed"
    assert l.name == "renamed"


def test_logging_warn_alias():
    # "WARN" is a deprecated alias for WARNING in Python's logging module
    l = Logging("test_warn_alias")
    l.level = "WARN"
    assert l.level == "WARNING"


def test_logging_copy():
    l = Logging("test_copy")
    copy.copy(l)
    copy.deepcopy(l)
