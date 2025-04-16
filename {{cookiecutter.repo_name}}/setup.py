#!/usr/bin/env python
{%- if cookiecutter.c_extension_support in ["yes", "cython", "cffi"] %}
import os
{%- if cookiecutter.c_extension_support == "yes" %}
import platform
{%- endif -%}
{%- endif -%}
{%- if cookiecutter.repo_hosting_domain == "no" %}
import os.path
{%- endif %}
import re
{%- if cookiecutter.c_extension_support == "cffi" %}
import sys
{%- endif %}
from pathlib import Path

{% if cookiecutter.c_extension_support not in ["no", "cffi"] -%}
from setuptools import Extension
{% endif -%}
from setuptools import find_namespace_packages
from setuptools import setup
{%- if cookiecutter.c_extension_support != "no" %}
{%- if cookiecutter.c_extension_optional == "yes" %}
from setuptools.command.build_ext import build_ext
{%- endif %}
from setuptools.dist import Distribution
{%- if cookiecutter.c_extension_support == "cython" %}

try:
    # Allow installing package without any Cython available. This
    # assumes you are going to include the .c files in your sdist.
    import Cython
except ImportError:
    Cython = None
{%- endif %}
{%- endif %}
{%- if cookiecutter.c_extension_support != "no" %}
{%- if cookiecutter.c_extension_support in ["yes", "cython"] %}

# Enable code coverage for C code: we cannot use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore, we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if "TOX_ENV_NAME" in os.environ and os.environ.get("SETUPPY_EXT_COVERAGE") == "yes"
{%- if cookiecutter.c_extension_support == "yes" %} and platform.system() == "Linux"{% endif %}:
{%- if cookiecutter.c_extension_support == "cython" %}
    CFLAGS = os.environ["CFLAGS"] = "-DCYTHON_TRACE=1"
    LFLAGS = os.environ["LFLAGS"] = ""
{%- elif cookiecutter.c_extension_support == "yes" %}
    CFLAGS = os.environ["CFLAGS"] = "-fprofile-arcs -ftest-coverage"
    LFLAGS = os.environ["LFLAGS"] = "-lgcov"
{%- endif %}
else:
    CFLAGS = ""
    LFLAGS = ""
{%- endif %}
{%- if cookiecutter.c_extension_optional == "yes" %}

allow_extensions = True
# Enable this if the extensions will not build on PyPy
# if '__pypy__' in sys.builtin_module_names:
#     print('NOTICE: C extensions disabled on PyPy (would be broken)!')
#     allow_extensions = False
if os.environ.get('SETUPPY_FORCE_PURE'):
    print('NOTICE: C extensions disabled (SETUPPY_FORCE_PURE)!')
    allow_extensions = False


class OptionalBuildExt(build_ext):
    """
    Allow the building of C extensions to fail.
    """

    def run(self):
        try:
            super().run()
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print("*" * 80)
        print(
            """WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
            """
        )

        print("CAUSE:")
        print("")
        print("    " + repr(e))
        print("*" * 80)
{%- endif %}


class BinaryDistribution(Distribution):
    """
    Distribution which almost always forces a binary package with platform name
    """

    def has_ext_modules(self):
        return super().has_ext_modules() or not os.environ.get("SETUPPY_ALLOW_PURE")

{%- endif %}


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


