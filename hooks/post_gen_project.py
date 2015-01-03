if __name__ == "__main__":
    print("""
*******************************************************************************
*******************************************************************************

    You have succesfully created `{{ cookiecutter.repo_name }}`.

*******************************************************************************

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        tox -e configure
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master

*******************************************************************************
*******************************************************************************
""")
