from easydev import do_profile




def test_profile():
    @do_profile()
    def runme():
        a = 1
