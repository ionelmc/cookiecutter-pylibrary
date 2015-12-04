#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import find_packages
from setuptools import setup
{%- if cookiecutter.c_extension_support|lower == 'yes' -%}
{%- if cookiecutter.c_extension_optional|lower == 'yes' %}
from setuptools.command.build_ext import build_ext
{%- endif %}
from distutils.core import Extension
{%- if cookiecutter.c_extension_optional|lower == 'yes' %}
from distutils.errors import CCompilerError
from distutils.errors import CompileError
from distutils.errors import DistutilsExecError
from distutils.errors import DistutilsPlatformError
{%- endif %}
{%- endif %}


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


{% if cookiecutter.c_extension_support|lower == 'yes' -%}
# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

{% endif %}
{% if cookiecutter.c_extension_support|lower == 'yes' and cookiecutter.c_extension_optional|lower == 'yes' -%}
class optional_build_ext(build_ext):
    '''Allow the building of C extensions to fail.'''
    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
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
setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    license='BSD',
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M|re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
{%- if cookiecutter.command_line_interface|lower == 'click' %}
        'click',
{%- else %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
{%- endif %}
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- if cookiecutter.command_line_interface|lower in ['plain', 'click'] %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.distribution_name }} = {{ cookiecutter.package_name|replace('-', '_') }}.cli:main',
        ]
    },
{%- endif %}
{%- if cookiecutter.c_extension_support|lower == 'yes' -%}
{%- if cookiecutter.c_extension_optional|lower == 'yes' %}
    cmdclass={'build_ext': optional_build_ext},
{%- endif %}
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root, '*.c'))
    ]
{%- endif %}
)
