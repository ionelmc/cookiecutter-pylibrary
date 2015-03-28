param (
    [string]$target=$(throw "Usage: {0} env-name" -f $MyInvocation.MyCommand.Name)
)
write-host "================================" -foregroundcolor "magenta"
write-host "================================ Testing: $target" -foregroundcolor "magenta"
write-host "================================" -foregroundcolor "magenta"

$rcpath=("{0}{1}\\.cookiecutterrc" -f $Env:HOMEDRIVE,$Env:HOMEPATH)
cat "ci/envs/$target.cookiecutterrc" | Set-Content -Path $rcpath
cat $rcpath
Remove-Item -Recurse -Force python-nameless
c:\\python27\\Scripts\\cookiecutter --no-input .
cd python-nameless
git init .
git config core.safecrlf false
git add -A .
git commit -m "initial."
(Get-Content -Path "tox.ini") -replace "sphinx-build -b linkcheck","#" | Set-Content -Path "tox.ini"
c:\\python27\\Scripts\\tox --skip-missing-interpreters
