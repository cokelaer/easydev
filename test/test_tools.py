from easydev import tools

def test_swapdict():
    assert {1:'a'} == tools.swapdict({'a':1})

def test_tools():
    tools.shellcmd('ls')
    tools.shellcmd('ls', show=False)
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
