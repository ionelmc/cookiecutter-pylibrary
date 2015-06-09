======================
cookiecutter-pylibrary
======================

Cookiecutter_ template for a Python python library. |travis| |appveyor|

.. |travis| image:: http://img.shields.io/travis/ionelmc/cookiecutter-pylibrary/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/cookiecutter-pylibrary

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/cookiecutter-pylibrary?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/cookiecutter-pylibrary

*Notes*:

* This is largely designed to address this `blog post about packaging python
  libraries <http://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

  * ... and it will save you from `packaging pitfalls
    <http://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/>`_.
* There's a bare library using this template (if you're curious about the final
  result): https://github.com/ionelmc/python-nameless.

Features
--------

This is an "all inclusive" sort of template.

* BSD 2-clause license.
* Tox_ for managing test environments for Python 2.6, 2.7, 3.3, PyPy etc.
* Pytest_ or Nose_ for testing Python 2.6, 2.7, 3.3, PyPy etc.
* *Optional* support for creating a tests matrix out of dependencies and python versions.
* Travis-CI_ and AppVeyor_ for continuous testing.
* Coveralls_ or Codecov_ for coverage tracking (using Tox_).
* Documentation with Sphinx_, ready for ReadTheDocs_.
* Configurations for:

  * isort_
  * bumpversion_

* Support for C extensions (including coverage measurement for the C code).
* Packaging and code quality checks. This template comes with a tox environment (``check``) that will:

  * Check if your ``README.rst`` is valid.
  * Check if the ``MANIFEST.in`` has any issues.
  * Run ``flake8`` (a combo of PEP8, pyflakes and McCabe checks)

Requirements
------------

Projects using this template have these minimal dependencies:

* Cookiecutter_ - just for creating the project
* Tox_ - for running the tests
* Setuptools_ - for building the package, wheels etc. Now-days Setuptools is widely available, it shouldn't pose a
  problem :)

To get quickly started on a new system, just `install setuptools
<https://pypi.python.org/pypi/setuptools#installation-instructions>`_ and then `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required install Tox_ and Cookiecutter_. To install
them, just run this in your shell or command prompt::

  pip install tox cookiecutter

Usage
-----

This template is more involved than the regular `cookiecutter-pypackage
<https://github.com/audreyr/cookiecutter-pypackage>`_.

First generate your project::

  cookiecutter gh:ionelmc/cookiecutter-pylibrary

You will be asked for these fields:

