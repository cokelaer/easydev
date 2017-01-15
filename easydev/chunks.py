# -*- coding: utf-8 -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2012-2017 - easydev
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/cokelaer/easydev
#  documentation: http://easydev-python.readthedocs.io
#
##############################################################################

#http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
#
# Here's a generator that yields the chunks you want:
# 
# def chunks(l, n):
#    """Yield successive n-sized chunks from l."""
#    for i in range(0, len(l), n):
#        yield l[i:i+n]
#
#The issue here is that the chunks are not evenly sized chunks
#

__all__ = ['split_into_chunks']


try:
    range = xrange # py2
except:
    pass  #py3


def split_into_chunks(items, maxchunks=10):
    """Split a list evenly into N chunks

    .. doctest::

        >>> from easydev import split_into_chunks
        >>> data = [1,1,2,2,3,3]
        >>> list(split_into_chunks(data, 3))
        [[1, 2], [1, 3], [2, 3]]


    """
    chunks = [[] for _ in range(maxchunks)]
    for i, item in enumerate(items):
        chunks[i % maxchunks].append(item)
    return filter(None, chunks)
