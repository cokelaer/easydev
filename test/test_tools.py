from easydev import tools


def test_check_range():
    tools.check_range(1, 0,1)
    tools.check_range(0, 0,1)
    tools.check_range(0.5, 0,1)

    try:
        tools.check_range(1, 0,1, strict=True)
        assert False
    except:
        assert True
    try:
        tools.check_range(0, 0,1, strict=True)
        assert False
    except:
        assert True



def test_swapdict():
    assert {1:'a'} == tools.swapdict({'a':1})

    # if the are non-unique values, we can catch the error or no:
    try:
        tools.swapdict({'a':1, 'b':1})
        assert False
    except:
        assert True
    tools.swapdict({'a':1, 'b':1}, check_ambiguity=False)

def test_tools():
    tools.shellcmd('ls')
    tools.shellcmd('ls', show=False)
    tools.shellcmd('ls', show=True)
    output = tools.shellcmd('ls', verbose=True)


def test_tools2():
    try:
        tools.shellcmd('lsss', verbose=False)
        assert False
    except:
        assert True


def test_checkParams():
    tools.checkParam(1, [1, 2])
    try:
        tools.checkParam(0, [1, 2])
        assert False
    except:
        assert True

    try:
        tools.checkParam(0, 0)
        assert False
    except TypeError:
        assert True

def test_check_param_in_list():
    tools.check_param_in_list(1, [0,1,5], "test")


def test_transform_into_list():
    assert tools.transform_into_list(1) == [1]
    assert tools.transform_into_list(1.) == [1.]
    assert tools.transform_into_list('1') == ['1']
    assert tools.transform_into_list([1]) == [1]
    assert tools.transform_into_list([1,2]) == [1,2]
