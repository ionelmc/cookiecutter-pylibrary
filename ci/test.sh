#!/bin/bash -eE
shopt -s xpg_echo

echo "\033[1;36m################################################################################\033[0m"
echo "\033[1;36m################################################################################\033[0m"
echo ""
echo "\033[1;36m    Testing: $USERPROFILE\033[0m"
echo ""
echo "\033[1;36m################################################################################\033[0m"

set -x
pwd
rm -rf python-nameless
cookiecutter --no-input .
cd python-nameless
git init .
git add .
git commit -m "initial."
bumpversion patch
bumpversion minor
bumpversion major
sed -i 's/sphinx-build -b linkcheck/#/' tox.ini
tox
