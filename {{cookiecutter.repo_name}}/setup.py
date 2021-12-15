#!/usr/bin/env python
# -*- encoding: utf-8 -*-
{%- if cookiecutter.legacy_python == "yes" %}
from __future__ import absolute_import
from __future__ import print_function
{%- endif %}

import io
{%- if cookiecutter.c_extension_support in ['yes', 'cython'] %}
import os
{%- if cookiecutter.c_extension_support == 'yes' %}
import platform
{%- endif -%}
{%- endif -%}
{%- if cookiecutter.repo_hosting_domain == "no" %}
import os.path
{%- endif %}
import re
{%- if cookiecutter.c_extension_support == 'cffi' %}
import sys
{%- endif %}
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
{%- if cookiecutter.c_extension_support not in ['no', 'cffi'] %}
from os.path import relpath
{%- endif %}
from os.path import splitext

{% if cookiecutter.c_extension_support not in ['no', 'cffi'] -%}
from setuptools import Extension
{% endif -%}
from setuptools import find_packages
from setuptools import setup
{%- if cookiecutter.c_extension_support != 'no' %}
{%- if cookiecutter.c_extension_optional == 'yes' %}
from setuptools.command.build_ext import build_ext
{%- endif %}
from setuptools.dist import Distribution
{%- if cookiecutter.c_extension_support == 'cython' %}

try:
    # Allow installing package without any Cython available. This
    # assumes you are going to include the .c files in your sdist.
    import Cython
except ImportError:
    Cython = None
{%- endif %}
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}
{%- if cookiecutter.c_extension_support in ['yes', 'cython'] %}

# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOX_ENV_NAME' in os.environ and os.environ.get('SETUPPY_EXT_COVERAGE') == 'yes'
{%- if cookiecutter.c_extension_support == 'yes' %} and platform.system() == 'Linux'{% endif %}:
{%- if cookiecutter.c_extension_support == 'cython' %}
    CFLAGS = os.environ['CFLAGS'] = '-DCYTHON_TRACE=1'
    LFLAGS = os.environ['LFLAGS'] = ''
{%- elif cookiecutter.c_extension_support == 'yes' %}
    CFLAGS = os.environ['CFLAGS'] = '-fprofile-arcs -ftest-coverage'
    LFLAGS = os.environ['LFLAGS'] = '-lgcov'
{%- endif %}
else:
    CFLAGS = ''
    LFLAGS = ''
{%- endif %}
{%- if cookiecutter.c_extension_optional == 'yes' %}


class OptionalBuildExt(build_ext):
    """Allow the building of C extensions to fail."""
    def run(self):
        try:
            if os.environ.get('SETUPPY_FORCE_PURE'):
                raise Exception('C extensions disabled (SETUPPY_FORCE_PURE)!')
            {% if cookiecutter.legacy_python == "yes" %}build_ext.run(self){% else %}super().build_ext(){% endif %}
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print('*' * 80)
        print('''WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
        ''')

        print('CAUSE:')
        print('')
        print('    ' + repr(e))
        print('*' * 80)
{%- endif %}


class BinaryDistribution(Distribution):
    """Distribution which almost always forces a binary package with platform name"""
    def has_ext_modules(self):
        return super({% if cookiecutter.legacy_python == "yes" %}BinaryDistribution, self{% endif %}).has_ext_modules() or not os.environ.get('SETUPPY_ALLOW_PURE')

{%- endif %}


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='{{ cookiecutter.distribution_name }}',
{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/{{ cookiecutter.package_name }}/_version.py',
        'fallback_version': '{{ cookiecutter.version }}',
    },
{%- else %}
    version='{{ cookiecutter.version }}',
{%- endif %}
{%- if cookiecutter.license != "no" %}
    license='{{ {
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
    }}',
{%- endif %}
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
{%- if cookiecutter.repo_hosting_domain == "no" %}
    url='file://' + os.path.abspath(dirname(__file__)),
{%- else %}
    url='https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}',
{%- endif %}
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
{%- if cookiecutter.license == "no" %}
{%- elif cookiecutter.license in ["BSD 2-Clause License", "BSD 3-Clause License"] %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == "MIT license" %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == "ISC license" %}
        'License :: OSI Approved :: ISC License (ISCL)',
{%- elif cookiecutter.license == "Apache Software License 2.0" %}
        'License :: OSI Approved :: Apache Software License',
{%- elif 'LGPLv3+' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
{%- elif 'LGPLv3' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
{%- elif 'LGPLv2' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)'
{%- elif 'LGPLv2' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)'
{%- endif %}
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
{%- if cookiecutter.legacy_python == "yes" %}
        'Programming Language :: Python :: 2.7',
{%- endif %}
        'Programming Language :: Python :: 3',
{%- if cookiecutter.legacy_python == "no" %}
        'Programming Language :: Python :: 3 :: Only',
{%- endif %}
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
{%- if cookiecutter.pypi_disable_upload == "yes" %}
        'Private :: Do Not Upload',
{%- endif %}
    ],
{%- if cookiecutter.repo_hosting_domain != "no" %}
    project_urls={
{%- if cookiecutter.sphinx_docs == "yes" %}
        'Documentation': '{{ cookiecutter.sphinx_docs_hosting }}',
        'Changelog': '{{ cookiecutter.sphinx_docs_hosting }}en/latest/changelog.html',
{%- else %}
        'Changelog': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst',
{%- endif %}
        'Issue Tracker': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues',
    },
{%- endif %}
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
{%- if cookiecutter.legacy_python == "yes" %}
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
{%- else %}
    python_requires='>=3.6',
{%- endif %}
    install_requires=[
{%- if cookiecutter.command_line_interface == 'click' %}
        'click',
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
        'cffi>=1.0.0',
{%- endif %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- set setup_requires_interior %}
{%- if cookiecutter.test_runner == 'pytest' and cookiecutter.setup_py_uses_test_runner == 'yes' %}
        'pytest-runner',{% endif %}
{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
        'setuptools_scm>=3.3.1{% if cookiecutter.legacy_python == 'yes' %},<6.0{% endif %}',{% endif %}
{%- endset %}
{%- if cookiecutter.c_extension_support == 'cython' %}
    setup_requires=[{{ setup_requires_interior }}
        'cython',
    ] if Cython else [{{ setup_requires_interior }}
    ],
{%- elif cookiecutter.c_extension_support == 'cffi' %}
    # We only require CFFI when compiling.
    # pyproject.toml does not support requirements only for some build actions,
    # but we can do it in setup.py.
    setup_requires=[{{ setup_requires_interior }}
        'cffi>=1.0.0',
    ] if any(i.startswith('build') or i.startswith('bdist') for i in sys.argv) else [{{setup_requires_interior}}
    ],
{%- elif setup_requires_interior.strip() %}
    setup_requires=[{{ setup_requires_interior }}
    ],
{%- endif -%}
{%- if cookiecutter.command_line_interface != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:main',
        ]
    },
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' -%}
{%- if cookiecutter.c_extension_optional == 'yes' %}
    cmdclass={'build_ext': OptionalBuildExt},
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
    cffi_modules=[i + ':ffi' for i in glob('src/*/_*_build.py')],
{%- else %}
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
{%- if cookiecutter.c_extension_support in ['yes', 'cython'] %}
            extra_compile_args=CFLAGS.split(),
            extra_link_args=LFLAGS.split(),
{%- endif %}
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root,
{%- if cookiecutter.c_extension_support == 'cython' %} '*.pyx' if Cython else '*.c'
{%- else %} '*.c'{% endif %}))
    ],
    distclass=BinaryDistribution,
{%- endif %}
{%- endif %}
)
