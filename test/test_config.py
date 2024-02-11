import os

from easydev import CustomConfig
from easydev.config_tools import DynamicConfigParser

from . import test_dir


def test_config_custom():
    c = CustomConfig("dummy")
    c.init()
    c.user_config_dir
    c.remove()


def test_configExample():

    c = DynamicConfigParser(f"{test_dir}/data/config.ini")
    assert "General" in c.sections()
    assert "GA" in c.sections()
    print(c)
    c.remove_section("General")


def test_ordered_dict_attribute():
    # disabled because incompatible with python 3
    c = DynamicConfigParser()
    c.add_section("GA")
    c.GA.test = 2  # this is an attribute only, not  yet a key
    c.add_option("GA", "test", 1)
    c.GA.test = 2
    c["GA"]["test"] = 4
    del c["GA"]["test"]


def test_DynamicConfig(tmpdir):

    outname = tmpdir.join("test.ini")

    # constructor with filename
    dc = DynamicConfigParser(f"{test_dir}/data/config.ini")

    # constructor with existing constructor
    dc = DynamicConfigParser(dc)

    dc.GA
    dc.add_option("GA", "bool", "True")
    dc.get_options("GA")

    # save file and read back
    outname = tmpdir.join("test.ini")
    dc.save(outname)
    dc.save(outname)  # called twice on purpose

    dc.remove_section("GA")
    assert "GA" not in dc.sections()
    print(dc)

    # try something stupid
    try:
        dc = DynamicConfigParser(234)
        assert False
    except TypeError:
        assert True

    dc = DynamicConfigParser()
    try:
        dc.read("test_dummy")
        assert False
    except:
        assert True


def test_DynamicConfigDelete():

    cfg = DynamicConfigParser(f"{test_dir}/data/config.ini")

    dcp = DynamicConfigParser(cfg)
    try:
        del dcp["GA"]
        assert dcp.sections() == ["General"]
    except:
        pass


def test_DynamicConfig_setter(tmpdir):
    outname = tmpdir.join("test.ini")

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "popsize", 1)
    dc.add_section("General")
    dc.add_option("General", "verbose", True)
    dc.add_option("General", "tag", "test")
    dc.save(outname)

    dc2 = DynamicConfigParser(f"{test_dir}/data/config.ini")
    assert dc == dc2

    dc.GA.test = 10


def test_section2dict():
    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)


def test_compare():

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    dc2.add_section("GA2")
    dc2.add_option("GA2", "test", 1)

    assert (dc == dc2) == False

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    dc2.add_section("GA")
    dc2.add_option("GA", "test", 2)

    assert (dc == dc2) == False

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    dc2.add_section("GA")
    dc2.add_option("GA", "test", 1)

    assert (dc == dc2) == True
