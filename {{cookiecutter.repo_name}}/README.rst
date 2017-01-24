========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | {%- if cookiecutter.travis|lower == 'yes' %} |travis|{% endif -%}
          {%- if cookiecutter.appveyor|lower == 'yes' %} |appveyor|{% endif -%}
          {%- if cookiecutter.requiresio|lower == 'yes' %} |requires|{% endif -%}
        {{ '' }}
        | {%- if cookiecutter.coveralls|lower == 'yes' %} |coveralls|{% endif -%}
          {%- if cookiecutter.codecov|lower == 'yes' %} |codecov|{% endif -%}
        {{ '' }}
        {%- if cookiecutter.landscape|lower == 'yes' or cookiecutter.scrutinizer|lower == 'yes' or cookiecutter.codacy|lower == 'yes' or cookiecutter.codeclimate|lower == 'yes' %}
        | {%- if cookiecutter.landscape|lower == 'yes' %} |landscape|{% endif -%}
          {%- if cookiecutter.scrutinizer|lower == 'yes' %} |scrutinizer|{% endif -%}
          {%- if cookiecutter.codacy|lower == 'yes' %} |codacy|{% endif -%}
          {%- if cookiecutter.codeclimate|lower == 'yes' %} |codeclimate|{% endif -%}
        {%- endif -%}
{{ '' }}
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name|replace('.', '') }}
    :alt: Documentation Status
{{ '' }}
{%- if cookiecutter.travis|lower == 'yes' %}
.. |travis| image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.appveyor|lower == 'yes' %}
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.requiresio|lower == 'yes' %}
.. |requires| image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements/?branch=master
{% endif %}
{%- if cookiecutter.coveralls|lower == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.codecov|lower == 'yes' %}
.. |codecov| image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.landscape|lower == 'yes' %}
.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master
    :alt: Code Quality Status
{% endif %}
{%- if cookiecutter.codacy|lower == 'yes' %}
.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{% endif %}
{%- if cookiecutter.codeclimate|lower == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{% endif %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...master

.. |downloads| image:: https://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}
{% if cookiecutter.scrutinizer|lower == 'yes' %}
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
{% endif %}

.. end-badges

{{ cookiecutter.project_short_description|wordwrap(119) }}

* Free software: BSD license

Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

Documentation
=============

https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
