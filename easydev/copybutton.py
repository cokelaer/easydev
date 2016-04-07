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
#  Website: https://github.com/cokelaer/easydev
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""This module is a copy of a sphinx extension. unknown origin.

    added by Thomas Cokelaer: get_copybutton_path function.

    Create a sphinx extension based on copybutton javascript from python website

Requires sphinx to be installed. imports are inside functions so not stricly
speaking required for the installation.
"""
import os
from os.path import join as pj
import shutil
try:
    from docutils import nodes
except Exception:
    # if docutils is not installed
    class Dummy():
        SkipNode = Exception
    nodes = Dummy()


__all__ = ["get_copybutton_path", ]


def copy_javascript_into_static_path(static="_static", filepath="copybutton.js"):
    """This script can be included in a sphinx configuration file to copy the
    copybutton in the static directory

    :param str static: name of the static path (_static by default)
    :param filename: full path of the file to copy

    :Details: If the path *static* does not exists, it is created. If the
        filename in filepath is already in the path *static*, nothing need to be done.
        Otherwise, the file is copied in *static* directory.

    """

    if os.path.isdir(static):
        pass
    else:
        os.mkdir(static)

    filename = os.path.split(filepath)[1]
    if os.path.isfile(static + os.sep + filename):
        pass
    else:
        shutil.copy(filepath, static + os.sep + filename)



def get_copybutton_path():
    """Return the path where the to find the copybutton javascript

    Copy the copybutton.js javascript in the share directory of easydev so
    that it is accesible by all packages that required it by typing:

    .. doctest::

        >>> from easydev import get_copybutton_path
        >>> p = get_copybutton_path()

    It can then be added with a Sphinx configuration file::

        jscopybutton_path = easydev.copybutton.get_copybutton_path()

    """
    import easydev
    try: # install mode
        packagedir = easydev.__path__[0]
        packagedir = os.path.realpath(pj(packagedir, 'share'))
        os.listdir(packagedir) # if this faisl, we are in deve mode
    except OSError:
        try:
            packagedir = easydev.__path__[0]
            packagedir = os.path.realpath(pj(packagedir, '..', 'share'))
        except:
            raise IOError("could not find data directory")
    return pj(packagedir, "copybutton.js")



def html_visit_math(self, node):
    self.body.append(self.starttag(node, 'span', '', CLASS='math'))
    self.body.append(self.encode(node['latex']) + '</span>')
    raise nodes.SkipNode

def html_visit_displaymath(self, node):
    if node['nowrap']:
        self.body.append(self.starttag(node, 'div', CLASS='math'))
        self.body.append(node['latex'])
        self.body.append('</div>')
        raise nodes.SkipNode
    for i, part in enumerate(node['latex'].split('\n\n')):
        part = self.encode(part)
        if i == 0:
            # necessary to e.g. set the id property correctly
            if node['number']:
                self.body.append('<span class="eqno">(%s)</span>' %
                                 node['number'])
            self.body.append(self.starttag(node, 'div', CLASS='math'))
        else:
            # but only once!
            self.body.append('<div class="math">')
        if '&' in part or '\\\\' in part:
            self.body.append('\\begin{split}' + part + '\\end{split}')
        else:
            self.body.append(part)
        self.body.append('</div>\n')
    raise nodes.SkipNode

def builder_inited(app):
    from sphinx.application import ExtensionError
    if not app.config.jscopybutton_path:
        raise ExtensionError('jscopybutton_path config value must be set for the '
                             'jscopybutton extension to work')
    app.add_javascript(app.config.jscopybutton_path)


def setup(app):
    from sphinx.ext.mathbase import setup_math as mathbase_setup
    mathbase_setup(app, (html_visit_math, None), (html_visit_displaymath, None))
    app.add_config_value('jscopybutton_path', '', False)
    app.connect('builder-inited', builder_inited)
