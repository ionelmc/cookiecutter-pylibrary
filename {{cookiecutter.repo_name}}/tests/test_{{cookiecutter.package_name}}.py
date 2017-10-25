from {{ cookiecutter.package_name }} import {{ cookiecutter.c_extension_function }}

{%- if cookiecutter.command_line_interface == 'click' %}
from click.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import main
{%- elif cookiecutter.command_line_interface in ['plain', 'argparse'] %}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' or
       cookiecutter.command_line_interface == 'no' %}
import {{ cookiecutter.package_name }}
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
    assert {{ cookiecutter.package_name }}  # use your library here
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}


def test_{{ cookiecutter.c_extension_function }}():
    assert {{ cookiecutter.c_extension_function }}(['a', 'bc', 'abc']) == 'abc'
{%- endif %}
