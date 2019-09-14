#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
from os.path import abspath
from os.path import dirname
from os.path import exists
from os.path import join
from os.path import normpath

if __name__ == "__main__":
    base_path = dirname(dirname(abspath(__file__)))
    print("Project path: {0}".format(base_path))
    env_path = join(base_path, ".tox", "bootstrap")
    if not exists(env_path):
        import subprocess

        print("Making bootstrap env in: {0} ...".format(env_path))
        try:
            subprocess.check_call([sys.executable, "-m", "venv", env_path])
        except subprocess.CalledProcessError:
            subprocess.check_call([sys.executable, "-m", "virtualenv", env_path])
        print("Installing `jinja2` into bootstrap environment...")
        subprocess.check_call([join(bin_path, "pip"), "install", "jinja2"])
        subprocess.check_call([join(bin_path, "pip"), "install", "tox"])
    bin_path = join(env_path, "Scripts" if sys.platform == "win32" else "bin")
    python_executable = join(bin_path, "python")
    if not os.path.exists(python_executable):
        python_executable += '.exe'
    assert os.path.exists(python_executable)
    # We do not want to use samefile here --- on some platforms,
    # a new virtual environment will get an executable that is a symlink to
    # the parent Python executable. The path used to activate it nevertheless
    # causes the executable to use that virtual environment.
    # Obviously we need to worry about an infinite loop here.
    # != is probably safe, but what would definitely be safe would be to split
    # the rest of this file into a separate script and unconditionally execute
    # that with python_executable.
    os.execv(python_executable, [python_executable, join(dirname(__file__), "create_testenv_files_from_templates.py")])


