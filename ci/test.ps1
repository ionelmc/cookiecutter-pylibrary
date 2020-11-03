param (
    [string]$target=$(throw "Usage: {0} env-name" -f $MyInvocation.MyCommand.Name)
)
$ErrorActionPreference='Stop'
$PSDefaultParameterValues['*:ErrorAction']='Stop'
function CheckError {
    if (-not $?) {
        throw "Command failed with exit code $?"
    }
}
write-host "================================" -foregroundcolor "magenta"
write-host "================================ Testing: $target" -foregroundcolor "magenta"
write-host "================================" -foregroundcolor "magenta"

$rcpath=("{0}{1}\\.cookiecutterrc" -f $Env:HOMEDRIVE,$Env:HOMEPATH)
cat "ci/envs/$target.cookiecutterrc" | Set-Content -Path $rcpath
cat $rcpath
Remove-Item -Recurse -Force python-nameless
$Env:PATH="$Env:PATH;c:\python27\Scripts"
cookiecutter --version
CheckError
cookiecutter --no-input .
CheckError
cd python-nameless
git init .
CheckError
git config core.safecrlf false
CheckError
git add -A .
CheckError
git commit -m "Initial."
CheckError
(Get-Content -Path "tox.ini") -replace "sphinx-build -b linkcheck","#" | Set-Content -Path "tox.ini"
tox --skip-missing-interpreters
CheckError
