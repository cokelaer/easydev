
from easydev import progressbar
import time


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
    
