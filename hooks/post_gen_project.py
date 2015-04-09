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
{%- if cookiecutter.command_line_interface|lower == 'no' %}
    from os.path import join
    import os
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '__main__.py'))
{% endif %}

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "%-26s"|format(key + ":") }} {{ (value|pprint).lstrip("u") }}
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
