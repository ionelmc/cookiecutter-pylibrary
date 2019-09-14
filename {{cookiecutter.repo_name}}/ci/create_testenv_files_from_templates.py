#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import jinja2
{% if cookiecutter.test_matrix_configurator == "yes" %}
import matrix
{% else %}
import subprocess
{% endif %}
import sys
import os
from os.path import join

if __name__ == "__main__":
    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(base_path, "ci", "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )
{% if cookiecutter.test_matrix_configurator == "yes" %}
    tox_environments = {}
    for (alias, conf) in matrix.from_file(join(base_path, "setup.cfg")).items():
        python = conf["python_versions"]
        deps = conf["dependencies"]
        tox_environments[alias] = {
            "deps": deps.split(),
        }
        if "coverage_flags" in conf:
            cover = {"false": False, "true": True}[conf["coverage_flags"].lower()]
            tox_environments[alias].update(cover=cover)
        if "environment_variables" in conf:
            env_vars = conf["environment_variables"]
            tox_environments[alias].update(env_vars=env_vars.split())
{% else %}
    tox_environments = [
        line.strip()
        # 'tox' need not be installed globally, but must be importable
        # by the Python that is running this script.
        # This uses sys.executable the same way that the call in
        # cookiecutter-pylibrary/hooks/post_gen_project.py
        # invokes this bootstrap.py itself.
        for line in subprocess.check_output([sys.executable, '-m', 'tox', '--listenvs'], universal_newlines=True).splitlines()
    ]
    tox_environments = [line for line in tox_environments if line.startswith('py')]
{% endif %}
    for name in os.listdir(join("ci", "templates")):
        with open(join(base_path, name), "w") as fh:
            fh.write(jinja.get_template(name).render(tox_environments=tox_environments))
        print("Wrote {}".format(name))
    print("DONE.")
