from easydev import PackageBuilder


def test_package():
    p = PackageBuilder("tstPkg")
    p.logging.debugLevel = "ERROR"
    p.buildPackage()
    p.buildPackage(force=True)
    import shutil
    shutil.rmtree("tstPkg")


def test_options():
    from easydev import package
    package.OptionsBuildPackage(["--pkgname", "test"])

