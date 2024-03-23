from pathlib import Path

from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    char* {{ cookiecutter.function_name }}(int argv, char *argv[]);
    """
)


ffi.set_source(
    "{{ cookiecutter.package_name }}._{{ cookiecutter.module_name }}",
    Path(__file__).parent.joinpath("_{{ cookiecutter.module_name }}.c").read_text(),
)

if __name__ == "__main__":
    ffi.compile()