setup(
    name="{{ cookiecutter.distribution_name }}",
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": "src/{{ cookiecutter.package_name }}/_version.py",
        "fallback_version": "{{ cookiecutter.version }}",
    },
{%- else %}
    version="{{ cookiecutter.version }}",
{%- endif %}
{%- if cookiecutter.license != "no" %}
    license="{{ {
        "BSD 2-Clause License": "BSD-2-Clause",
        "BSD 3-Clause License": "BSD-3-Clause",
        "MIT license": "MIT",
        "ISC license": "ISC",
        "Apache Software License 2.0": "Apache-2.0",
        "GNU Lesser General Public License v3 or later (LGPLv3+)": "LGPL-3.0-or-later",
        "GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0-only",
        "GNU Lesser General Public License v2.1 or later (LGPLv2+)": "LGPL-2.1-or-later",
        "GNU Lesser General Public License v2.1 (LGPLv2)": "LGPL-2.1-only",
      }[cookiecutter.license]
    }}",
{%- endif %}
    description={{ cookiecutter.project_short_description|jsonquote }},
    long_description="{}\n{}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.rst")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    long_description_content_type='text/x-rst',
    author={{ cookiecutter.full_name|jsonquote }},
    author_email={{ cookiecutter.email|jsonquote }},
{%- if cookiecutter.repo_hosting_domain == "no" %}
    url="file://" + Path(__file__).parent),
{%- else %}
    url="https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}",
{%- endif %}
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=[path.stem for path in Path("src").glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
{%- if cookiecutter.pypi_disable_upload == "yes" %}
        "Private :: Do Not Upload",
{%- endif %}
    ],
{%- if cookiecutter.repo_hosting_domain != "no" %}
    project_urls={
{%- if cookiecutter.sphinx_docs == "yes" %}
        "Documentation": "{{ cookiecutter.sphinx_docs_hosting }}",
        "Changelog": "{{ cookiecutter.sphinx_docs_hosting }}en/latest/changelog.html",
{%- else %}
        "Changelog": "https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst",
{%- endif %}
        "Issue Tracker": "https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues",
    },
{%- endif %}
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    python_requires=">=3.9",
    install_requires=[
{%- if cookiecutter.command_line_interface == "click" %}
        "click",
{%- endif %}
{%- if cookiecutter.c_extension_support == "cffi" %}
        "cffi>=1.0.0",
{%- endif %}
        # eg: "aspectlib==1.1.1", "six>=1.7",
    ],
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=='3.8'": ["backports.zoneinfo"],
    },
{%- set setup_requires_interior %}
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
            "setuptools_scm>=3.3.1",
        {% endif %}
{%- endset %}
{%- if cookiecutter.c_extension_support == "cython" %}
    setup_requires=(
        [
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
            "setuptools_scm>=3.3.1",
{%- endif %}
            "cython",
        ]
        if Cython
        else [{% if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
            "setuptools_scm>=3.3.1",
        {% endif %}]
    ),
{%- elif cookiecutter.c_extension_support == "cffi" %}
    # We only require CFFI when compiling.
    # pyproject.toml does not support requirements only for some build actions,
    # but we can do it in setup.py.
    setup_requires=(
        [
{%- if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
            "setuptools_scm>=3.3.1",
{%- endif %}
            "cffi>=1.0.0",
        ]
        if any(arg.startswith(("build", "bdist")) for arg in sys.argv)
        else [{% if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
            "setuptools_scm>=3.3.1",
        {% endif %}]
    ),
    {%- elif setup_requires_interior.strip() %}
    setup_requires=[{% if cookiecutter.setup_py_uses_setuptools_scm == "yes" %}
        "setuptools_scm>=3.3.1",
    {% endif %}],
{%- endif -%}
{%- if cookiecutter.command_line_interface != "no" %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:run",
        ]
    },
{%- endif %}
{%- if cookiecutter.c_extension_support != "no" -%}
{%- if cookiecutter.c_extension_optional == "yes" %}
    cmdclass={"build_ext": OptionalBuildExt},
{%- endif %}
{%- if cookiecutter.c_extension_support == "cffi" %}
    cffi_modules=[f"{path}:ffi" for path in Path("src").glob("**/_*_build.py")],
{%- else %}
    ext_modules=[
        Extension(
            str(path.relative_to("src").with_suffix("")).replace(os.sep, "."),
            sources=[str(path)],
{%- if cookiecutter.c_extension_support in ["yes", "cython"] %}
            extra_compile_args=CFLAGS.split(),
            extra_link_args=LFLAGS.split(),
{%- endif %}
            include_dirs=[str(path.parent)],
        )
        for path in Path("src").glob(
{%- if cookiecutter.c_extension_support == "cython" %}"**/*.pyx" if Cython else "**/*.c"
{%- else %}"**/*.c"{% endif %})
    ]
    if allow_extensions
    else [],
    distclass=BinaryDistribution if allow_extensions else None,
{%- endif %}
{%- endif %}
)
