from {{ cookiecutter.package_name }} import {{ cookiecutter.function_name }}


def test_{{ cookiecutter.function_name }}():
    assert {{ cookiecutter.function_name }}(["a", "bc", "abc"]) == "abc"
