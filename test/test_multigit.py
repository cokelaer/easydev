from easydev import multigit



def test_mg():

    try:
        m = multigit.MultiGIT(['pull'], directories=['test'])
    except:
        pass
    
