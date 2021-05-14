#!/bin/bash -eux
shopt -s xpg_echo

if [[ -z "$1" ]]; then
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
cat ci/envs/$1.cookiecutterrc
rm -rf python-nameless
cookiecutter --no-input --config-file=ci/envs/$1.cookiecutterrc .
cd python-nameless
git init .
sed -i 's/0.0.0/0.0.1/' CHANGELOG.rst
git add -A .
git commit -m "Initial."
bumpversion --config-file=.bumpversion.cfg patch || tbump --no-push --non-interactive 0.0.1
sed -i 's/0.0.1/0.1.0/' CHANGELOG.rst
git add -A CHANGELOG.rst
git commit -m "Update changelog."
bumpversion --config-file=.bumpversion.cfg minor || tbump --no-push --non-interactive 0.1.0
sed -i 's/0.1.0/1.0.0/' CHANGELOG.rst
git add -A CHANGELOG.rst
git commit -m "Update changelog."
bumpversion --config-file=.bumpversion.cfg major || tbump --no-push --non-interactive 1.0.0
safe_sed 's/sphinx-build -b linkcheck/#/' tox.ini
for name in py36 py37 py38; do
  for env in $name ${name}-cover ${name}-nocov; do
    safe_sed "s/,$env,/,/" tox.ini
    safe_sed "s/$env,//" tox.ini
    safe_sed "s/,$env//" tox.ini
  done
done
