from .{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "{{ cookiecutter.version }}"
{%- else %}

__version__ = "{{ cookiecutter.version }}"
{%- endif %}

__all__ = [
    "{{ cookiecutter.function_name }}",
]
