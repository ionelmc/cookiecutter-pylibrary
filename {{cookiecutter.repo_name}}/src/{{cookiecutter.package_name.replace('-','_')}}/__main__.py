import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
# Why does this file exist, and why __main__?
# For more info, read:
# - https://www.python.org/dev/peps/pep-0338/
# - https://docs.python.org/2/using/cmdline.html#cmdoption-m
# - https://docs.python.org/3/using/cmdline.html#cmdoption-m


{% if cookiecutter.command_line_interface|lower == 'click' -%}
@click.command()
@click.argument('names', nargs=-1)
def main(names):
    click.echo(repr(names))
{%- else -%}
def main(argv=()):
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

if __name__ == "__main__":
    sys.exit(main())
