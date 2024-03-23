from .. import {{ cookiecutter.function_name }}


def test_{{ cookiecutter.function_name }}():
    assert {{ cookiecutter.function_name }}([b"a", b"bc", b"abc"]) == b"abc"
