{{ cookiecutter.package_name }}
{{ "=" * cookiecutter.package_name|length }}

.. testsetup::

    from {{ cookiecutter.package_name }} import *

.. automodule:: {{ cookiecutter.package_name }}
    :members:
    :undoc-members:
    :special-members: __init__, __len__
