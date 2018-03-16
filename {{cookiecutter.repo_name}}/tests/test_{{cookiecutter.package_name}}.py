{%- if cookiecutter.test_runner == "unittest" %}
import unittest
{% endif %}
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

{%- if cookiecutter.test_runner == "unittest" %}


class TestClass(unittest.TestCase):

    def test_main(self):
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' %}
        assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter.command_line_interface == 'click' %}
        runner = CliRunner()
        result = runner.invoke(main, [])

        self.assertEqual(result.output, '()\n')
        self.assertEqual(result.exit_code, 0)
{%- elif cookiecutter.command_line_interface == 'argparse' %}
        main([])
{%- elif cookiecutter.command_line_interface == 'plain' %}
        self.assertEqual(main([]), 0)
{%- else %}
        pass
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}

    def test_{{ cookiecutter.c_extension_function }}(self):
        self.assertEqual({{ cookiecutter.c_extension_function }}([b'a', b'bc', b'abc']), b'abc')
{%- endif %}

{%- else %}


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
{%- endif %}
