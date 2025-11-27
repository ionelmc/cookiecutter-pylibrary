========
Overview
========
{% if cookiecutter.repo_hosting_domain == "github.com" %}

.. list-table::
    :stub-columns: 1
{% if cookiecutter.sphinx_docs == "yes" %}
    * - docs
      - |docs|
{%- endif %}
    * - tests
      - {%- if cookiecutter.github_actions == 'yes' %} |github-actions|{% endif -%}
        {%- if cookiecutter.coveralls == 'yes' %} |coveralls|{% endif -%}
        {%- if cookiecutter.codecov == 'yes' %} |codecov|{% endif -%}
        {%- if cookiecutter.scrutinizer == 'yes' %} |scrutinizer|{% endif -%}
        {%- if cookiecutter.codacy == 'yes' %} |codacy|{% endif -%}
        {%- if cookiecutter.codeclimate == 'yes' %} |codeclimate|{% endif -%}
{%- if cookiecutter.pypi_badge == "yes" or cookiecutter.repo_hosting_domain == "github.com" %}
    * - package
      - {%- if cookiecutter.pypi_badge == "yes" %} |version| |wheel| |supported-versions| |supported-implementations|{% endif %}
        {%- if cookiecutter.repo_hosting_domain == "github.com" %} |commits-since|{% endif %}
{%- endif %}
{%- if cookiecutter.sphinx_docs == "yes" %}
{%- if 'readthedocs' in cookiecutter.sphinx_docs_hosting %}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name|replace('.', '') }}/
    :alt: Documentation Status
{%- elif 'gitlab' in cookiecutter.sphinx_docs_hosting and 'gitlab' in cookiecutter.repo_hosting_domain %}
.. |docs| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/{{ cookiecutter.repo_main_branch }}/pipeline.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name|replace('.', '') }}/commits/{{ cookiecutter.repo_main_branch }}
    :alt: Documentation Status
{%- endif %}
{%- endif %}
{%- if cookiecutter.github_actions == 'yes' %}
.. |github-actions| image:: https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions
{%- endif %}
{%- if cookiecutter.coveralls == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch={{ cookiecutter.repo_main_branch }}
    :alt: Coverage Status
    :target: https://coveralls.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}?branch={{ cookiecutter.repo_main_branch }}
{%- endif %}
{%- if cookiecutter.codecov == 'yes' %}
.. |codecov| image:: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/branch/{{ cookiecutter.repo_main_branch }}/graphs/badge.svg?branch={{ cookiecutter.repo_main_branch }}
    :alt: Coverage Status
    :target: https://app.codecov.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{%- endif %}
{%- if cookiecutter.codacy == 'yes' %}
.. |codacy| image:: https://img.shields.io/codacy/grade/{{ cookiecutter.codacy_projectid }}.svg
    :target: https://www.codacy.com/app/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{%- endif %}
{%- if cookiecutter.codeclimate == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{%- endif %}
{%- if cookiecutter.pypi_badge == "yes" %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported versions
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{%- endif %}
{%- if cookiecutter.repo_hosting_domain == "github.com" %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...{{ cookiecutter.repo_main_branch }}
{%- endif %}
{%- if cookiecutter.scrutinizer == 'yes' %}
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_main_branch }}.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/
{%- endif %}

{% endif %}
{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter.license != "no" %}
* Free software: {{ cookiecutter.license }}
{% endif %}
Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter.repo_main_branch }}
{%- endif %}

Documentation
=============

{% if cookiecutter.sphinx_docs == "yes" %}
{{ cookiecutter.sphinx_docs_hosting }}
{% else %}
To use the project:
{% if cookiecutter.command_line_interface != "no" %}
.. code-block:: python

    import {{ cookiecutter.package_name }}
    {{ cookiecutter.package_name }}.{{ cookiecutter.function_name }}(...)
{% else %}
.. code-block:: bash

    $ {{ cookiecutter.command_line_interface_bin_name }} ...
{% endif %}
{% endif %}

Development
===========

To run all the tests run::

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
