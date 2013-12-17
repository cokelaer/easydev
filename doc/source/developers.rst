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
    easydev                    29      2    93%   12-13
    easydev.config_tools      140     52    63%   83, 129-132, 135, 142-143, 145, 173, 206, 208, 212-213, 229, 232-234, 270-271, 280-292, 297-298, 318-337
    easydev.console            53     12    77%   45-49, 62, 71, 74-79
    easydev.copybutton         60     28    53%   90-91, 97-99, 102-123, 126-129,133-135
    easydev.dependencies        9      6    33%   7-12
    easydev.doc                 5      0   100%   
    easydev.logging_tools      29      4    86%   76-77, 80-81
    easydev.multicore          31      3    90%   51-53
    easydev.multisetup        154     55    64%   50-53, 105, 108, 119, 136,  220-223, 242-243, 271-277, 282, 315-359, 363-364
    easydev.package           127     27    79%   223-224, 237, 244, 250-265, 276, 340, 349, 377-388
    easydev.paths              49     14    71%   51, 58-68, 88, 109, 112-113
    easydev.sphinx_themes      15      0   100%   
    easydev.tools              33      1    97%   63
    easydev.url                13      1    92%   42
    -----------------------------------------------------
    TOTAL                     747    205    73%   
    ----------------------------------------------------------------------
    Ran 30 tests in 9.410s



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



