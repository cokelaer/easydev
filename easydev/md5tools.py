# -*- coding: utf-8 -*-
#
#  This file is part of easydev software
#
#  Copyright (c) 2012-2016 - Sequana Development Team
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/cokelaer/easydev
#
##############################################################################
import hashlib

def md5(fname, chunk=65536):
    """Return the MD5 checksums of a file

    Takes about 25 seconds on a 8Gb file.
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for this in iter(lambda: f.read(chunk), b""):
            hash_md5.update(this)
    return hash_md5.hexdigest()
