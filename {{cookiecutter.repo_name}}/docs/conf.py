extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
master_doc = "index"
project = {{ cookiecutter.project_name|jsonquote }}
year = "{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}"
author = {{ cookiecutter.full_name|jsonquote }}
copyright = f"{year}, {author}"
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
try:
    from pkg_resources import get_distribution

    version = release = get_distribution("{{ cookiecutter.package_name }}").version
except Exception:
    import traceback

    traceback.print_exc()
    version = release = {{ cookiecutter.version|jsonquote }}
{%- else %}
version = release = {{ cookiecutter.version|jsonquote }}
{%- endif %}

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues/%s", "#%s"),
    "pr": ("https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/pull/%s", "PR #%s"),
}

html_theme = "{{ cookiecutter.sphinx_theme|replace('-', '_') }}"
html_theme_options = {
    "githuburl": "https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/",
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
