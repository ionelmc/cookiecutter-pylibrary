===============================
{{ cookiecutter.project_name }}
===============================

.. image:: http://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: http://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: http://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.png?style=flat
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. image:: http://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.png?style=flat
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.png?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master
    :alt: Code Quality Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}
    :alt: Documentation Status

{{ cookiecutter.project_short_description }}

* Free software: BSD license

Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

Documentation
=============

https://{{ cookiecutter.repo_name }}.readthedocs.org/

Development
===========

To run the all tests run::

    tox
