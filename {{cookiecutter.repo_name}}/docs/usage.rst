=====
Usage
=====

To use the project:

{% if cookiecutter.command_line_interface != "no" -%}
.. code-block:: python

    import {{ cookiecutter.package_name }}
    {{ cookiecutter.package_name }}.{{ cookiecutter.function_name }}(...)
{% else -%}
.. code-block:: bash

    $ {{ cookiecutter.command_line_interface_bin_name }} ...
{% endif -%}
