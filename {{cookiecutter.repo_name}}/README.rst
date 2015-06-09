===============================
{{ cookiecutter.project_name }}
===============================

| |docs| |travis| |appveyor|
|
{%- if cookiecutter.coveralls|lower == 'yes' %} |coveralls|{% endif -%}
{%- if cookiecutter.codecov|lower == 'yes' %} |codecov|{% endif -%}
{%- if cookiecutter.landscape|lower == 'yes' %} |landscape|{% endif -%}
{%- if cookiecutter.scrutinizer|lower == 'yes' %} |scrutinizer|{% endif -%}
{{ '' }}
| |version| |downloads|

..
    |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. |appveyor| image:: https://img.shields.io/appveyor/ci/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. |coveralls| image:: http://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. |codecov| image:: http://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |downloads| image:: http://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |wheel| image:: https://pypip.in/wheel/{{ cookiecutter.distribution_name }}/badge.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://pypip.in/py_versions/{{ cookiecutter.distribution_name }}/badge.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://pypip.in/implementation/{{ cookiecutter.distribution_name }}/badge.svg?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/

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
