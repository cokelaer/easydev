easydev
##########

.. image:: https://badge.fury.io/py/easydev.svg
    :target: https://pypi.python.org/pypi/easydev

.. image:: https://github.com/cokelaer/easydev/actions/workflows/main.yml/badge.svg
    :target: https://github.com/cokelaer/easydev/actions/workflows/main.yml

.. image:: https://coveralls.io/repos/cokelaer/easydev/badge.svg?branch=main
   :target: https://coveralls.io/r/cokelaer/easydev?branch=main

.. image:: https://static.pepy.tech/personalized-badge/easydev?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads
    :target: https://pepy.tech/projects/easydev

:documentation: http://easydev-python.readthedocs.io/en/latest/
:contributions: Please join https://github.com/cokelaer/easydev
:source: Please use https://github.com/cokelaer/easydev
:issues: Please use https://github.com/cokelaer/easydev/issues
:Python version supported: 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

Overview
--------

The `easydev <http://pypi.python.org/pypi/easydev/>`_ package provides
miscellaneous utility functions and classes that are repeatedly useful during
the development of Python packages. The goal is to help developers speed up
their work by providing ready-to-use tools for common tasks such as parameter
validation, logging, progress bars, configuration files, multiprocessing, and
more.

It has been used as an incubator for other packages (e.g.,
`colormap <http://pypi.python.org/pypi/colormap>`_) and is used in projects
such as `bioservices <https://pypi.python.org/pypi/bioservices>`_,
`sequana <https://sequana.readthedocs.io>`_, and
`GDSCTools <https://gdsctools.readthedocs.io>`_.

Installation
------------

Install the latest release from PyPI::

    pip install easydev

Features
--------

- **Parameter validation** – ``check_param_in_list``, ``check_range``
- **Dictionary utilities** – ``swapdict``, ``AttrDict`` (access dict keys as attributes, supports nested dicts)
- **Logging** – coloured logging via ``Logging`` class
- **Progress bar** – ``Progress`` works in Python, IPython, and Jupyter notebooks
- **Timer** – measure elapsed time with the ``Timer`` context manager
- **Profiling** – ``do_profile`` decorator using ``line_profiler``
- **Configuration files** – ``CustomConfig`` and ``DynamicConfigParser`` for INI-style config management
- **Shell commands** – ``shellcmd`` and ``execute`` wrappers around subprocess/pexpect
- **File utilities** – ``touch``, ``mkdirs``, ``md5``
- **Multiprocessing** – ``MultiProcessing`` class for easy parallel job execution
- **Codecs** – ``to_list``, ``list2string`` and other conversion helpers
- **URL utilities** – ``isurl_reachable`` and related helpers
- **Sphinx integration** – bundled Sphinx theme and ``copybutton`` extension

Quick Start
-----------

Parameter validation::

    from easydev import check_param_in_list, check_range

    check_param_in_list("on", ["on", "off"])   # passes silently
    check_range(0.5, 0, 1)                     # passes silently

AttrDict – access nested dictionary keys as attributes::

    from easydev import AttrDict

    d = AttrDict(**{"server": {"host": "localhost", "port": 8080}})
    print(d.server.host)   # localhost
    d.server.port = 9090

Coloured logging::

    from easydev import Logging

    logger = Logging("myapp", "WARNING")
    logger.warning("something went wrong")
    logger.debug("not shown at WARNING level")
    logger.level = "DEBUG"
    logger.debug("now it is shown")

Progress bar::

    from easydev import Progress

    pb = Progress(100)
    for i in range(100):
        # do work here
        pb.animate(i + 1)

Timer::

    from easydev import Timer
    import time

    times = []
    with Timer(times):
        time.sleep(0.1)
    print(f"elapsed: {times[0]:.2f}s")

Multiprocessing::

    from easydev.multicore import MultiProcessing

    def square(n):
        return n * n

    t = MultiProcessing(maxcpu=4)
    for i in range(10):
        t.add_job(square, i)
    t.run()
    print(t.results)

Moving away from easydev
------------------------

easydev dates from a time when Python lacked many small conveniences. Most of
its tools now have a standard-library or well-maintained third-party
replacement, and new projects should not depend on easydev. The full
module-by-module guide is in the
`documentation <https://easydev.readthedocs.io/en/latest/migration.html>`_
(``doc/source/migration.rst``). Main replacements:

========================================= ======================================================
easydev                                   Use instead
========================================= ======================================================
``CustomConfig``, ``AppDirs``             ``platformdirs``
``DynamicConfigParser``                   ``configparser``
``AttrDict``                              ``types.SimpleNamespace`` / ``dataclasses``
``Logging``                               ``logging`` (+ ``colorlog``)
``Progress``                              ``tqdm``
``MultiProcessing``                       ``concurrent.futures.ProcessPoolExecutor``
``shellcmd``, ``execute``                 ``subprocess.run``
``mkdirs``, ``touch``, ``get_home``       ``pathlib`` / ``os.makedirs(exist_ok=True)``
``cmd_exists``                            ``shutil.which``
``md5``                                   ``hashlib.file_digest`` (Python 3.11+)
``browse``                                ``webbrowser.open``
``get_dependencies``                      ``importlib.metadata.requires``
``get_share_file``                        ``importlib.resources.files``
========================================= ======================================================

For example, replacing ``CustomConfig``::

    # before
    from easydev import CustomConfig
    config_dir = CustomConfig("myapp").user_config_dir

    # after
    from pathlib import Path
    from platformdirs import user_config_dir

    config_dir = Path(user_config_dir("myapp"))
    config_dir.mkdir(parents=True, exist_ok=True)

Changelog
---------

========= ==========================================================================
Version   Description
========= ==========================================================================
0.15.0    * fix ``is_mac`` (always returned False)
          * ``assert_list_almost_equal`` now warns (FutureWarning) when called without
            ``places``/``deltas`` (nothing is compared); raises ``ListMismatchError``
            (both ValueError and AssertionError)
          * add a migration guide (README and documentation) explaining how to
            replace easydev tools with the standard library, platformdirs, etc.
          * require Python >= 3.9
0.13.3    * update pyproject with contribs from @s-t-e-v-e-n-k see PR37
0.13.2    * replace mock with unittest.mock (fixes
            https://github.com/cokelaer/easydev/issues/20)
0.13.1    * fix get_dependencies
0.13.0    * fix requirements (line_profiler) and CI
0.12.2    * For developers: move to pyproject. add precommit
          * replace pkg_resources (deprecated) with importlib
          * replace appdirs with more generic platformdirs
========= ==========================================================================
