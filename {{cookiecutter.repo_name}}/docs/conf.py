# -*- coding: utf-8 -*-
from __future__ import unicode_literals

{% if cookiecutter.sphinx_theme == 'sphinx-rtd-theme' -%}
import os
{% endif -%}
{% if cookiecutter.setup_py_uses_setuptools_scm == 'yes' -%}
import traceback
{%- endif %}
{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' %}

import {{ cookiecutter.sphinx_theme|replace('-', '_') }}
{%- endif %}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = '{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}'
author = {{ '{0!r}'.format(cookiecutter.full_name) }}
copyright = '{0}, {1}'.format(year, author)
{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
try:
    from pkg_resources import get_distribution
    version = release = get_distribution('{{ cookiecutter.package_name }}').version
except Exception:
    traceback.print_exc()
    version = release = {{ '{0!r}'.format(cookiecutter.version) }}
{%- else %}
version = release = {{ '{0!r}'.format(cookiecutter.version) }}
{%- endif %}

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues/%s', '#'),
    'pr': ('https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/pull/%s', 'PR #'),
}

{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' %}
html_theme = "{{ cookiecutter.sphinx_theme|replace('-', '_') }}"
html_theme_path = [{{ cookiecutter.sphinx_theme|replace('-', '_') }}.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/'
}
{%- else %}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'
{%- endif %}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
