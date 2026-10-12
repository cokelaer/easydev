# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`easydev` is a flat collection of independent utility modules for Python package development (parameter validation, logging, progress bar, config files, multiprocessing, shell helpers, Sphinx theme/extension, etc.). Used downstream by bioservices, sequana, GDSCTools, so public API names are stable; avoid breaking renames. CI covers Python 3.9–3.14.

## Commands

```bash
poetry install --with dev                      # dev setup
poetry run pytest --cov-report term --cov=easydev   # what CI runs
pytest test/test_tools.py::test_name -xvs      # single test
pytest -m "not network"                        # skip tests needing network (marker in test/pytest.ini)
pre-commit run --all-files                     # black (120), isort (black profile), flake8
poetry build                                   # wheel + sdist
cd doc && make html                            # Sphinx docs (doc/source, ChangeLog in doc/ChangeLog.txt)
```

## Architecture

- `easydev/` is a single package of mostly self-contained modules; `easydev/__init__.py` imports each submodule and re-exports their public names at top level (`from easydev import X`), mostly via `from .module import *` (so `__all__` in each module controls what is exported; `md5`, `browse` as `onweb`, and `get_dependencies` are imported explicitly). When adding a function/class to a module, check whether `__init__.py` needs to expose it.
- `easydev/share/` ships non-Python assets (`copybutton.js`, Sphinx `themes/`) used by `sphinx_themes.py` and `copybutton.py`; they are included via `packages` in `pyproject.toml`/`MANIFEST.in`.
- `appdirs.py` is a thin `AppDirs` wrapper over `platformdirs` (not a vendored copy); `config_tools.py` imports it for user config dirs and provides INI-style config (`CustomConfig`, `DynamicConfigParser`).
- Tests live in `test/` (one `test_<module>.py` per module) with shared `conftest.py` and `test/data/`.
- Version is set in `pyproject.toml`; `easydev.version` reads it via `importlib.metadata` (needs installed package).
