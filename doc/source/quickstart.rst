.. _quickstart:

User Guide
###############

There is no tutorial *per-se* in **easydev** since it is a set of
versatile and independent functionalities.

Here below, we describe some of available tools.

.. contents::

Progress bar
==============

Many tasks may take a while to finish especially when using a loop. A progress bar is usually
quite handy to keep track of the computation. **easydev** provides a Progress bar
that can be used in python, IPython, and IPython notebooks::

    from easydev import Progress
    p = Progress(1000)
    for i in range(0, 1000):
        # do something.
        p.animate(i+1)

Swapping key and value in a dictionary with swapdict
=======================================================

In Python, dictionaries are used everywhere. Sometimes, it is convenient
to swap the keys and values (values become keys and vice-versa).
The :func:`~easydev.tools.swapdict` can be used for that purpose:

.. doctest::

    >>> from easydev import swapdict
    >>> d = {'a':1, 'b':2}
    >>> inv = swapdict(d)
    >>> inv
    {1: 'a', 2: 'b'}

.. note:: values must be unique

The tools module
======================

In addition to the *swapdict* function, the :mod:`easydev.tools` module has
many more functionalities.

.. autosummary::
    :nosignatures:

    ~easydev.tools.precision
    ~easydev.tools.check_param_in_list
    ~easydev.tools.shellcmd
    ~easydev.tools.execute
    ~easydev.tools.touch
    ~easydev.tools.swapdict
    ~easydev.tools.mkdirs
    ~easydev.tools.AttrDict
    ~easydev.tools.DevTools

For :class:`~easydev.tools.DevTools` and :class:`~easydev.tools.AttrDict`,
please see :ref:`devtools` and :ref:`attrdict` sections, respetively.

Check validity of a values
----------------------------

The :func:`~easydev.tools.check_param_in_list` is used to check the validity of a parameter::

    >>> mode = "on"
    >>> check_param_in_list(mode, ["on", "off"])
    True

.. _attrdict:

AttrDict
-------------

This is a very convenient class to expose keys of a dictionary-like object as
attributes:

.. code-block:: python

    >>> from easydev import AttrDict
    >>> d = AttrDict({'val1':1})
    >>> d.val1
    1

This works also if you want to set a value::

    d.val2 = 2

.. _devtools:

The DevTools class
-------------------------

Little by little, small tools have been added in **easydev**. To make life easier such tools
have been gatherered within a single class called :class:`easydev.tools.DevTools`.

Usually, we can create just an instance and add it in a class as an accessible
set of functionalities. Consider the following example:

.. code-block:: python
    :linenos:

    from easydev import DevTools
    class MyTest(object):
        def __init__(self):
            self._devtools = Devtools()

        def plot_in_range(self, x):
            self._devtools.check_range(x, -2,2)
            # do something

        def sum(self, x):
            # sometimes it is a value, sometimes a list but
            # the function to be used accepts only list
            x = self._devtools.to_list(x)
            # do something with the list

        def switch(self, x):
            # this function will only understand x if it is a
            # value between 1 and 3 so let us check that
            self._devtools.check_param_in_list(x, [1,2,3])
            if x == 1:
                #do something
            else:
                #do something


The same code without DevTools would be twice as long. Consider for example the
line 7. You would need to type::

    if x < -2:
        raise ValueError('the value provided is incorrect....')
    if x >2:
        raise ValueError('the value provided is incorrect....')

logging
=========

The logging module uses the standard Python logging module and colorlog package
to provide a simple interface to include in your own library. For instance:

::

    >>> from easydev import Logging
    >>> log = Logging("easydev", "WARNING")
    >>> log.warning("using a logging")
    >>> log.debug("debug message not shown")
    >>> log.level = "DEBUG"
    >>> log.debug("debug message")
    WARNING [easydev]:  using a logging
    DEBUG   [easydev]:  debug message



Timer
=========

Timer populate a list variable with time spent in **with** statements
::

    from easydev import Timer
    import time
    times = []
    with Timer(times):
       time.sleep(0.1)
    with Timer(imes):
        time.sleep(0.2)
    sum(times)



Profiling
================

