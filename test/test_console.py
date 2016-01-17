from easydev.console import *
from easydev import console

def test_get_terminal_width():
    get_terminal_width()

def test_term_width_line():
    term_width_line('text')

def test_color_terminal():
    color_terminal()

def test_print_color():
    print(purple('\t%s' % "test"))
    print(red('\t%s' % "test"))
