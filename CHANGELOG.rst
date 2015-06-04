Changelog
#########

Use cookiecutter's ``--checkout`` options to use a specific version.

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
