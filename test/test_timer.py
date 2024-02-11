import time

from easydev.timer import Timer


def test_timer():

    times = []
    with Timer(times):
        time.sleep(0.1)
    assert len(times) == 1
    assert sum(times) < 1

    tt = Timer(times)
