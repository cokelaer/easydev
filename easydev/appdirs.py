import os
import sys

from platformdirs import (
    site_config_dir,
    site_data_dir,
    user_cache_dir,
    user_config_dir,
    user_data_dir,
    user_log_dir,
)


class AppDirs(object):
    """Convenience wrapper for getting application dirs."""

    def __init__(self, appname, appauthor=None, version=None, roaming=False, multipath=False):
        self.appname = appname
        self.appauthor = appauthor
        self.version = version
        self.roaming = roaming
        self.multipath = multipath

    @property
    def user_data_dir(self):
        return user_data_dir(self.appname, self.appauthor, version=self.version, roaming=self.roaming)

    @property
    def site_data_dir(self):
        return site_data_dir(self.appname, self.appauthor, version=self.version, multipath=self.multipath)

    @property
    def user_config_dir(self):
        return user_config_dir(self.appname, self.appauthor, version=self.version, roaming=self.roaming)

    @property
    def site_config_dir(self):
        return site_config_dir(self.appname, self.appauthor, version=self.version, multipath=self.multipath)

    @property
    def user_cache_dir(self):
        return user_cache_dir(self.appname, self.appauthor, version=self.version)

    @property
    def user_log_dir(self):
        return user_log_dir(self.appname, self.appauthor, version=self.version)
