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
:source: Please use https://github.com/cokelaer/easydev
:issues: Please use https://github.com/cokelaer/easydev/issues
:Python version supported: 2.6, 2.7, 3.3, 3.4, 3.5

**easydev** is a package I use for the development of other software available on pypi such as dreamtools, bioservices, gdsctools, biokit, cno, ...


It provides utilities that are of general usage for the development of Python packages either to ease the creation of a package layout or to ease the development of code. It has been used also as an incubator for other packages (e.g.,
`http://pypi.python.org/pypi/colormap`) and is stable.

It is difficult to describe **easydev** since the tools are heteregeneous.
However, here are some of the tools available.

First, there are some standalone available when you install easydev. For
instance, it provides a tool like **multisetup** (to ease the development of
several packages within a single namespace), or **multigit** that will execute a
git command across several directories::

    multigit pull --directories easydev colormap


There is an executable to create a Python package layout automatically::

    easydev_buildPackage --help

There are a few functionalities for developer that I use a lot. For instance,
a way to get the path of the share directory of any package, which is 
very convenient to access to shared files from tests or from the code. Another
handy tool is a Progress class that works in a Python shell, 
ipython notebook or a shell::

    from easydev import Progress
    pb = Progress(1000)
    for i in range(1,1000+1):
        # do something
        pb.animate(i)

Another useful to is the AttrDict that allows one to set and get dictionary
contents as if there were attributes::

    >>> from easydev impotr AttrDict
    >>> d = AttrDict()
    >>> d.a = 1
    >>> d['a'] # now the key is available in the dictionary !
    1

There are more tools available and described in the documentation. For a full documentation, see the sphinx documentation at
`<http://pythonhosted.org/easydev/>`_

