============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <https://github.com/ionelmc/cookiecutter-pylibrary/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

cookiecutter-pylibrary could always use more documentation, whether as part of the
official cookiecutter-pylibrary docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/ionelmc/cookiecutter-pylibrary/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

Development
===========

To set up `cookiecutter-pylibrary` for local development:

1. `Fork cookiecutter-pylibrary on GitHub <https://github.com/ionelmc/cookiecutter-pylibrary/fork>`_.
2. Clone your fork locally::

    git clone git@github.com:your_name_here/cookiecutter-pylibrary.git

3. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes, run all the checks, doc builder and spell checker with `tox <http://tox.readthedocs.org/en/latest/install.html>`_ one command::

    tox

5. Commit your changes and push your branch to GitHub::

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run ``tox``) [1]_.
2. Update documentation when there's new API, functionality etc. 
3. Add a note to ``CHANGELOG.rst`` about the changes.

.. [1] If you don't have all the necessary python versions available locally you can rely on Travis - it will 
       `run the tests <https://travis-ci.org/ionelmc/cookiecutter-pylibrary/pull_requests>`_ for each change you add in the pull request.
       
       It will be slower though ...
       
Tips
----

If you want to add a context option, you need to:

* Add the actual option in `cookiecutter.json <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/cookiecutter.json>`_
* Add it in the cookiecutter test builder suite:
 
  * Edit `setup.cfg <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/ci/setup.cfg>`_
  * Run ``./ci/bootstrap.py`` to regenerate the test ``.cookiecutterrc`` files.
* Change the `bare tox.ini <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/tox.ini>`_ to have an conditional for it.
* Change the `template tox.ini <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/ci/templates/tox.ini>`_
  (don't forget the raw sections) to have an conditional for it  (this ``tox.ini`` file is used with the ``test_matrix_configurator=yes`` option)

