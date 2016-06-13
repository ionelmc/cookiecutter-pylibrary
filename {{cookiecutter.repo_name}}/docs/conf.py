# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


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
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = {{ '{0!r}'.format('<YEAR>' if cookiecutter.year == 'now' else cookiecutter.year) }}
author = {{ '{0!r}'.format(cookiecutter.full_name) }}
copyright = '{0}, {1}'.format(year, author)
version = release = {{ '{0!r}'.format(cookiecutter.version) }}

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues/%s', '#'),
    'pr': ('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pull/%s', 'PR #'),
}

{%- if cookiecutter.sphinx_theme|lower != 'sphinx-rtd-theme' %}
import {{ cookiecutter.sphinx_theme|replace('-', '_') }}
html_theme = "{{ cookiecutter.sphinx_theme|replace('-', '_') }}"
html_theme_path = [{{ cookiecutter.sphinx_theme|replace('-', '_') }}.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/'
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
