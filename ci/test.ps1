param (
    [string]$target=$(throw "Usage: {0} env-name" -f $MyInvocation.MyCommand.Name)
)
write-host "################################################################################" -foregroundcolor "magenta"
write-host "################################################################################" -foregroundcolor "magenta"
write-host ""
write-host "    Testing: ${Env:USERPROFILE}" -foregroundcolor "magenta"
write-host ""
write-host "################################################################################" -foregroundcolor "magenta"

rmdir /S /Q python-nameless
c:\\python27\\Scripts\\cookiecutter --no-input .
cd python-nameless
git init .
git add .
git commit -m "initial."
(Get-Content -Path "tox.ini") -replace "sphinx-build -b linkcheck","#" | Set-Content -Path "tox.ini"
c:\\python27\\Scripts\\tox --skip-missing-interpreters
