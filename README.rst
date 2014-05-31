======================
cookiecutter-pylibrary
======================

`Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template for a Python python library. This is largely designed
to address this `blog post about packaging python libraries <http://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

There's a bare library using this template (if you're curious about the final result): https://github.com/ionelmc/python-nameless.

Features
--------

* BSD 2-clause license.
* Tox_ for testing Python 2.6, 2.7, 3.3, PyPy etc. Support for creating a tests matrix out of dependencies and python versions.
* Travis-CI_ and Coveralls_ for continuous testing and coverage tracking (using Tox_).
* Documentation with Sphinx_, ready for ReadTheDocs_.

Requirements
------------

Projects using this template have these minimal dependencies:

* Tox_ - for running the tests
* Setuptools_ - for building the package, wheels etc. Now-days Setuptools is widely available, it shouldn't pose a
  problem :)

Usage
-----

This template is more involved than the regular `cookiecutter-pypackage
<https://github.com/audreyr/cookiecutter-pypackage>`_.

First generate your project::

    cookiecutter https://github.com/ionelmc/cookiecutter-pylibrary.git

..

    .. list-table:: The variables
        :stub-columns: 1

        * - project_name
          - Verbose project name, used in headings (docs, readme, etc)
        * - repo_name
          - Repository name on github
        * - package_name
          - Python package name (whatever you would import)
        * - distribution_name
          - PyPI distribution name (what you would ``pip install``)
        * - test_pythons
          - Space separated list of python versions to test. Changeable later in ``configure.py``.
        * - test_dependencies
          - Vertical bar (``|``) separated list of dependencies to test. Changeable later in ``configure.py``.

The testing (``tox.ini`` and ``.travis.yml``) configuration is generated from templates. For your convenience there's an
initial bootstrap ``tox.ini``, to get the initial generation going just run::

    tox

You can later regenerate ``tox.ini`` and ``.travis.yml`` by running::

    ./configure.py

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

    git init .
    git add .
    git commit -m "Initial skel."
    git remote add origin git@github.com:ionelmc/python-nameless.git
    git push -u origin master

Then:

* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package. This template comes with a tox environment that will:

  * Check if your ``README.rst`` is valid.
  * Check if the ``MANIFEST.in`` has any issues.
  * Run ``flake8`` (a combo of PEP8, pyflakes and McCabe checks)

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
