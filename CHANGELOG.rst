Changelog
#########

Use cookiecutter's ``--checkout`` options to use a specific version.

v1.2 (2015-04-10)
-----------------

* Changed the string repr routine for name/description/email to dump unicode literals instead of utf8 encoded bytestrings.

  If you run cookiecutter on Python 2 you'll get unicode escapes ("\uXXXX") and on Python 3 you'll get the pretty gliphs.
* Fixed the ``bootstrap.py`` script (that's used for the ``test_matrix_configurator`` mode) to work from any current working directory.
* Included the branch name in the AppVeyor build number.

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
