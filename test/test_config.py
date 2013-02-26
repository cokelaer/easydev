from easydev.config_tools import *
from easydev.config_tools import _set_section


def test_section():
    s = _set_section()
    print s


def test_configExample():
    c = ConfigExample().config
    assert 'General' in c.sections()
    assert 'GA' in c.sections()
    print c
    c.remove_section('General')    


def test_DynamicConfig():
    c = ConfigExample()
    dc = DynamicConfigParser(c.config)
    dc.save('test.ini')

    dc = DynamicConfigParser('test.ini')
    #dc = DynamicConfigParser(c.config)
    dc.replace_config(c.config)
    dc.GA
    import os
    os.remove('test.ini')

    dc.remove_section('GA')
    assert 'GA' not in dc.sections()
    print dc



