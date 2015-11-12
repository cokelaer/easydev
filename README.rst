easydev
##########

.. image:: https://badge.fury.io/py/easydev.svg
    :target: https://pypi.python.org/pypi/easydev

.. image:: https://secure.travis-ci.org/cokelaer/easydev.png
    :target: http://travis-ci.org/cokelaer/easydev

.. image:: https://coveralls.io/repos/cokelaer/easydev/badge.svg?branch=master 
   :target: https://coveralls.io/r/cokelaer/easydev?branch=master 
   
.. image:: https://landscape.io/github/cokelaer/easydev/master/landscape.png
   :target: https://landscape.io/github/cokelaer/easydev/master

.. image:: https://badge.waffle.io/cokelaer/easydev.png?label=ready&title=Ready 
   :target: https://waffle.io/cokelaer/easydev

:contributions: Please join https://github.com/cokelaer/easydev
:issues: Please use https://github.com/cokelaer/easydev/issues
:Python version supported: 2.6, 2.7, 3.3, 3.4, 3.5

**easydev** is a package I use for the development of other software available on pypi.
It provides utilities that are of general usage for the development of Python packages.
It has been used also as an incubator for other packages (e.g.,
`http://pypi.python.org/pypi/colormap`).


For instance, it provides the sphinx templates being used for this documentation. It is also used by
other packages where documentation using Sphinx is being used (e.g., rtools, 
spectrum). It provides tools such as multisetup (to ease the development of
several packages within a single namespace), or **multigit**, which is an
executable installed with easydev::

    multigit pull --directories easydev colormap

There is also a set of functions to get the path of the share 
directory of any package. 

There is an executable to create a Python package layout automatically::

    easydev_buildPackage --help

There is also a handy Progress class that works in a Python shell, 
ipython notebook or a shell::

    from easydev import Progress
    pb = Progress(1000)
    for i in range(1,1000+1):
        # do something
        pb.animate(i)


Similar projects are pytools, pytoolbox.

For a full documentation, see the sphinx documentation at
`<http://pythonhosted.org/easydev/>`_

