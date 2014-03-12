from easydev import Logging


def test_logging():

    l = Logging("INFO")
    l.info("test")
    l.level = "WARNING"
    l.level == "INFO"
    l.level == "CRITICAL"
    l.level == "ERROR"

    try:
        l.level = "WARN"
        assert Fales
    except:
        assert True
