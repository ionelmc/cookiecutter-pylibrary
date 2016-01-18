{{ cookiecutter.package_name|replace('-', '_') }}
{{ "=" * cookiecutter.package_name|length }}

.. testsetup::

    from {{ cookiecutter.package_name|replace('-', '_') }} import *

.. automodule:: {{ cookiecutter.package_name|replace('-', '_') }}
    :members:
