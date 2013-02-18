import easydev

def test_path():
    p = easydev.get_path_sphinx_themes()
    import os
    dirs = os.listdir(p)
    assert 'standard' in dirs

def test_sphinx_themes():
    p = easydev.get_sphinx_themes()
    assert 'standard' in p

