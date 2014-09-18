Contributing
================
The project is hosted on Assembla with a SVN from which you can get the source.

If you want to join, visit the website https://www.github.com/cokelaer/easydev


Testing
====================

nosetests
------------

There is a test suite, which can be run using nosetests. The tests are in the
./test directory an using this command should run them::

    python setup.py nosetests



doctest
-------------

There are some examples in the docstrings that use the doctest extension. For
those familiar with sphinx, you can type the following command in the ./doc
directory::

    make doctest

to perform more tests


Release Notes
==============

.. include:: ../ChangeLog.txt 



