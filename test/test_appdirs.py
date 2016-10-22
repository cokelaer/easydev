import mock

def test_app():

    def getter(app):
        app.user_data_dir
        app.site_data_dir
        app.user_config_dir
        app.site_config_dir
        app.user_cache_dir
        app.user_log_dir

    with mock.patch("sys.platform", "darwin"):
        from easydev import appdirs
        app = appdirs.AppDirs("test")
        getter(app)

    with mock.patch("sys.platform", "win32"):
        from easydev import appdirs
        app = appdirs.AppDirs("test")
        getter(app)

    with mock.patch("sys.platform", "linux"):
        from easydev import appdirs
        app = appdirs.AppDirs("test")
        getter(app)
