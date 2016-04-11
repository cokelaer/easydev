from easydev.config_tools import ConfigExample, DynamicConfigParser
from easydev import CustomConfig
import os


def test_config_custom():
    c = CustomConfig('dummy')
    c.init()
    c.user_config_dir
    c.remove()

def test_configExample():
    c = ConfigExample().config
    assert 'General' in c.sections()
    assert 'GA' in c.sections()
    print(c)
    c.remove_section('General')


def _test_ordered_dict_attribute():
    # disabled because incompatible with python 3
    c = DynamicConfigParser()
    c.add_section("GA")
    c.GA.test = 2 # this is an attribute only, not  yet a key
    c.add_option("GA", "test", 1)
    c.GA.test = 2


def test_DynamicConfig():
    c = ConfigExample()
    dc = DynamicConfigParser(c.config)
    dc.save('test.ini')

    dc = DynamicConfigParser('test.ini')
    #dc = DynamicConfigParser(c.config)
    dc._replace_config(c.config)
    dc.GA
    dc.add_option("GA", "bool", 'True')
    dc.get_options("GA")

    os.remove('test.ini')

    dc.remove_section('GA')
    assert 'GA' not in dc.sections()
    print(dc)

    # try something stupid
    try:
        dc = DynamicConfigParser(234)
        assert False
    except TypeError:
        assert True



def test_DynamicConfig_setter():

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)
    dc.save("test.ini")

    dc2 = DynamicConfigParser("test.ini")
    assert dc == dc2
    dc2.GA.test == 1


    dc.GA.test = 10
    dc.save("test.ini")
    dc2 = DynamicConfigParser("test.ini")
    assert dc == dc2

    assert dc2.GA.test == '10'

    os.remove('test.ini')


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

    assert (dc==dc2) == False


    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    dc2.add_section("GA")
    dc2.add_option("GA", "test", 2)

    assert (dc==dc2) == False

    dc = DynamicConfigParser()
    dc.add_section("GA")
    dc.add_option("GA", "test", 1)

    dc2 = DynamicConfigParser()
    dc2.add_section("GA")
    dc2.add_option("GA", "test", 1)

    assert (dc==dc2) == True




