#!/bin/bash -eE
shopt -s xpg_echo

if [ -z "$1" ]; then
    echo Usage:
    echo    $0 env-name
    exit 1
fi

# A safer way to invoke 'sed', compensates for the difference between BSD and GNU sed. 
# https://stackoverflow.com/a/38595160/1950432
safe_sed () {
    sed --version > /dev/null 2>&1 && sed -i -- "$@" || sed -i "" "$@"
}

echo "\033[1;36m================================\033[0m"
echo "\033[1;36m================================ Testing: $1\033[0m"
echo "\033[1;36m================================\033[0m"

set -x
pwd
cp ci/envs/$1.cookiecutterrc ~/.cookiecutterrc
cat ~/.cookiecutterrc
rm -rf python-nameless
cookiecutter --no-input .
cd python-nameless
git init .
git add -A .
git commit -m "initial."
bumpversion patch
bumpversion minor
bumpversion major
safe_sed 's/sphinx-build -b linkcheck/#/' tox.ini
tox