.. list-table::
    :header-rows: 1

    * - Template variable
      - Default
      - Description
    * - ``project_name``
      - .. code:: python

            "Nameless"
      - Verbose project name, used in headings (docs, readme, etc).
    * - ``repo_name``
      - .. code:: python

            "python-nameless"
      - Repository name on github.
    * - ``package_name``
      - .. code:: python

            "nameless"
      - Python package name (whatever you would import).
    * - ``distribution_name``
      - .. code:: python

            "nameless"
      - PyPI distribution name (what you would ``pip install``).
    * - ``c_extension_support``
      - .. code:: python

            "no"
      - Support C extensions (will slighly change the outputted ``setup.py``)
    * - ``c_extension_optional``
      - .. code:: python

            "no"
      - Make C extensions optional (will allow your package to install even if extensions can't be compiled)
    * - ``test_matrix_configurator``
      - .. code:: python

            "no"
      - Enable the test matrix generator script. If you don't have a huge number of test environments then probably you
        don't need this.
    * - ``test_runner``
      - .. code:: python

            "pytest"
      - Test runner to use. Available options: ``pytest`` or ``nose``.
    * - ``command_line_interface``
      - .. code:: python

            "plain"
      - Option to enable a CLI (a bin/executable file). Available options:

        * ``plain`` - a very simple command.
        * ``click`` - a command implemented with `click <http://click.pocoo.org/>`_ - which you can use to build more complex commands.
        * ``no`` - no CLI at all.

    * - ``cookiecutter.coveralls``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Coveralls_ and add badge in ``README.rst``.

    * - ``cookiecutter.codecov``
      - .. code:: python

            "no"
      - Enable pushing coverage data to Codecov_ and add badge in ``README.rst``.

        **Note:** Doesn't support pushing C extension coverage yet.

    * - ``cookiecutter.landscape``
      - .. code:: python

            "no"
      - Add a Landscape_ badge in ``README.rst``.

    * - ``cookiecutter.scrutinizer``
      - .. code:: python

            "no"
      - Add a Scrutinizer_ badge in ``README.rst``.

    * - ``rtd_theme``
      - .. code:: python

            "no"
      - Whether to use the Read The Docs theme when building docs locally.

The testing (``tox.ini`` and ``.travis.yml``) configuration is generated from templates. For your convenience there's an
initial bootstrap ``tox.ini``, to get the initial generation going just run::

  tox

You can later regenerate ``tox.ini`` and ``.travis.yml`` by running (if you enabled the ``test_matrix_configurator``
option)::

  tox -e configure

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

  git init .
  git add .
  git commit -m "Initial skel."
  git remote add origin git@github.com:ionelmc/python-nameless.git
  git push -u origin master

Then:

* `Enable the repository in your Travis CI account <https://travis-ci.org/profile>`_.
* `Enable the repository in your Coveralls account <https://coveralls.io/repos/new>`_.
* `Add the repo to your ReadTheDocs account <https://readthedocs.org/dashboard/import/>`_ + turn on the ReadTheDocs
  service hook. Don't forget to enable virtualenv and specify ``docs/requirements.txt`` as the requirements file in
  `Advanced Settings`.

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To see all the tox environments::

  tox -l

To only build the docs::

  tox -e docs

To build and verify that the built package is proper and other code QA checks::

  tox -e check

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the tox environments passing.

Version management
''''''''''''''''''

This template provides a basic bumpversion_ configuration. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

Building and uploading
''''''''''''''''''''''

To make a release of the project on PyPI, the most simple usage is::

  python setup.py release
  twine upload dist/*

Explanations:

* ``release`` is aliased to ``register clean sdist bdist_wheel``, see ``setup.cfg``.
* `twine <https://pypi.python.org/pypi/twine>`_ is a tool that you can use to securely upload your releases to PyPI.

Changelog
---------

See `CHANGELOG.rst <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/CHANGELOG.rst>`_.

Questions & answers
-------------------

There's no Makefile?

  Sorry, no ``Makefile`` yet. The Tox_ environments stand for whatever you'd have in a ``Makefile``.

Why does ``tox.ini`` have a ``passenv = *``?

  Tox 2.0 changes the way it runs subprocesses - it no longer passes all the environment variables by default. This causes
  all sorts of problems if you want to run/use any of these with Tox: SSH Agents, Browsers (for Selenium), Appengine SDK,
  VC Compiler and so on.

  `cookiecutter-pylibrary` errs on the side of convenience here. You can always remove ``passenv = *`` if you like
  the strictness.

Why is the version stored in several files (``pkg/__init__.py``, ``setup.py``, ``docs/conf.py``)?

  We cannot use a metadata/version file [#]_ because this template is to be used with both distributions of packages (dirs
  with ``__init__.py``) and modules (simple ``.py`` files that go straigh in ``site-packages``). There's no good place
  for that extra file if you're distributing modules.

  But this isn't so bad - `bumpversion <https://pypi.python.org/pypi/bumpversion>`_ manages the version string quite
  neatly.

.. [#] Example, an ``__about__.py`` file.

Not Exactly What You Want?
--------------------------

No way, this is the best. :stuck_out_tongue_winking_eye:


If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Coveralls: https://coveralls.io/
.. _ReadTheDocs: https://readthedocs.org/
.. _Setuptools: https://pypi.python.org/pypi/setuptools
.. _Pytest: http://pytest.org/
.. _AppVeyor: http://www.appveyor.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Nose: http://nose.readthedocs.org/
.. _isort: https://pypi.python.org/pypi/isort
.. _bumpversion: https://pypi.python.org/pypi/bumpversion
.. _Codecov: http://codecov.io/
.. _Landscape: https://landscape.io/
.. _Scrutinizer: https://scrutinizer-ci.com/
