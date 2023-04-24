from pathlib import Path

from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    char* {{ cookiecutter.c_extension_function }}(int argv, char *argv[]);
    """
)


ffi.set_source(
    "{{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_module }}",
    Path(__file__).parent.joinpath("{{ cookiecutter.c_extension_module }}.c").read_text(),
)

if __name__ == "__main__":
    ffi.compile()
