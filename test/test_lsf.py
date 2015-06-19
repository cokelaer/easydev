from easydev.lsf import *
import os

def test_lsf():
    t = LSFCluster(prog="dummy", verbose=True)
    t.add_cmd("ls", level=1)
    t.create_scripts()
    t.cleanup()

