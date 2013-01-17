import easydev

def test_path():
    p = easydev.get_path_sphinx_themes()
    import os
    dirs = os.listdir(p)
    assert 'cno' in dirs
    print dirs

