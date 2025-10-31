import shutil
import subprocess
import sys
from pathlib import Path


try:
    from click.termui import secho
except ImportError:
    warn = note = success = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)

    def success(text):
        for line in text.splitlines():
            secho(line, fg="green", bold=True)



if __name__ == "__main__":
    cwd = Path().resolve()
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
    src.joinpath('{{ cookiecutter.package_name }}', 'tests', 'test_cli.py').unlink()
    cwd.joinpath('tests', 'test_cli.py').unlink()
{% endif %}

    ci.joinpath('templates', 'tox.ini').unlink(missing_ok=True)

{%- if cookiecutter.tests_inside_package == 'no' %}
    shutil.rmtree(src / '{{ cookiecutter.package_name }}' / 'tests')
{%- else %}
    shutil.rmtree('tests')
{%- endif %}

{%- if cookiecutter.c_extension_support == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}.c').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}.pyx').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}_build.py').unlink()
{%- elif cookiecutter.c_extension_support == 'cffi' %}
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}.pyx').unlink()
{%- elif cookiecutter.c_extension_support == 'cython' %}
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}.c').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}_build.py').unlink()
    try:
        subprocess.check_call(['tox', '-e', 'cythonize'])
    except Exception:
        subprocess.check_call([sys.executable, '-mtox', '-e', 'cythonize'])
{%- else %}
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}.pyx').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', '_{{ cookiecutter.module_name }}_build.py').unlink()
{%- endif %}

    ci.joinpath('appveyor-bootstrap.py').unlink(missing_ok=True)
    ci.joinpath('appveyor-download.py').unlink(missing_ok=True)
    ci.joinpath('appveyor-with-compiler.cmd').unlink(missing_ok=True)
    ci.joinpath('templates', '.appveyor.yml').unlink(missing_ok=True)
    ci.joinpath('templates', 'appveyor.yml').unlink(missing_ok=True)
    ci.joinpath('templates', '.travis.yml').unlink(missing_ok=True)
    cwd.joinpath('.appveyor.yml').unlink(missing_ok=True)
    cwd.joinpath('appveyor.yml').unlink(missing_ok=True)
    cwd.joinpath('.travis.yml').unlink(missing_ok=True)

{%- if cookiecutter.github_actions == 'no' %}
    ci.joinpath('templates', '.github', 'workflows', 'github-actions.yml').unlink()
    cwd.joinpath('.github', 'workflows', 'github-actions.yml').unlink(missing_ok=True)
{% endif %}

{%- if cookiecutter.repo_hosting == 'no' %}
    cwd.joinpath('CONTRIBUTING.rst').unlink()
{% endif %}

{%- if cookiecutter.setup_py_uses_setuptools_scm == 'yes' %}
    cwd.joinpath('MANIFEST.in').unlink()
{%- else %}
    src.joinpath('{{ cookiecutter.package_name }}', '_version.py').unlink(missing_ok=True)
{% endif %}

{%- if cookiecutter.version_manager == 'bump2version' %}
    cwd.joinpath('tbump.toml').unlink()
{%- elif cookiecutter.version_manager == 'tbump' %}
    cwd.joinpath('.bumpversion.cfg').unlink()
{% endif %}

{%- if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink()
{% endif %}
    cwd.joinpath('setup.cfg').unlink(missing_ok=True)

    width = min(140, shutil.get_terminal_size(fallback=(140, 0)).columns)
    note(" Generating CI configuration ".center(width, "#"))
    try:
        subprocess.check_call(['tox', '-e', 'bootstrap', '--sitepackages'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap', '--sitepackages'])
        except Exception:
            subprocess.check_call([sys.executable, ci / 'bootstrap.py'])
    if shutil.which('git'):
        if not Path('.git').is_dir():
            note('+ git init')
            subprocess.check_call(['git', 'init'])
        note(' Setting up pre-commit '.center(width, "#"))
        if prek:=shutil.which('prek'):
            note('+ prek autoupdate')
            subprocess.check_call(['prek', 'autoupdate'])
        elif shutil.which('pre-commit'):
            note('+ pre-commit autoupdate')
            subprocess.check_call(['pre-commit', 'autoupdate'])
    else:
        warn('Not git available. Skipping pre-commit setup.')
    precommit_name= 'prek' if prek else 'pre-commit'
    success(' Successfully created `{{ cookiecutter.repo_name }}` '.center(width, "#"))
    print('See .cookiecutterrc for instructions on regenerating the project.')
    note('To get started run these:')
    print(f'''
cd {{ cookiecutter.repo_name }}
git init
{precommit_name} install --install-hooks
{precommit_name} autoupdate
git add --all
git commit -m "Add initial project skeleton."
git tag v{{ cookiecutter.version }}
git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}
''')
    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name }}':
            warn('''
┌───────────────────────────────────────────────────────────────────────┐
│ ERROR:                                                                │
│                                                                       │
│     Your result package is broken. Your bin script named              │
│     {0} │
│                                                                       │
│     Python automatically adds the location of scripts to              │
│     `sys.path`. Because of that, the bin script will fail             │
│     to import your package because it has the same name               │
│     (it will try to import itself as a module).                       │
│                                                                       │
│     To avoid this problem you have two options:                       │
│                                                                       │
│     * Remove the ".py" suffix from `command_line_interface_bin_name`. │
│                                                                       │
│     * Use a different `package_name` {1} │
└───────────────────────────────────────────────────────────────────────┘
'''.format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
            sys.exit(1)
        break
