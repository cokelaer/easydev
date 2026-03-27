import os

import pytest

from easydev.config_tools import DynamicConfigParser
from easydev.tools import AttrDict

_test_dir = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def config_ini_path():
    return os.path.join(_test_dir, "data", "config.ini")


@pytest.fixture
def dynamic_config(config_ini_path):
    return DynamicConfigParser(config_ini_path)


@pytest.fixture
def empty_config():
    return DynamicConfigParser()


@pytest.fixture
def sample_attrdict():
    return AttrDict(value=1, name="test")
