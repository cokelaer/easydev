from easydev import Logging


def test_logging():

    l = Logging("INFO")
    l.info("test")
    l.level = "WARNING"
    l.info("test")
    l.level == "INFO"

    try:
        l.level = "WARN"
        assert Fales
    except:
        assert True
