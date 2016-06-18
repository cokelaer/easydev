.. _quickstart:

There is no quickstart or tutorial in **easydev** since it is a set of 
versatile tools. The documentation is the :ref:`ref_guide`.

However, here are some general tools.

.. contents::

The DevTools class
========================

We will tend to put small utilities within this :class:`easydev.tools.DevTools`.
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

and so on. The DevTools has more functionalities that those presented here and
will be extended little by little. 

Progress bar
==============

Many tasks may take a while to end and users may want to known the progress.
Here is a simple Progress bar that would work in python and IPython, and IPython
notebooks::

    from easydev import Progress
    p = Progress(1000)
    for i in range(0,1000):
        # do something.
        p.animate(i+1)

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

Sphinx configuration file comes with lot of extensions from Sphinx itself or other packages (e.g., numpy or
matplotlib). A useful extension is called copybutton (I do not remember where I found it...). For now, we provide it within easydev so that it can be used easily by all the packages::

    >>> from easydev import copybutton
    >>> p = copybutton.get_copybutton_path()

Again, it can be used within you configuration file::

    extensions.append('easydev.copybutton')
    jscopybutton_path = easydev.copybutton.get_copybutton_path()





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
    
The tools module
======================

In addition to the DevTools presented above, the :mod:`easydev.tools` module
also provide some other functionalities.


Check validity of a values
----------------------------

The module :mod:`~easydev.tools` provides a few simple functions amongst which,
the :func:`~easydev.tools.checkParam` is used to check the validity of a parameter::

    >>> mode = "on"
    >>> checkParam(mode, ["on", "off"])
    True


AttrDict
-------------

This is a very convenient class to expose keys of a dictionary-like object as
attributes::

    >>> from easydev import AttrDict
    >>> d = AttrdDict({'val1':1})
    >>> d.val1
    1


Create a package layout in one command
=======================================

The package :mod:`~easydev.package` can build a package layout automatically. The type of layout is quite simple but alloas a quickstart::

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

Each job must be a function with arguments and optional arguments but must return an object (that will be stored in the results attribute). Typically, you will use this class as follows::

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




