

#############################
EASYDEV documentation
#############################


Motivation 
###########


The package `easydev <http://pypi.python.org/pypi/easydev/>`_ provides
miscellaneous functions and files that are repeatidly used in other packages but
have no common semantic or purpose. It also provides executables that ease the development of new packages.
The targetted audience is therefore developers of Python packages.

.. warning:: I'm not pretending to provide universal and bug-free tools. The
    tools provided may also change. However, since I'm using the tools provided
    in easydev in many other packages, it tends to be stable. 
    I'm using **easydev** in other Python packages such as 
    `bioservices <https://pypi.python.org/pypi/bioservices>`_.


Here are some features:

 #. Builds a python package layout automatically with an executable. See :mod:`~easydev.package`
 #. A user interface to run multiple jobs with :mod:`~easydev.multicore`
 #. Some functions to access to the share/data directories of python packages
    installed in develop or install modes.
 #. Gather sphinx themes being used in different package documentations (e.g., `rtools <http://pypi.python.org/pypi/rtools>`_, `CellNOpt <http://www.cellnopt.org>`_).
 #. Set of tools to manipulate multi packaging under Python (see e.g., :mod:`~easydev.multisetup`).
 #. A simple interface to run shell command (see :mod:`~easydev.tools`).
 #. A logging class to ease manipulation of the logging standard Python module (see :mod:`~easydev.logging_tools`).
 #. Quickly check if an url exists (see :mod:`~easydev.url.isurl`)
 #. Decorators: :mod:`~easydev.decorators`


Installation
###################

Prerequisites
===============

Of course, you will need to install `Python <http://www.python.org/download/>`_
(linux and mac users should have it installed already). We recommend also to install `ipython <http://ipython.org/>`_, which provides a more flexible shell alternative to the python shell itself.

Installation
================
Since **easydev** is available on `PyPi <http://pypi.python.org/>`_, the following command should install the package and its dependencies automatically:: 

    pip install easydev

User guide
##################


.. toctree::
    :maxdepth: 2
    :numbered:

    quickstart.rst

Developer Guide
####################

.. toctree::
    :maxdepth: 2
    :numbered:

    developers

Reference Guide
##################


.. toctree::
    :maxdepth: 2
    :numbered:

    references

