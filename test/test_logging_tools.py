from easydev import Logging


def test_logging():

    l = Logging("INFO")
    l.name = "test"
    l.info("test")
    l.debug("test")
    l.warning("test")
    l.error("test")
    l.critical("test")

    for level in ['DEBUG', 'INFO', 'ERROR', 'WARNING', 'CRITICAL']:
        l.level = level
        assert l.level == level
    l.level = True
    l.level = False
    for x in [10,20,30,40,50]:
        l.level = x

    try:
        l.level = "WARN"
        assert Fales
    except:
        assert True

    # FIXME is this working ??wierd syntax in loggibg_tools.
    import copy
    copy.copy(l)
    copy.deepcopy(l)
