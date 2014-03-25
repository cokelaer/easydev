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


    Name                     Stmts   Miss  Cover   Missing
    ------------------------------------------------------
    easydev                     38      2    95%   12-13
    easydev.colors             305     17    94%   678-687, 776-782
    easydev.config_tools       114     11    90%   209, 283, 285, 289-290, 308-310, 330, 395-396
    easydev.console             53     12    77%   45-49, 62, 71, 74-79
    easydev.copybutton          60     28    53%   90-91, 97-99, 102-123, 126-129, 133-135
    easydev.decorators          52     33    37%   45-80, 85-96, 123
    easydev.dependencies        10      0   100%   
    easydev.doc                  5      0   100%   
    easydev.easytest            16      4    75%   57-58, 62-63
    easydev.logging_tools       34      0   100%   
    easydev.multicore           32      0   100%   
    easydev.multisetup         154     55    64%   50-53, 105, 108, 119, 136, 220-223, 242-243, 271-277, 282, 315-359, 363-364
    easydev.package            127     27    79%   226-227, 240, 247, 253-268, 279, 343, 352, 380-391
    easydev.paths               54     13    76%   52, 60-70, 90, 115, 121
    easydev.pypi_downloads      19      0   100%   
    easydev.setuptools          12      0   100%   
    easydev.sphinx_themes       15      0   100%   
    easydev.tools               45      2    96%   42, 75
    easydev.url                 16      1    94%   49
    easydev.xfree86              2      0   100%   
    ------------------------------------------------------
    TOTAL                     1163    205    82%   
    ----------------------------------------------------------------------
    Ran 52 tests in 8.392s






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



