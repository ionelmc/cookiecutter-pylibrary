"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m{{cookiecutter.package_name}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- else %}
import sys
{%- endif %}


{% if cookiecutter.command_line_interface|lower == 'click' -%}
@click.command()
@click.argument('names', nargs=-1)
def main(names):
    click.echo(repr(names))
{%- else -%}
def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """

    print(argv)
    return 0
{%- endif %}
