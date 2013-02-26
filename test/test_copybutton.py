from easydev import copybutton


def test_copybutton():
     copybutton.get_copybutton_path()

def test_copy_javascript_into_static_path():
    copybutton.copy_javascript_into_static_path("_static", 
        copybutton.get_copybutton_path())
    copybutton.copy_javascript_into_static_path("_static", 
        copybutton.get_copybutton_path())
    import os 
    os.remove("_static/copybutton.js")
    os.rmdir("_static")
