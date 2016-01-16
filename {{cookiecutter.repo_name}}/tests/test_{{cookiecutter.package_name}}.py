{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import main
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}
import {{ cookiecutter.package_name }}


def test_main():
{%- if cookiecutter.test_matrix_configurator|lower == 'yes' %}
    assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
    assert main([]) == 0
{%- else %}
    assert {{ cookiecutter.package_name }}  # use your library here
{%- endif %}
