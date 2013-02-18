Contributing
================
The project is hosted on Assembla with a SVN from which you can get the source.

If you want to join, visit the website https://www.assembla.com/spaces/pyeasydev/wiki


Testing
====================

nosetests
------------

There is a test suite, which can be run using nosetests. The tests are in the
./test directory an using this command should run them::

    python setup.py nosetests

The latests coverage was about 70% of the code::

    Name                    Stmts   Miss  Cover   Missing
    -----------------------------------------------------
    easydev                    20      2    90%   12-13
    easydev.console            51     11    78%   42-46, 60, 63-68
    easydev.copybutton         50     28    44%   62-63, 69-71, 74-95, 98-101,105-107
    easydev.doc                 4      0   100%   
    easydev.logging_tools      23      0   100%   
    easydev.multisetup        155     56    64%   45-48, 83, 86, 97, 114, 198-201, 220-221, 253-259, 264, 283, 297-341, 345-346
    easydev.paths              39     13    67%   53-66, 88
    easydev.sphinx_themes       9      0   100%   
    easydev.tools              30      0   100%   
    -----------------------------------------------------
    TOTAL                     381    110    71%   
    ----------------------------------------------------------------------
    Ran 38 tests in 0.480s

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



