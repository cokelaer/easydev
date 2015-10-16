
from easydev import progressbar
import time
from easydev import Progress

def test_progressbar():


    N = 2

    p = progressbar.progress_bar(N)

    for i in range(0,N):
        time.sleep(1)
        p.animate(i+1, i)


    p = progressbar.TextProgressBar(N, progressbar.consoleprint)
    for i in range(0,N):
        time.sleep(1)
        p.animate(i+1, i)
    
    p = Progress(100)
    p.animate(1)
    assert p.pb.interval == 1

    p = Progress(200)
    assert p.pb.interval == 2
    p.animate(1)

    # IPYthon test ? fails on travis
    # p = progressbar.IPythonNotebookPB(200)
    # p.animate(1)

