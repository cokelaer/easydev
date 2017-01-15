from easydev import do_profile




@do_profile()
def test_profile():
    @do_profile()
    def test_runme():
        a = 1
        a**2
