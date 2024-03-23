import subprocess


def test_main():
    assert subprocess.check_output(["{{ cookiecutter.command_line_interface_bin_name }}", "foo", "foobar"], text=True) == "foobar\n"
