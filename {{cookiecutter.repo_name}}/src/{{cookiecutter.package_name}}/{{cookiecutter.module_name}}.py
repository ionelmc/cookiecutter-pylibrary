{% if cookiecutter.c_extension_support == "cffi" -%}
from ._{{ cookiecutter.module_name }} import ffi as _ffi
from ._{{ cookiecutter.module_name }} import lib as _lib


def {{ cookiecutter.function_name }}(args):
    args = [_ffi.new("char[]", arg.encode()) for arg in args]
    result = _lib.{{ cookiecutter.function_name }}(len(args), _ffi.new("char *[]", args))
    if result == _ffi.NULL:
        return None
    else:
        return _ffi.string(result).decode()
{% elif cookiecutter.c_extension_support != "no" -%}
{% if cookiecutter.c_extension_optional == "yes" -%}
try:
    from ._{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}
except ImportError:

    def {{ cookiecutter.function_name }}(args):
        return max(args, key=len)
{% else -%}
from ._{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}

__all__ = [
    "{{ cookiecutter.function_name }}",
]
{% endif -%}
{% else -%}
def {{ cookiecutter.function_name }}(args):
    return max(args, key=len)
{% endif -%}
