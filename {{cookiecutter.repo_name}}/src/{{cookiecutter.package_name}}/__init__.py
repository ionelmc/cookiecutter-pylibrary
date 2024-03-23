__version__ = "{{ cookiecutter.version }}"

from .{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}

__all__ = [
    "{{ cookiecutter.function_name }}",
]
