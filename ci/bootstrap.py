#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
from os.path import exists
from os.path import join
from os.path import dirname
from os.path import abspath


if __name__ == "__main__":
    base_path = dirname(dirname(abspath(__file__)))
    print("Project path: {0}".format(base_path))
    env_path = join(base_path, ".tox", "bootstrap")
    if sys.platform == "win32":
        bin_path = join(env_path, "Scripts")
    else:
        bin_path = join(env_path, "bin")
    if not exists(env_path):
        import subprocess
        print("Making bootstrap env in: {0} ...".format(env_path))
        try:
            subprocess.check_call(["virtualenv", env_path])
        except Exception:
            subprocess.check_call([sys.executable, "-m", "virtualenv", env_path])
        print("Installing `jinja2` and `matrix` into bootstrap environment ...")
        subprocess.check_call([join(bin_path, "pip"), "install", "jinja2", "matrix", "pyyaml"])
    activate = join(bin_path, "activate_this.py")
    exec(compile(open(activate, "rb").read(), activate, "exec"), dict(__file__=activate))

    import jinja2
    import matrix
    import yaml

    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(base_path, "ci", "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )
    tox_environments = {}
    for name in os.listdir(join(base_path, "ci", "envs")):
        os.unlink(join(base_path, "ci", "envs", name))

    for (alias, conf) in matrix.from_file(join(base_path, "ci", "setup.cfg")).items():
        tox_environments[alias] = conf
        conf['repo_name'] = 'python-nameless'
        conf['package_name'] = 'nameless'
        with open(join(base_path, "ci", "envs", alias + '.cookiecutterrc'), "w") as fh:
            fh.write(yaml.safe_dump(
                dict(default_context={k: v for k, v in conf.items() if v}),
                default_flow_style=False
            ))
    for name in os.listdir(join(base_path, "ci", "templates")):
        with open(join(base_path, name), "w") as fh:
            fh.write(jinja.get_template(name).render(tox_environments=tox_environments))
        print("Wrote {}".format(name))
    print("DONE.")
