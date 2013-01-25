# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2013 
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
"""Format colored consoled output. Modified from sphinx.util.console

.. doctest::

    from easydev.console import bold, red, green, \
           color_terminal, nocolor, underline, purple
    print red("test")

"""

import os
import sys

codes = {}

def get_terminal_width():
    """Borrowed from the py lib."""
    try:
        import termios, fcntl, struct
        call = fcntl.ioctl(0, termios.TIOCGWINSZ,
                           struct.pack('hhhh', 0, 0, 0, 0))
        height, width = struct.unpack('hhhh', call)[:2]
        terminal_width = width
    except (SystemExit, KeyboardInterrupt):
        raise
    except:
        # FALLBACK
        terminal_width = int(os.environ.get('COLUMNS', 80)) - 1
    return terminal_width

_tw = get_terminal_width()

def term_width_line(text):
    if not codes:
        # if no coloring, don't output fancy backspaces
        return text + '\n'
    else:
        return text.ljust(_tw) + '\r'

def color_terminal():
    if not hasattr(sys.stdout, 'isatty'):
        return False
    if not sys.stdout.isatty():
        return False
    if 'COLORTERM' in os.environ:
        return True
    term = os.environ.get('TERM', 'dumb').lower()
    if term in ('xterm', 'linux') or 'color' in term:
        return True
    return False


def nocolor():
    codes.clear()

def coloron():
    codes.update(_orig_codes)

def colorize(name, text):
    return codes.get(name, '') + text + codes.get('reset', '')

def create_color_func(name):
    def inner(text):
        return colorize(name, text)
    globals()[name] = inner

_attrs = {
    'reset':     '39;49;00m',
    'bold':      '01m',
    'faint':     '02m',
    'standout':  '03m',
    'underline': '04m',
    'blink':     '05m',
}

for _name, _value in _attrs.items():
    codes[_name] = '\x1b[' + _value

_colors = [
    ('black',     'darkgray'),
    ('darkred',   'red'),
    ('darkgreen', 'green'),
    ('brown',     'yellow'),
    ('darkblue',  'blue'),
    ('purple',    'fuchsia'),
    ('turquoise', 'teal'),
    ('lightgray', 'white'),
]

for i, (dark, light) in enumerate(_colors):
    codes[dark] = '\x1b[%im' % (i+30)
    codes[light] = '\x1b[%i;01m' % (i+30)

_orig_codes = codes.copy()

for _name in codes:
    create_color_func(_name)
