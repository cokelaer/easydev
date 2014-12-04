.. _quickstart:

Tools available
#################

There is no quickstart or tutorial in **easydev**. It is a set of tools that are
handy for developing tools in Python. However, here are some general tools that 
I used a lot.

.. contents::


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

