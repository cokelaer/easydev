# -*- python -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2012-2013
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: https://pypi.python.org/pypi/easydev
#
##############################################################################
"""Utilities related to the web

"""
import httplib


__all__ = ["isurl", "isurl_reachable"]



def isurl(url):
    """.. deprecated:: 0.6.12 use :param:`isurl_reachable instead`."""
    print("warning:: use isurl_reachable function instead")
    return isurl_reachable(url)


def isurl_reachable(url):
    """Checks if an URL exists or nor

    :param str url: the url to look for
    :return: True if it exists


    """
    if url.startswith("http://"):
        url = url.split("http://")[1]
    request = httplib.HTTPConnection(url)
    try:
        request.request("HEAD", '')
    except:
        return False
    # 302 is a redirection
    # 200 is okay
    if request.getresponse().status in [200, 302]:
        return True
    else:
        return False
