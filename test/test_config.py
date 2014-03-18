from easydev.config_tools import *




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
    #assert dc2.GA.test == 10


