#############################
EASYDEV documentation
#############################


.. raw:: html

    <div style="width:40%">
    <a href="https://pypi.python.org/pypi/easydev"> <img src="https://badge.fury.io/py/easydev.svg"></a> 
    <a href="https://travis-ci.org/cokelaer/easydev"> <img src="https://travis-ci.org/cokelaer/easydev.svg?branch=master"></a>
    <a href="https://coveralls.io/github/cokelaer/easydev?branch=master"> <img src="https://coveralls.io/repos/github/cokelaer/easydev/badge.svg?branch=master"></a>
    <a href="https://landscape.io/github/cokelaer/easydev/master"> <img src="https://landscape.io/github/cokelaer/easydev/master/landscape.png"></a>
    </div>


:documentation: http://easydev-python.readthedocs.io/en/latest/
:contributions: Please join https://github.com/cokelaer/easydev
:source: Please use https://github.com/cokelaer/easydev
:issues: Please use https://github.com/cokelaer/easydev/issues
:Python version supported: 2.6, 2.7, 3.3, 3.4, 3.5



Motivation
=============


The package `easydev <http://pypi.python.org/pypi/easydev/>`_ provides
miscellaneous functions and files that are repeatidly used in other Python
packages.

Some functions are very simple such as the :func:`~easydev.tools.swapdict`,
which inverts the keys/values in a dictionary (assuming unique keys):

.. doctest::

    >>> from easydev import swapdict
    >>> d = {'a':1, 'b':2}
    >>> inv = swapdict(d)
    >>> inv
    {1: 'a', 2: 'b'}

Other functions such as the progress bar (:mod:`~easydev.progressbar`) are more
complex and **easydev** should be very useful in speeding up development.
Another example is the :func:`~easydev.tools.AttrDict` function: it makes the keys of a dictionary
accessible as attributes. Meaning that you can get or set the values quickly as
follows:

.. doctest::

    >>> from easydev import AttrDict
    >>> d = AttrDic(**{'a':1, 'b':2})
    >>> d.a
    1
    >>> d.a = 10
    >>> d.a
    10

Another example is the :mod:`~easydev.multicore` module that provides
a simple tool to perform a multi-core analysis in Python. Note, however,
that specialised library would surely cover more aspects. Yet, in a few lines
of code many applications would work out of the box with this code::

    from easydev.multicore import MultiProcessing
    mp = MultiProcessing(maxcpu=4)
    mp.add_job(test_func, 2)
    mp.add_job(test_func, 1)
    mp.run()


There are many such functions in **easydev** and the best would be to have a
look at the :ref:`user_guide` for more examples and the :ref:`ref_guide` guide for an
exhaustive list of tools available.

There are also a few applications installed with **easydev**. One is the
**browse** application that is equivalent to **open** under Mac. The interest is
that it is multi-platform.

Note also that **easydev** was starting a few years ago and that some
functionalities did not exist back then. Some functionalities available in
easydev may now exist in standard modules of Python.

.. toctree::
    :maxdepth: 2
    :numbered:

    installation
    quickstart
    references

