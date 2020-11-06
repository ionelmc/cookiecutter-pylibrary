============
Installation
============

This can also be installed by conda via the `conda-channel <_static/conda-channel/index.html>`_ if the most recent build included conda::

    conda install --name tmpEnv --channel {{ cookiecutter.sphinx_docs_hosting }}/_static/conda-channel {{ cookiecutter.distribution_name }}

Because building a conda package significantly slows our build time, we might not build a conda package every time.
If you need a conda package of the latest commits and the `conda-channel <_static/conda-channel/index.html>`_ is empty, please reach out to us.

At the command line::

    pip install {{ cookiecutter.distribution_name }}
