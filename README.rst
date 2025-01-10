easydev
##########

.. image:: https://badge.fury.io/py/easydev.svg
    :target: https://pypi.python.org/pypi/easydev

.. image:: https://github.com/cokelaer/easydev/actions/workflows/main.yml/badge.svg
    :target: https://github.com/cokelaer/easydev/actions/workflows/main.yml


.. image:: https://coveralls.io/repos/cokelaer/easydev/badge.svg?branch=main
   :target: https://coveralls.io/r/cokelaer/easydev?branch=main




:documentation: http://easydev-python.readthedocs.io/en/latest/
:contributions: Please join https://github.com/cokelaer/easydev
:source: Please use https://github.com/cokelaer/easydev
:issues: Please use https://github.com/cokelaer/easydev/issues
:Python version supported: 3.8, 3.9, 3.10, 3.11, 3.12


The  `easydev <http://pypi.python.org/pypi/easydev/>`_ package
provides miscellaneous functions that are repeatidly used during
the development of Python packages. The goal is to help developers on
speeding up their own dev. It has been used also as an incubator for other
packages (e.g., http://pypi.python.org/pypi/colormap) and is stable.

.. warning:: I'm not pretending to provide universal and bug-free tools. The
    tools provided may also change. However, **easydev** is used
    in a few other packages such as
    `bioservices <https://pypi.python.org/pypi/bioservices>`_,
    `sequana <https://sequana.readthedocs.io>`_ or
    `GDSCTools <https://sequana.readthedocs.io>`_ to give a few
    examples.



Changelog
~~~~~~~~~

========= ==========================================================================
Version   Description
========= ==========================================================================
0.13.3    * update pyproject with contribs from @s-t-e-v-e-n-k see PR37
0.13.2    * replace mock with unittest.mock (fixes
            https://github.com/cokelaer/easydev/issues/20)
0.13.1    * fix get_dependencies
0.13.0    * fix requirements (line_profiler) and CI
0.12.2    * For developers: move to pyprojet. add precomit
          * replace pkg_resources (deprecated) with importlib
          * replace appdirs with more generic platformdirs
========= ==========================================================================
