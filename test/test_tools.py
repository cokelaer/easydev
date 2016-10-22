from easydev import tools, TempFile


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

    try:
        tools.check_range(10, 0,1, strict=False)
        assert False
    except:
        assert True
    try:
        tools.check_range(-10, 0,1, strict=False)
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
    tools.shellcmd('lssssssss', verbose=True, ignore_errors=True)

    tools.execute('ls')

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
    try:
        tools.check_param_in_list(10, [0,1,5])
        assert False
    except:
        assert True
    try:
        tools.check_param_in_list(10, [0,1,5], 'testt')
        assert False
    except:
        assert True


def test_precision():
    assert tools.precision(2.123) == 2.12
    assert tools.precision(2.123, 1) == 2.1
    assert tools.precision(2.123,3) == 2.123
    assert tools.precision(2123,-2) == 2100


def test_attrdict():

    a = tools.AttrDict(value=1)
    assert a.value == 1
    assert 'value' in list(a.keys())
    assert 1 in (a.values())

    a.description = 'test'
    assert a['description'] == 'test'

    a['output'] = 'txt'
    assert a.output == 'txt'


    d = {'a':{'b':1}, 'aa':2}
    ad = tools.AttrDict(**d)
    assert ad.a.b == 1
    ad.a.b = 2
    assert ad.a.b == 2

    ad['d'] = 4
    assert ad.d == 4

    try:
        ad.update(1)
        assert False
    except:
        assert True

    # check json capabilities
    fh = TempFile()
    js = ad.to_json()
    ad.to_json(filename=fh.name)
    ad.from_json(fh.name)
    fh.delete()


def test_devtools():
    d = tools.DevTools()
    d.check_param_in_list(1, [1,2])
    d.check_range(1,0,2)
    assert d.list2string(['a', 'b']) == 'a,b'
    assert d.swapdict({'a':1}) == {1:'a'}
    d.to_json({'a':1})
    assert d.to_list('a') == ['a']
    import tempfile, os
    d.mkdirs(tempfile.mkdtemp() + os.sep + "test")
    try:
        d.check_exists("ttttttttttt")
        assert False
    except:
        assert True

def test_mkdirs():
    import tempfile, os
    tools.mkdirs(tempfile.mkdtemp() + os.sep + "test")
    try:
        tools.mkdirs(tempfile.mkdtemp() + os.sep + "test")
        assert False
    except:
        assert True

    try:
        # without / , the dir is not created and raise an error
        tools.mkdirs("tttttttttttttttttttttt")
        assert False
    except:
        assert True

def test_touch():
    with TempFile() as fh:
        fh.name
        tools.touch(fh.name)
