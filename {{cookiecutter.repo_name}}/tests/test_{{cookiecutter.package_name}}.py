{%- if cookiecutter.command_line_interface == 'click' %}
from click.testing import CliRunner
{% endif %}
{%- if cookiecutter.c_extension_support != 'no' %}
from {{ cookiecutter.package_name }} import {{ cookiecutter.c_extension_function }}
{%- endif %}
{%- if cookiecutter.command_line_interface != 'no' %}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' or
       cookiecutter.command_line_interface == 'no' %}
from {{ cookiecutter.package_name }} import main
{%- endif %}


def test_main():
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' %}
    assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter.command_line_interface == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface == 'argparse' %}
    main([])
{%- elif cookiecutter.command_line_interface == 'plain' %}
    assert main([]) == 0
{%- else %}
    pass
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}


def test_{{ cookiecutter.c_extension_function }}():
    assert {{ cookiecutter.c_extension_function }}([b'a', b'bc', b'abc']) == b'abc'
{%- endif %}
