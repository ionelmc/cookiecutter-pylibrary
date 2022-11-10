import pathlib
import shutil
import subprocess
import sys


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

    cwd = pathlib.Path().resolve()
    src = cwd / 'src'
    ci = cwd / 'ci'

{% if cookiecutter.sphinx_docs == "no" %}
    shutil.rmtree(cwd / 'docs')
    cwd.joinpath('.readthedocs.yml').unlink()
{%- elif 'readthedocs' not in cookiecutter.sphinx_docs_hosting %}
    cwd.joinpath('.readthedocs.yml').unlink()
{% endif %}


{%- if cookiecutter.command_line_interface == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '__main__.py').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', 'cli.py').unlink()
{% endif %}

{%- if cookiecutter.test_matrix_configurator == 'no' %}
    ci.joinpath('templates', 'tox.ini').unlink()
{% endif %}
{%- if cookiecutter.allow_tests_inside_package == 'no' %}
    shutil.rmtree(src / '{{ cookiecutter.package_name }}' / 'tests')
{% endif %}
{%- if cookiecutter.c_extension_support == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py').unlink()
{%- elif cookiecutter.c_extension_support == 'cffi' %}
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx').unlink()
{%- elif cookiecutter.c_extension_support == 'cython' %}
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py').unlink()
    try:
        subprocess.check_call(['tox', '-e', 'cythonize'])
    except Exception:
        subprocess.check_call([sys.executable, '-mtox', '-e', 'cythonize'])
{%- else %}
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py').unlink()
{%- endif %}

    ci.joinpath('appveyor-with-compiler.cmd').unlink(missing_ok=True)
{%- if cookiecutter.appveyor == 'no' %}
    ci.joinpath('templates', '.appveyor.yml').unlink()
    ci.joinpath('.appveyor.yml').unlink(missing_ok=True)
{% endif %}
    cwd.joinpath('appveyor.yml').unlink(missing_ok=True)
    ci.joinpath('templates', 'appveyor.yml').unlink(missing_ok=True)
    ci.joinpath('appveyor-bootstrap.py').unlink(missing_ok=True)

{%- if cookiecutter.travis == 'no' %}
    ci.joinpath('templates', '.travis.yml').unlink()
    cwd.joinpath('.travis.yml').unlink(missing_ok=True)
{% endif %}

{%- if cookiecutter.github_actions == 'no' %}
    ci.joinpath('templates', '.github', 'workflows', 'github-actions.yml').unlink()
    cwd.joinpath('.github', 'workflows', 'github-actions.yml').unlink(missing_ok=True)
{% endif %}

{%- if cookiecutter.repo_hosting == 'no' %}
    cwd.joinpath('CONTRIBUTING.rst').unlink()
{% endif %}

{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
    cwd.joinpath('MANIFEST.in').unlink()
{% endif %}

{%- if cookiecutter.pre_commit == 'no' %}
    cwd.joinpath('.pre-commit-config.yaml').unlink()
{% endif %}

{%- if cookiecutter.version_manager == 'bump2version' %}
    cwd.joinpath('tbump.toml').unlink()
{%- elif cookiecutter.version_manager == 'tbump' %}
    cwd.joinpath('.bumpversion.cfg').unlink()
{% endif %}

{%- if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink()
{% endif %}

    print("""
################################################################################

    Generating CI configuration ...
""")
    try:
        subprocess.check_call(['tox', '-e', 'bootstrap', '--sitepackages'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap', '--sitepackages'])
        except Exception:
            subprocess.check_call([sys.executable, ci / 'bootstrap.py'])

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
        git tag v{{ cookiecutter.version }}
        git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}

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
    - https://travis-ci.com{% if cookiecutter.repo_hosting == 'github.com' %}/github
                           {%- elif cookiecutter.repo_hosting == 'gitlab.com' %}/gitlab
                           {%- endif %}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/settings
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
