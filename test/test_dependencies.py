from easydev.dependencies import get_dependencies



def test():
    get_dependencies("easydev")
    get_dependencies("easydev_dummyi_dont_exists")
