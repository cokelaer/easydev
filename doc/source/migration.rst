.. _migration:

Moving away from easydev
########################

easydev started many years ago, when Python itself (and its ecosystem) lacked
many small conveniences. Most of what easydev offers is now available in the
standard library or in well-maintained third-party packages. **New code should
not depend on easydev**, and existing code can usually drop it with a few
lines of changes. This page lists, module by module, what to use instead.

.. contents::
    :local:
    :depth: 2

Summary
=======

Minimum Python versions are given when a replacement needs more than 3.9.

================================================== =====================================================================
easydev                                            Replacement
================================================== =====================================================================
``CustomConfig``, ``AppDirs``                      ``platformdirs`` + ``pathlib`` (:ref:`details <mig_customconfig>`)
``DynamicConfigParser``                            ``configparser.ConfigParser``
``AttrDict``                                       ``types.SimpleNamespace``, ``dataclasses`` or plain ``dict``
``Logging``                                        ``logging`` (+ ``colorlog`` for colors)
``Progress``, ``progress_bar``                     ``tqdm`` or ``rich.progress``
``MultiProcessing``                                ``concurrent.futures.ProcessPoolExecutor``
``Timer``                                          ``time.perf_counter`` or a ``contextlib`` context manager
``do_profile``                                     ``line_profiler`` directly
``shellcmd``, ``execute``                          ``subprocess.run``
``mkdirs``                                         ``os.makedirs(path, exist_ok=True)`` / ``Path.mkdir``
``touch``                                          ``pathlib.Path.touch``
``md5``                                            ``hashlib.file_digest`` (3.11+) or ``hashlib.md5``
``get_home``                                       ``pathlib.Path.home``
``cmd_exists``                                     ``shutil.which``
``get_platform``, ``is_windows``, ...              ``sys.platform`` / ``platform.system``
``browse``                                         ``webbrowser.open``
``isurl_reachable``                                ``urllib.request`` or ``requests`` / ``httpx``
``get_terminal_width``, ``term_width_line``        ``shutil.get_terminal_size``
``swapdict``                                       dict comprehension
``precision``                                      ``round`` / ``math.trunc``
``check_range``, ``check_param_in_list``           plain ``if`` + ``raise ValueError``
``to_list``, ``tolist``, ``list2string``           small helper / ``", ".join(map(str, x))``
``split_into_chunks``                               slicing, ``numpy.array_split`` or ``itertools.batched`` (3.12+)
``get_dependencies``                               ``importlib.metadata.requires``
``get_package_location``, ``get_share_file``, ...  ``importlib.resources.files``
``underline``                                      f-string
``SmartFormatter``                                 ``argparse.RawTextHelpFormatter``
``assert_list_almost_equal``                       ``pytest.approx``
``trysetattr``                                     ``pytest.raises(AttributeError)``
``TempFile``                                       ``tempfile.NamedTemporaryFile`` / pytest ``tmp_path``
``ifpandas``, ``ifpylab``                          ``pytest.importorskip`` / ``importlib.util.find_spec``
``sphinx_themes``, ``copybutton``                  ``sphinx-copybutton`` and a theme from PyPI
``in_ipynb``                                       no stable replacement (see below)
``requires`` decorator                             no replacement; copy it (about 20 lines)
================================================== =====================================================================

.. _mig_customconfig:

CustomConfig and AppDirs
========================

:class:`~easydev.config_tools.CustomConfig` is a thin layer over
:class:`~easydev.appdirs.AppDirs`, itself a thin wrapper around
`platformdirs <https://platformdirs.readthedocs.io>`_. It only returns (and
creates on access) the user configuration directory of an application.
``platformdirs`` does the same directly.

Before:

.. code-block:: python

    from easydev import CustomConfig

    config = CustomConfig("damona")
    config.init()                      # creates the directory
    path = config.user_config_dir      # str, directory is created if missing

After:

.. code-block:: python

    from pathlib import Path
    from platformdirs import user_config_dir

    config_dir = Path(user_config_dir("damona"))
    config_dir.mkdir(parents=True, exist_ok=True)

Other directories are available the same way (``user_data_dir``,
``user_cache_dir``, ``user_log_dir``, ``site_config_dir``, ...)::

    from platformdirs import PlatformDirs

    dirs = PlatformDirs("damona")
    dirs.user_config_dir, dirs.user_cache_dir, dirs.user_data_dir

