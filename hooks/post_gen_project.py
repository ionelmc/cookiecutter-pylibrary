if __name__ == "__main__":
    print("""
################################################################################

    Configuring your test environments for the first time ...
""")
    {% if cookiecutter.test_matrix_configurator|lower == "yes" %}
    import subprocess
    import sys
    try:
        subprocess.check_call(['tox'])
    except Exception:
        subprocess.check_call([sys.executable, '-mtox'])
    {% else %}
    import os
    os.unlink(os.path.join('ci/bootstrap.py'))
    {% endif %}

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

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
{% endif %}
""")