A quick way to check the profiling of a specific function or method is to use
the do_profile decorator (requires the package line_profiler)::

    from easydev import do_profile
    @do_profile()
    def test(a, b):
        a **2
        a + b
        a*b
        import time
        time.sleep(0.1)
    test(1,2)

Data related
==================

You can split a list into chunks using
:func:`~easydev.chunks.split_into_chunks`:

.. doctest::

    >>> from easydev import split_into_chunks
    >>> data = [1,1,2,2,3,3]
    >>> list(split_into_chunks(data, 3))
    [[1, 2], [1, 3], [2, 3]]

Note that it is an iterator (hence the list cast).


Sphinx tools
===============

Sphinx is a framework that ease the development of HTML documentation. I personally use Sphinx for all kind of projects, not only documentation of software. In order to have a uniform documentation a theme called **standard** is provided in the share/ directory of **easydev**. Moreover, **easydev** provides an easy way to obtained the path of this theme::

    >>> from easydev import *
    >>> p = get_path_sphinx_themes()

you can then check the presence of the themes::

    >>> import os
    >>> themes = os.listdir(p)
    >>> 'standard' in themes
    True

You can then use this path in your sphinx configuration file (conf.py). Here is a
piece of code extracted from the **conf.py** of this package::

    >>> import easydev
    >>> html_theme = 'standard' # one theme provided in easydev
    >>> html_theme_path = [easydev.get_path_sphinx_themes()]

Sphinx configuration file comes with lot of extensions from Sphinx itself or other packages (e.g., numpy or matplotlib). A useful extension is called copybutton (Found on Python official documentation website). As far as I known, it is not an official sphinx extension. It is available within **easydev**.

To use it, in your sphinx configuration file (conf.py), just add::

    import easydev
    extensions.append('easydev.copybutton')

It will copy the file in source/_static so your configuration file should set::

    html_static_path = ["source/_static"]




Multisetup
=============


Imagine you have tree structure with a bunch of projects::


    |-- pypiview
    |   |-- setup.py
    |   |-- pypiview
    |   |   |-- __init__.py
    |   |   |-- pypiview.py
    `-- spectrum
    |   |-- setup.py
    |   |-- spectrum
    |   |   |-- __init__.py

If you decided to install all those packages, you need to type::

    cd pypiview
    python setup.py install
    cd ../
    cd spectrum
    python setup.py install
    cd ../

This can be cumbersome if you've got lots of packages are do those operations
regularly. The module :mod:`~easydev.multisetup` provides a tool to simplify the
building of several python packages that are within the same directory. Arguments are
the same as those of setup.py.


Simply create a python file that contains the following code::

    from easydev import Multisetup
    if __name__ == '__main__':
        import sys
        packages = ['spectrum', 'pypiview']
        mysetup = Multisetup(curdir='.', commands=sys.argv[1:], packages=packages)
        mysetup.run()



Create a package layout in one command
=======================================

The package :mod:`~easydev.package` can build a package layout automatically. The type of layout is quite simple but alloas a quickstart:

.. code-block:: python

    >>> from easydev import PackageBuilder
    >>> p = PackageBuilder("myPackage")
    >>> p.buildPackage()

a package is built in the directory "myPackage". You can go in it and type::

    python setup.py install

Of course, no modules are to be found but it is a valid package. Besides, you should edit the setup.py file to set the version, author, email and so on.

You can also use the executable **easydev_buildPackage** provided with easydev.


Multiprocessing
====================

A :mod:`~easydev.multicore` class is provided to perform multiprocessing tasks. It allows to create
a list of jobs to be run in an asynchronous way. In other words your jobs do not need to communicate
between them.

Each job must be a function with arguments and optional arguments but must return an object (that will be stored in the results attribute). Typically, you will use this class as follows:

.. code-block:: python

     >>> from easydev.multicore import MultiProcessing
     >>> def test_func(n):
     ...    import time
     ...    time.sleep(n)
     ...    return n

     >>> t = MultiProcessing(maxcpu=4) # default is the number of CPU (returned by cpucount function)
     >>> t.add_job(test_func, 2)
     >>> t.add_job(test_func, 1)
     >>> t.run()

The :meth:`add_job` takes as input a function name followed by a lost of arguments. You can then introspect individual results::

  t.results