If your code relied on the ``AppDirs`` class of easydev, ``PlatformDirs`` is a
drop-in replacement (same property names). ``platformdirs`` is already a
dependency of easydev, so no new package is pulled in.

Differences to be aware of:

- ``CustomConfig`` printed ``Creating directory ...`` when creating the
  directory; the code above is silent.
- ``CustomConfig.remove()`` called ``os.rmdir``, which only works on an empty
  directory. Use ``shutil.rmtree`` if you want to delete a populated one.

DynamicConfigParser
===================

:class:`~easydev.config_tools.DynamicConfigParser` extends
``configparser.ConfigParser`` with attribute access (``c.section.option``)
and a ``save`` method. Use the standard class::

    from configparser import ConfigParser

    config = ConfigParser()
    config.read("settings.ini")
    host = config["server"]["host"]
    port = config.getint("server", "port")

    config["server"]["port"] = "9090"
    with open("settings.ini", "w") as fout:
        config.write(fout)

For new configuration files, consider TOML (``tomllib`` in the standard
library from Python 3.11 for reading, ``tomli-w`` for writing).

AttrDict
========

.. code-block:: python

    # before
    from easydev import AttrDict
    d = AttrDict(**{"server": {"host": "localhost"}})
    d.server.host

    # after: a dataclass gives you attributes, types and defaults
    from dataclasses import dataclass, field

    @dataclass
    class Server:
        host: str = "localhost"
        port: int = 8080

    @dataclass
    class Settings:
        server: Server = field(default_factory=Server)

    settings = Settings()
    settings.server.host

For quick, untyped, flat objects use ``types.SimpleNamespace(host="localhost")``.
``AttrDict.to_json`` / ``from_json`` are ``json.dumps(d)`` / ``json.load(f)``
on a plain dict (or ``dataclasses.asdict``).

Logging
=======

.. code-block:: python

    # before
    from easydev import Logging
    logger = Logging("myapp", "WARNING")
    logger.level = "DEBUG"

    # after
    import logging
    import colorlog

    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter("%(log_color)s%(levelname)-8s[%(name)s:%(lineno)d]: %(reset)s%(message)s")
    )
    logger = logging.getLogger("myapp")
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)
    logger.setLevel("DEBUG")

Drop ``colorlog`` and the handler lines if you do not need colors; a library
should only call ``logging.getLogger(__name__)`` and let the application
configure handlers.

Progress bar
============

.. code-block:: python

    # before
    from easydev import Progress
    pb = Progress(100)
    for i in range(100):
        pb.animate(i + 1)

    # after
    from tqdm import tqdm
    for i in tqdm(range(100)):
        ...

``tqdm`` handles terminals, IPython and Jupyter automatically.

Multiprocessing
===============

.. code-block:: python

    # before
    from easydev.multicore import MultiProcessing
    t = MultiProcessing(maxcpu=4)
    for i in range(10):
        t.add_job(square, i)
    t.run()
    results = t.results

    # after (results are returned in submission order)
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, range(10)))

As with easydev, the function must be defined at module level (picklable).

Timer and profiling
===================

.. code-block:: python

    # before
    from easydev import Timer
    times = []
    with Timer(times):
        work()

    # after
    import time
    t0 = time.perf_counter()
    work()
    elapsed = time.perf_counter() - t0

``do_profile`` is a small wrapper around ``line_profiler.LineProfiler``; use
``line_profiler`` (``kernprof -l -v script.py`` with ``@profile``) directly.

Shell commands and files
========================

.. code-block:: python

    import hashlib
    import shutil
    import subprocess
    import sys
    import webbrowser
    from pathlib import Path

    # shellcmd(cmd) / execute(cmd): raise on failure, capture output as text
    out = subprocess.run("ls -l", shell=True, check=True, capture_output=True, text=True).stdout
    # preferably without shell=True:
    out = subprocess.run(["ls", "-l"], check=True, capture_output=True, text=True).stdout

    # mkdirs(path)
    Path("a/b/c").mkdir(parents=True, exist_ok=True)

    # touch(path)
    Path("file.txt").touch()

    # md5(path) -- Python 3.11+
    with open("big.bin", "rb") as f:
        digest = hashlib.file_digest(f, "md5").hexdigest()

    # get_home()
    Path.home()

    # cmd_exists("samtools")
    shutil.which("samtools") is not None

    # get_platform(), is_windows(), is_linux(), is_mac()
    sys.platform.startswith("win")
    sys.platform.startswith("linux")
    sys.platform == "darwin"

    # browse(url)
    webbrowser.open("https://github.com/cokelaer/easydev")

