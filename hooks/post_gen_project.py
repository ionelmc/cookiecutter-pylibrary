if __name__ == "__main__":
{% if cookiecutter.test_matrix_configurator|lower == "yes" %}
    print("""
################################################################################

    For your convenience, the test environments are getting configured for the
    first time, as you have selected "yes" for `test_matrix_configurator` ...
""")
    from os.path import join
    import subprocess
    import sys
    try:
        subprocess.check_call(['tox'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox'])
        except Exception:
            subprocess.check_call([sys.executable, join('ci', 'bootstrap.py')])
{% endif %}
    from os.path import join
    import shutil
    import os

{%- if cookiecutter.command_line_interface|lower == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name|replace('-', '_') }}', '__main__.py'))
{% endif %}

{%- if cookiecutter.test_matrix_configurator|lower == 'no' %}
    os.unlink(join('ci', 'bootstrap.py'))
    shutil.rmtree(join('ci', 'templates'))
{% endif %}

{%- if cookiecutter.appveyor|lower == 'no' %}
    os.unlink(join('ci', 'appveyor-bootstrap.ps1'))
    os.unlink(join('ci', 'appveyor-with-compiler.cmd'))
    os.unlink('appveyor.yml')
    if os.path.exists(join('ci', 'templates', 'appveyor.yml')):
        os.unlink(join('ci', 'templates', 'appveyor.yml'))
{% endif %}

{%- if cookiecutter.travis|lower == 'no' %}
    os.unlink('.travis.yml')
    if os.path.exists(join('ci', 'templates', '.travis.yml')):
        os.unlink(join('ci', 'templates', '.travis.yml'))
{% endif %}

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master

{% if cookiecutter.test_matrix_configurator|lower == "yes" %}
    To reconfigure your test/CI settings run:

        tox -e bootstrap

    You can also run:

        ci/bootstrap.py
{% else %}
    The project doesn't use the test matrix configurator, but in case
    you change your mind just edit `setup.cfg` and run `ci/bootstrap.py`.
{% endif %}
""")
