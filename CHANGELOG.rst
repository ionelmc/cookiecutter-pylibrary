Changelog
#########

Use cookiecutter's ``--checkout`` options to use a specific version.

v1.1 (2015-03-28)
-----------------

* Added support for `nose <http://nose.readthedocs.org/>`_ test runner. Contributed by Alexander Artemenko, `#8
  <https://github.com/ionelmc/cookiecutter-pylibrary/issues/8>`_ `#9
  <https://github.com/ionelmc/cookiecutter-pylibrary/pull/9>`_.
* Strip all text roles from ``long_description`` in ``setup.py``.
* Added contributing guide for the template.
* Improved the tests for the template (no more ``.cookiecutterrc`` overriding, other minor perm and path issues).
* The ``setup.py release`` doesn't upload anymore. Added instructions for using `twine
  <https://pypi.python.org/pypi/twine>`_.
* Minor glob simplification in ``MANIFEST.in``.

v1.0 (2015-03-24)
-----------------

* First tag.
