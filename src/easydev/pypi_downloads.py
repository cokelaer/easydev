# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://www.assembla.com/spaces/pyeasydev/wiki
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""Utilities to lookup into pypi stats.

This uses vanity package, which must be installed manually to prevent any
external dependencies on easydev.

"""

import datetime


def plot_pypi_downloads(package):
    """pLot number of downloads versus time


    .. plot::
        :include-source:

        >>> from easydev import pypi_downloads
        >>> df = pypi_downloads.plot_pypi_downloads("easydev")

        
    .. warnings:: requires pandas and vanity packages
    """
    try:
        import vanity
        import pandas as pd
    except:
        print("This function requires pandas and vanity packages available on pypi.")
        return
    releases = list(vanity.package_releases([package]))[0][1]
    downloads = []
    times = []
    data = list(vanity.release_data([package]))
    for i in range(0, len(releases)):
        if len(data[i][0]):
            dtime = data[i][0][0]['upload_time']
            download = data[i][0][0]['downloads']
            tt = dtime.timetuple()
            times.append([tt[0], tt[1], tt[2]])
            downloads.append(download)
    df = pd.Series(downloads, [datetime.datetime(*x) for x in times],
            name=package)
    df = df.sort_index()
    df.cumsum().plot(marker="o")
    return df
