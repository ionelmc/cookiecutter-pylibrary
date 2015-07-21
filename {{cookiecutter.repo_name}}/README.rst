{{ "=" * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|length }}

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | {%- if cookiecutter.coveralls|lower == 'yes' %} |coveralls|{% endif -%}
          {%- if cookiecutter.codecov|lower == 'yes' %} |codecov|{% endif -%}
          {%- if cookiecutter.landscape|lower == 'yes' %} |landscape|{% endif -%}
          {%- if cookiecutter.scrutinizer|lower == 'yes' %} |scrutinizer|{% endif -%}
          {%- if cookiecutter.codacy|lower == 'yes' %} |codacy|{% endif -%}
          {%- if cookiecutter.codeclimate|lower == 'yes' %} |codeclimate|{% endif -%}
{{ '' }}
    * - package
      - |version| |downloads|

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. |appveyor| image:: https://img.shields.io/appveyor/ci/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat&label=AppVeyor
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% if cookiecutter.coveralls|lower == 'yes' %}
.. |coveralls| image:: http://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat&label=Coveralls
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{% if cookiecutter.codecov|lower == 'yes' %}
.. |codecov| image:: http://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat&label=Codecov
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{% if cookiecutter.landscape|lower == 'yes' %}
.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master
    :alt: Code Quality Status
{% endif %}
{% if cookiecutter.codacy|lower == 'yes' %}
.. |codacy| image:: https://www.codacy.com/project/badge/REPLACE_WITH_PROJECT_ID
    :target: https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{% endif %}
{% if cookiecutter.codeclimate|lower == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/repos/REPLACE_WITH_PROJECT_ID/gpa.svg
   :target: https://codeclimate.com/repos/REPLACE_WITH_PROJECT_ID/feed
   :alt: CodeClimate Quality Status
{% endif %}
.. |version| image:: http://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}

.. |downloads| image:: http://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}
{% if cookiecutter.scrutinizer|lower == 'yes' %}
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
{% endif %}
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