.. note::

    ``easydev.shellcmd`` treats any output on stderr as an error and ignores
    the exit status (a failing command that prints nothing to stderr does not
    raise). This legacy behavior is kept for backward compatibility;
    ``subprocess.run(..., check=True)`` raises on a non-zero exit code instead.
    ``is_mac()`` always returned ``False`` before 0.15.0.

Small helpers
=============

.. code-block:: python

    # swapdict(d)
    swapped = {v: k for k, v in d.items()}

    # check_param_in_list(mode, ["on", "off"])
    if mode not in ("on", "off"):
        raise ValueError(f"mode must be one of ('on', 'off'), got {mode!r}")

    # check_range(x, 0, 1)
    if not 0 <= x <= 1:
        raise ValueError(f"{x} must be between 0 and 1")

    # list2string([1, 2], sep=";")
    "; ".join(map(str, [1, 2]))

    # to_list(x) for scalars / sequences
    items = list(x) if isinstance(x, (list, tuple)) else [x]

    # split_into_chunks(items, 3): round-robin split, like easydev
    chunks = [items[i::3] for i in range(3)]

    # underline("title")
    f"{title}\n{'=' * len(title)}"

    # get_terminal_width()
    import shutil
    shutil.get_terminal_size().columns

``easydev.tools.precision`` truncates instead of rounding
(``precision(2.129) == 2.12``, kept for backward compatibility); use ``math.trunc(x * 100) / 100`` for the
same result or ``round(x, 2)`` if rounding is what you actually want.

Package metadata and data files
===============================

.. code-block:: python

    # get_dependencies("easydev")
    from importlib.metadata import requires
    requires("easydev")      # raw requirement strings, may be None

    # get_share_file("mypackage", "data", "file.txt")
    from importlib.resources import files
    path = files("mypackage") / "share" / "data" / "file.txt"

``importlib.resources.files`` also works for zipped installs, which the
directory-walking logic of ``get_shared_directory_path`` does not.

Command-line and tests
======================

.. code-block:: python

    # SmartFormatter: keep newlines in argparse help
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    # assert_list_almost_equal([0, 0, 1], [0, 0, 0.9999], places=3)
    import pytest
    assert [0, 0, 1] == pytest.approx([0, 0, 0.9999], abs=1e-3)

    # trysetattr(obj, "b", 1, possible=False)
    with pytest.raises(AttributeError):
        obj.b = 1

    # TempFile
    def test_something(tmp_path):
        path = tmp_path / "out.txt"

    # ifpandas / ifpylab
    pd = pytest.importorskip("pandas")

.. note::

    ``assert_list_almost_equal`` compares nothing when neither ``places`` nor
    ``deltas`` is given (it now issues a ``FutureWarning``), and ignores
    length differences. Migrating to ``pytest.approx`` makes the test stricter.

Sphinx helpers
==============

``easydev.copybutton`` ships the JavaScript of a "copy" button for code blocks
and ``easydev.sphinx_themes`` ships a few themes. Use the maintained
`sphinx-copybutton <https://sphinx-copybutton.readthedocs.io>`_ extension
(``extensions = ["sphinx_copybutton"]`` in ``conf.py``) and a theme from PyPI
such as ``sphinx-rtd-theme`` or ``furo``.

What has no direct replacement
==============================

- ``easydev.misc.in_ipynb``: it inspects the IPython kernel config and is
  fragile. Prefer feature-testing (e.g. let ``tqdm.auto`` decide how to render)
  or copy the function.
- ``easydev.decorators.requires``: checks that attributes exist before running
  a method. Small enough to copy into your project.
- ``easydev.tools.DevTools``: an aggregate of other helpers; use the
  individual replacements above.

Dropping the dependency
=======================

1. ``grep -rn "easydev" .`` to list the imports in your project.
2. Replace each usage with the recipes above.
3. Remove ``easydev`` from ``pyproject.toml`` / ``requirements`` / conda recipe.
4. Add what you now use directly (``platformdirs``, ``colorlog``, ``tqdm``,
   ...), since easydev used to bring ``colorama``, ``colorlog``, ``pexpect``,
   ``platformdirs`` and ``line_profiler`` transitively.
