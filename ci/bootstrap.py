#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
from os.path import exists
from os.path import join


if __name__ == "__main__":
    base_path = join(".tox", "configure")
    if sys.platform == "win32":
        bin_path = join(base_path, "Scripts")
    else:
        bin_path = join(base_path, "bin")
    if not exists(base_path):
        import subprocess
        print("Bootstrapping ...")
        try:
            subprocess.check_call(["virtualenv", base_path])
        except Exception:
            subprocess.check_call([sys.executable, "-m", "virtualenv", base_path])
        print("Installing `jinja2` and `matrix` into bootstrap environment ...")
        subprocess.check_call([join(bin_path, "pip"), "install", "jinja2", "matrix"])
    activate = join(bin_path, "activate_this.py")
    exec(compile(open(activate, "rb").read(), activate, "exec"), dict(__file__=activate))

    import jinja2
    import matrix

    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join("ci", "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )
    tox_environments = {}
    for (alias, conf) in matrix.from_file("setup.cfg").items():
        python = conf["python_versions"]
        deps = conf["dependencies"]
        if "coverage_flags" in conf:
            cover = {"false": False, "true": True}[conf["coverage_flags"].lower()]
        if "environment_variables" in conf:
            env_vars = conf["environment_variables"]

        tox_environments[alias] = {
            "python": "python" + python if "py" not in python else python,
            "deps": deps.split(),
        }
        if "coverage_flags" in conf:
            tox_environments[alias].update(cover=cover)
        if "environment_variables" in conf:
            tox_environments[alias].update(env_vars=env_vars.split())

    for name in os.listdir(join("ci", "templates")):
        with open(name, "w") as fh:
            fh.write(jinja.get_template(name).render(tox_environments=tox_environments))
        print("Wrote {}".format(name))
    print("DONE.")
