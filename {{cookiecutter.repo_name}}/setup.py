#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
{% if cookiecutter.c_extension_support != 'no' -%}
import os
{% endif -%}
import re
{% if cookiecutter.c_extension_support == 'cffi' -%}
import sys
{% endif -%}
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
{% if cookiecutter.c_extension_support not in ['no', 'cffi'] -%}
from os.path import relpath
{% endif -%}
from os.path import splitext

{% if cookiecutter.c_extension_support not in ['no', 'cffi'] -%}
from setuptools import Extension
{% endif -%}
from setuptools import find_packages
from setuptools import setup
{%- if cookiecutter.c_extension_support != 'no' -%}
{%- if cookiecutter.c_extension_optional == 'yes' %}
from setuptools.command.build_ext import build_ext
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cython' %}

try:
    # Allow installing package without any Cython available. This
    # assumes you are going to include the .c files in your sdist.
    import Cython
except ImportError:
    Cython = None
{%- endif %}
{%- endif %}


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


{% if cookiecutter.c_extension_support != 'no' -%}
# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

{% if cookiecutter.c_extension_optional == 'yes' %}
class optional_build_ext(build_ext):
    """Allow the building of C extensions to fail."""
    def run(self):
        try:
            build_ext.run(self)
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


{% endif -%}
{% endif -%}
setup(
    name='{{ cookiecutter.distribution_name }}',
{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/{{ cookiecutter.package_name }}/_version.py',
        'fallback_version': '1.4.1',
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
        "Apache Software License 2.0": "Apache-2.0"}[cookiecutter.license]
    }}',
{%- endif %}
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
{%- if cookiecutter.repo_hosting != "no" %}
    url='https://{{ cookiecutter.repo_hosting }}.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}',
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
{%- endif %}
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
{%- if cookiecutter.repo_hosting == "no" %}
        'Private :: Do Not Upload',
{%- endif %}
    ],
{%- if cookiecutter.repo_hosting != "no" %}
    project_urls={
{%- if cookiecutter.sphinx_docs == "yes" %}
        'Documentation': 'https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/',
        'Changelog': 'https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/en/latest/changelog.html',
{%- else %}
        'Changelog': 'https://{{ cookiecutter.repo_hosting }}.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst',
{%- endif %}
        'Issue Tracker': 'https://{{ cookiecutter.repo_hosting }}.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues',
    },
{%- endif %}
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
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
{%- if cookiecutter.test_runner == 'pytest' and cookiecutter.setup_py_uses_test_runner == 'yes' -%}
{% set setup_requires_from_test_runner %}
        'pytest-runner',{% endset %}
{%- else -%}
{% set setup_requires_from_test_runner %}{% endset %}
{%- endif -%}
{%- if cookiecutter.c_extension_support == 'cython' %}
    setup_requires=[{{ setup_requires_from_test_runner }}
        'cython',
    ] if Cython else [{{ setup_requires_from_test_runner }}
    ],
{%- elif cookiecutter.c_extension_support == 'cffi' %}
    setup_requires=[{{ setup_requires_from_test_runner }}
        'cffi>=1.0.0',
    ] if any(i.startswith('build') or i.startswith('bdist') for i in sys.argv) else [{{setup_requires_from_test_runner}}
    ],
{%- else %}
    setup_requires=[{{ setup_requires_from_test_runner }}
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
    cmdclass={'build_ext': optional_build_ext},
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
    cffi_modules=[i + ':ffi' for i in glob('src/*/_*_build.py')],
{%- else %}
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root,
{%- if cookiecutter.c_extension_support == 'cython' %} '*.pyx' if Cython else '*.c'
{%- else %} '*.c'{% endif %}))
    ],
{%- endif %}
{%- endif %}
)
