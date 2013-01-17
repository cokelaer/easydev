# -*- python -*-
#
#  Copyright (c) 2011-2012 - EBI
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://www.ebi.ac.uk/~cokelaer/easydev
#
##############################################################################

__all__ = ["underline"]

def underline(text):
    """return underlined text. used in sphinx text."""
    l = len(text)
    return text + "\n" + l*"="

