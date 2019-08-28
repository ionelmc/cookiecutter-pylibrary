from __future__ import print_function

import datetime
import os
import shutil
import subprocess
import sys
from os.path import join

try:
    from click.termui import secho
except ImportError:
    warn = note = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)

def replace_contents(filename, what, replacement):
    with open(filename) as fh:
        changelog = fh.read()
    with open(filename, 'w') as fh:
        fh.write(changelog.replace(what, replacement))

if __name__ == "__main__":
{%- if cookiecutter.c_extension_test_pypi == 'yes' %}
{%- if cookiecutter.test_matrix_separate_coverage == 'no' %}
    warn("TODO: c_extension_test_pypi=yes will not work with test_matrix_separate_coverage=no for now.")
    sys.exit(1)
{%- endif %}
{%- if cookiecutter.c_extension_support == 'no' %}
    warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      ERROR:                                                                !!
!!                                                                            !!
!!          c_extension_test_pypi=yes is designed to build and publish        !!
!!          platform-specific wheels.                                         !!
!!                                                                            !!
!!          You have set c_extension_support=no, and that will make every     !!
!!          test environment publish duplicated universal wheels.             !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""")
    sys.exit(1)
{%- endif %}
{%- endif %}


    today = datetime.date.today()
    replace_contents('CHANGELOG.rst', '<TODAY>', today.strftime("%Y-%m-%d"))
    replace_contents(join('docs', 'conf.py'), '<YEAR>', today.strftime("%Y"))
    replace_contents('LICENSE', '<YEAR>', today.strftime("%Y"))

{% if cookiecutter.sphinx_docs == "no" %}
    shutil.rmtree('docs')
{% endif %}

{%- if cookiecutter.command_line_interface == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '__main__.py'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', 'cli.py'))
{% endif %}

{%- if cookiecutter.test_matrix_configurator == 'no' %}
    os.unlink(join('ci', 'templates', 'tox.ini'))
{% endif %}
{%- if cookiecutter.allow_tests_inside_package == 'no' %}
    shutil.rmtree(join('src', '{{ cookiecutter.package_name }}', 'tests'))
{% endif %}

{%- if cookiecutter.c_extension_support == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
{%- elif cookiecutter.c_extension_support == 'cffi' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
{%- elif cookiecutter.c_extension_support == 'cython' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
    try:
        subprocess.check_call(['tox', '-e', 'cythonize'])
    except Exception:
        subprocess.check_call([sys.executable, '-mtox', '-e', 'cythonize'])
{%- else %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
{%- endif %}

{%- if cookiecutter.appveyor == 'no' %}
    os.unlink(join('ci', 'appveyor-download.py'))
    os.unlink(join('ci', 'appveyor-with-compiler.cmd'))
    os.unlink(join('ci', 'templates', '.appveyor.yml'))
    if os.path.exists('.appveyor.yml'):
        os.unlink('.appveyor.yml')
{% endif %}
    if os.path.exists('appveyor.yml'):
        os.unlink('appveyor.yml')
    if os.path.exists(join('ci', 'appveyor-bootstrap.py')):
        os.unlink(join('ci', 'appveyor-bootstrap.py'))

{%- if cookiecutter.travis == 'no' %}
    os.unlink(join('ci', 'templates', '.travis.yml'))
    if os.path.exists('.travis.yml'):
        os.unlink('.travis.yml')
{% endif %}

{%- if cookiecutter.repo_hosting == 'no' %}
    os.unlink('CONTRIBUTING.rst')
{% endif %}

{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
    os.unlink('MANIFEST.in')
{% endif %}

{%- if cookiecutter.license == "no" %}
    os.unlink('LICENSE')
{% endif %}

    print("""
################################################################################

    Generating CI configuration ...
""")
    try:
        subprocess.check_call(['tox', '-e', 'bootstrap'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap'])
        except Exception:
            subprocess.check_call([sys.executable, join('ci', 'bootstrap.py')])

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

    See .cookiecutterrc for instructions on regenerating the project.

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@{{ cookiecutter.repo_hosting }}.com:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master

{% if cookiecutter.test_matrix_configurator == "yes" %}
    To regenerate your tox.ini, .travis.yml or .appveyor.yml run:
{% else %}
    To regenerate your .travis.yml or .appveyor.yml run:
{% endif %}

        tox -e bootstrap

    You can also run:

        ./ci/bootstrap.py

""")

{%- if cookiecutter.c_extension_test_pypi == 'yes' %}
    note("""
NOTE:

    You are using the c_extension_test_pypi option.

    Make sure you are setting TWINE_PASSWORD as a secret env variable in CI settings:
    - https://ci.appveyor.com/project/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/settings/environment
    - https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/settings
""")
{%- endif %}

    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      ERROR:                                                                !!
!!                                                                            !!
!!          Your result package is broken. Your bin script named              !!
!!          {0} !!
!!                                                                            !!
!!          Python automatically adds the location of scripts to              !!
!!          `sys.path`. Because of that, the bin script will fail             !!
!!          to import your package because it has the same name               !!
!!          (it will try to import itself as a module).                       !!
!!                                                                            !!
!!          To avoid this problem you have two options:                       !!
!!                                                                            !!
!!          * Remove the ".py" suffix from the `command_line_interface_bin_name`.                    !!
!!                                                                            !!
!!          * Use a different `package_name` {1} !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
            sys.exit(1)
        break
