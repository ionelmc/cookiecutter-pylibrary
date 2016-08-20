Changelog
#########

Use cookiecutter's ``--checkout`` options to use a specific version.

v1.12 (2016-08-20)
------------------

* Removed all references to Python 2.6 from various config files. Contributed by Lucas Wiman,
  `#48 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/48>`_.
* Rename ``bin_name`` to ``command_line_interface_bin_name`` for more clarity.
* Added ``test_matrix_separate_coverage`` option with default to ``"no"``. Previously the template generated two environment
  flavors in ``tox.ini``: ``cover`` and ``nocov`` (what ``test_matrix_separate_coverage == "yes"`` would generate now).
* Added ``sphinx_doctest`` option to complement the lack of doctest support when ``test_matrix_separate_coverage == "no"`` is
  used.
* Added ``isort`` checks in ``tox.ini``. Contributed by Fábio C. Barrionuevo da Luz in `#50
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/50>`_.
* Removed ``"extension-coveralls"`` if it's not used. Contributed by Fábio C. Barrionuevo da Luz in `#49
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/49>`_.
* Fixed issues when running ``ci/bootstrap.py`` on Python 3.
* Fixed issues with Sphinx configuration so it works properly with Sphinx 1.4. Contributed by Sean Fisk in `#55
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/55>`_.
* Changed default options to use templating and reuse the `project_name`. Contributed by Christoph Sarnowski in `#56
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/56>`_.
* Extended default coverage reporting to include tests.
* Fixed trailing newline. Contributed in `#67 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/67>`_.
* Fixed missing ``console_scripts`` entrypoint and improve nose configuration. Contributed by Laurent Laporte in `#64
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/64>`_.
* Improved code style in a bunch of files. Contributed by Laurent Laporte in `#62
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/62>`_.
* Fixed coverage combining in coveralls/codecov tox envs. Now append mode is used, to avoid discarding coverage data.


v1.11 (2016-01-05)
------------------

* Added ``.editorconfig``.
* Changed Travis config: pip's cache is saved, libsegfault.so now works on all signals (like ABRT) and pytest-travis-fold
  is included by default.
* Use the builtin ``napoleon`` extension in Sphinx 1.3. Contributed by Christer van der Meeren, `#37
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/37>`_.
* Enable the ``extlinks`` extension from Sphinx.
* Added ``bin_name`` options and warnings when ``bin_name`` could be problematic (eg: it has ``.py`` extension and same name
  as the ``package_name``).
* Added Python 3.5 to classifiers (``setup.py``).
* Renamed the tox environment names to be more similar with the tox defaults (if ``test_matrix_generator`` is ``"no"``).
* Added few comments and tweaks in ``setup.py`` to make it easy to switch to Cython extensions.
* Various other small fixups.

v1.10 (2015-09-27)
------------------

* Added support for Python 3.5 in AppVeyor conf.
* Various small fixes and improvements to the CI and testing configuration.
* Switched some badges to not use shields.io (it has bad uptime).
* Added codecov support in Appveyor configuration.
* Made appveyor, travis and requires.io optional.

v1.9 (2015-08-06)
-----------------

* Changed badge images to be served over https.
* Fix wrong path and missing passenv in the tox.ini template. Closed `#24 <https://github.com/ionelmc/cookiecutter-pylibrary/issues/24>`_.
* Excluded *.dylib in ``MANIFEST.in``.
* Replaced dashes with underscores in package name. Closed `#23 <https://github.com/ionelmc/cookiecutter-pylibrary/issues/23>`_.
* Added Codeclimate and Codacy badge placeholders. Contributed by kaidokert, `#22 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/22>`_.
* Minor cleanup in ``tox.ini``.
* Fixed long heading underlines in generated RST documents.
* Changed tox configuration to use ``skip_install`` instead of ``usedevelop`` for envs that don't need to import anything.
* Fixed missing interpreter for the spell env.
* Moved bumpversion configuration out of ``setup.cfg``. Unfortunately bumpversion removes comments from the
  config file, so ``setup.cfg`` is not a good place.
* Simplified coverage configuration a bit.

v1.8.1 (2015-07-04)
-------------------

* Change the basic ``tox.ini`` to allow overriding the interpreter (so that 64bit interpreter
  actually gets used on AppVeyor).

v1.8 (2015-07-03)
-----------------

* Remove the 64bit environment from the basic AppVeyor test matrix.
* Change the ``tox.ini`` template (``test_matrix_configurator=yes``) to allow overriding the
  interpreter (so that 64bit interpreter actually gets used on AppVeyor).

v1.7.1 (2015-07-03)
-------------------

* Re-fixed wrong check for ``command_line_interface`` option in the template for ``setup.py``.

v1.7 (2015-06-30)
-----------------

* Fixed wrong check for ``command_line_interface`` option in the template for ``setup.py``.

v1.6 (2015-06-28)
-----------------

* Fix wrong ``.cookiecutterrc`` output.

v1.5 (2015-06-18)
-----------------

* Added support for Codecov. Codecov badge is active by default.
* Made support and badges for landscape, scrutinizer, coveralls and codecov switchable at project creation time.
* Disabled all the pypip.in badges (server has way too much downtime).
* Fixed a whitespace issue in outputed ``tox.ini``.
* Added option to use any Sphinx theme. Default changed to ``readthedocs`` theme. Contributed by Christer van der Meeren, `#20 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/20>`_.
* Added a ``.cookiecutterrc`` file to help with regenerating projects.
* Prettied up the badges (SVG badges, better grouping).
* Corrected the use of the deprecated 'files' option anymore in bumpversion configuration.
* Changed the sample console script to use the distribution name instead of the package name for the bin name.
* Changed coverage measurements to use pytest-cover instead of pytest-cov (which has several issues now).

v1.4 (2015-06-05)
-----------------

* Add ``passenv = *`` in the resulting ``tox.ini``. Fixes various inconveniences caused by the restricted
  subprocess environments in `tox-2.0`. Contributed by Christer van der Meeren, `#11 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/11>`_.

v1.3 (2015-05-06)
-----------------

* Cleanup and extend ``.gitignore`` a bit. Contributed by Ludovic Gasc, `#10 <https://github.com/ionelmc/cookiecutter-pylibrary/pull/10>`_.

v1.2 (2015-04-11)
-----------------

* Changed the string repr routine for name/description/email to dump unicode literals instead of utf8 encoded bytestrings.

  If you run cookiecutter on Python 2 you'll get unicode escapes ("\uXXXX") and on Python 3 you'll get the pretty gliphs.
* Fixed the ``bootstrap.py`` script (that's used for the ``test_matrix_configurator`` mode) to work from any current working directory.
* Included the branch name in the AppVeyor build number.
* Make the CLI optional and add support for using `click`.

v1.1 (2015-03-28)
-----------------

* Added support for `nose <http://nose.readthedocs.org/>`_ test runner. Contributed by Alexander Artemenko, `#8
  <https://github.com/ionelmc/cookiecutter-pylibrary/issues/8>`_ `#9
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/9>`_.
* Strip all text roles from ``long_description`` in ``setup.py``.
* Added contributing guide for the template.
* Improved the tests for the template (minor perm and path issues).
* The ``setup.py release`` doesn't upload anymore. Added instructions for using `twine
  <https://pypi.python.org/pypi/twine>`_.
* Minor glob simplification in ``MANIFEST.in``.

v1.0 (2015-03-24)
-----------------

* First tag.
