========
Overview
========
{% if cookiecutter.repo_hosting != "no" %}
.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | {%- if cookiecutter.travis == 'yes' %} |travis|{% endif -%}
          {%- if cookiecutter.appveyor == 'yes' %} |appveyor|{% endif -%}
          {%- if cookiecutter.requiresio == 'yes' %} |requires|{% endif -%}
        {{ '' }}
        | {%- if cookiecutter.coveralls == 'yes' %} |coveralls|{% endif -%}
          {%- if cookiecutter.codecov == 'yes' %} |codecov|{% endif -%}
        {{ '' }}
        {%- if cookiecutter.landscape == 'yes' or cookiecutter.scrutinizer == 'yes' or cookiecutter.codacy == 'yes' or cookiecutter.codeclimate == 'yes' %}
        | {%- if cookiecutter.landscape == 'yes' %} |landscape|{% endif -%}
          {%- if cookiecutter.scrutinizer == 'yes' %} |scrutinizer|{% endif -%}
          {%- if cookiecutter.codacy == 'yes' %} |codacy|{% endif -%}
          {%- if cookiecutter.codeclimate == 'yes' %} |codeclimate|{% endif -%}
        {%- endif -%}
{{ '' }}
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
{%- if cookiecutter.repo_hosting == "github" %}
        | |commits-since|
{%- endif %}
{{ '' }}
{%- if cookiecutter.sphinx_docs == "yes" -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name|replace('.', '') }}
    :alt: Documentation Status
{% endif %}
{%- if cookiecutter.travis == 'yes' %}
.. |travis| image:: https://api.travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.appveyor == 'yes' %}
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.requiresio == 'yes' %}
.. |requires| image:: https://requires.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/requirements/?branch=master
{% endif %}
{%- if cookiecutter.coveralls == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.codecov == 'yes' %}
.. |codecov| image:: https://codecov.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.landscape == 'yes' %}
.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/master
    :alt: Code Quality Status
{% endif %}
{%- if cookiecutter.codacy == 'yes' %}
.. |codacy| image:: https://img.shields.io/codacy/grade/{{ cookiecutter.codacy_projectid }}.svg
    :target: https://www.codacy.com/app/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{% endif %}
{%- if cookiecutter.codeclimate == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter.upload_to_pypi.upload_immediately_and_link_to_pypi == "yes" %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{% if cookiecutter.repo_hosting == "github" %}
.. |commits-since| image:: https://img.shields.io/{{ cookiecutter.repo_hosting }}/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter.repo_hosting }}.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...master
{% endif %}
.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported versions
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{% endif %}
{% if cookiecutter.scrutinizer == 'yes' %}
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/
{% endif %}

.. end-badges
{% endif %}
{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter.license != "no" %}
* Free software: {{ cookiecutter.license }}
{% endif %}
Installation
============

{% if cookiecutter.upload_to_pypi.upload_immediately_and_link_to_pypi == "no" %}If {{ cookiecutter.distribution_name }} has been uploaded to a devpi instance your pip is connected to, then you can install with{% endif -%}
::

    pip install {{ cookiecutter.distribution_name }}

{% if 'git' in cookiecutter.repo_hosting -%}
You can always install the bleeding-edge updates with::

    pip install git+ssh://git@{{ cookiecutter.repo_hosting }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@master
{%- endif %}

Documentation
=============

{% if cookiecutter.sphinx_docs == "yes" %}
{{ cookiecutter.sphinx_docs_hosting }}
{% else %}
To use the project:

.. code-block:: python

    import {{ cookiecutter.package_name }}
    {{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_function }}()
{% endif %}

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
