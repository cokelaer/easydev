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
import httplib


__all__= ["isurl"]


def isurl(url):
    """Checks if an URL exists or nor

    :param str url: the url to look for
    :return: True if it exists


    """
    if url.startswith("http://"):
        url = url.split("http://")[1]
    c = httplib.HTTPConnection(url)
    try:
        c.request("HEAD", '')
    except:
        return False
    # 302 is a redirection
    # 200 is okay
    if c.getresponse().status in [200, 302]:
        return True
    else:
        return False
