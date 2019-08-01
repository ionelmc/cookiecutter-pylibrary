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
    warn = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)


def replace_contents(filename, what, replacement):
    with open(filename) as fh:
        changelog = fh.read()
    with open(filename, 'w') as fh:
        fh.write(changelog.replace(what, replacement))

if __name__ == "__main__":
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
    os.unlink(join('ci', 'appveyor-bootstrap.py'))
    os.unlink(join('ci', 'appveyor-download.py'))
    os.unlink(join('ci', 'appveyor-with-compiler.cmd'))
    os.unlink(join('ci', 'templates', '.appveyor.yml'))
    if os.path.exists('.appveyor.yml'):
        os.unlink('.appveyor.yml')
{% endif %}

{%- if cookiecutter.travis == 'no' %}
    os.unlink(join('ci', 'templates', '.travis.yml'))
    if os.path.exists('.travis.yml'):
        os.unlink('.travis.yml')
{% endif %}

{%- if cookiecutter.repo_hosting == 'no' %}
    os.unlink('CONTRIBUTING.rst')
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

    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      WARNING:                                                              !!
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
        break
