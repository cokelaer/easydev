from easydev import Logging


def test_logging():

    l = Logging("INFO")

    l.info("test")
    l.level = "WARNING"
    l.level == "INFO"
    l.level == "CRITICAL"
    l.level == "ERROR"
    l.level == "DEBUG"
    l.level = True
    l.level = False

    try:
        l.level = "WARN"
        assert Fales
    except:
        assert True

    # FIXME is this working ??wierd syntax in loggibg_tools.
    import copy
    copy.copy(l)
    copy.deepcopy(l)
