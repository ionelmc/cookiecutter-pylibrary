{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner

from {{cookiecutter.package_name}}.__main__ import main
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
from {{cookiecutter.package_name}}.__main__ import main
{%- else %}
import {{cookiecutter.package_name}}
{%- endif %}


def test_main():
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
    assert main([]) == 0
{%- else %}
    assert {{cookiecutter.package_name}}  # use your library here
{%- endif %}
