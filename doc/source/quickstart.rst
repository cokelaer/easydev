.. _quickstart:

Quick Start
#################

.. contents::


Sphinx tools
===============

Sphinx is a framework that ease the development of HTML documentation. In cnolab and associated projects, we use Sphinx to create documentation. In order to have a uniform documentation a theme called **cno** is provided in the share/ directory of **easydev**. Moreover, **easydev** provides an easy way to obtained the path of this theme::

    >>> from easydev import *
    >>> p = get_path_sphinx_themes()

you can then check the presence of the cno themes::
 
    >>> import os
    >>> themes = os.listdir(p)
    >>> 'cno' in themes
    True


You can then use this path in your sphinx configuration file (conf.py). Here is a
piece of code extracted from the **conf.py** of this package::

    >>> import easydev
    >>> html_theme = 'cno' # one theme provided in easydev
    >>> html_theme_path = [easydev.get_path_sphinx_themes()]

Sphinx configuration file comes with lot of extensions from Sphinx itself or other packages (e.g., numpy or
matplotlib). A useful extension is called copybutton (I do not remember where I found it...sorry for the author).
For now, we provide it within easydev so that it can be used easily by all
the package::

    >>> from easydev import copybutton
    >>> p = copybutton.get_copybutton_path()

Again, it can be used within you configuration file::

    extensions.append('easydev.copybutton')
    jscopybutton_path = easydev.copybutton.get_copybutton_path()





Multisetup
=============

The module :mod:`~easydev.multisetup` provides a tool to simplify the
building of several python packages that are within the same directory. Arguments are 
the same as those of setup.py.


Simply create a python file that contains the following code::


    if __name__ == '__main__':
        import sys
        packages = ['deploy', 'data', 'wrapper', 'greedy', 'pipeline', 'apps']
        mysetup = Multisetup(curdir='.', commands=sys.argv[1:], packages=packages)
        mysetup.run()
    

Check Parameter value
======================

The module :mod:`~easydev.tools` provides a few simple functions amongst which,
the `checkParam` is used to check the validity of a parameter::

    >>> mode = "on"
    >>> checkParam(mode, ["on", "off"])
    True


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

