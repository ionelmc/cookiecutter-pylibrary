===============================
{{ cookiecutter.project_name }}
===============================


.. image:: http://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.png
    :alt: Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: http://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.png
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: http://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. image:: http://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

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
