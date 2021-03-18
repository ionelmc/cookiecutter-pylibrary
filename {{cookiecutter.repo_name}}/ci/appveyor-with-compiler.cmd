SET COMMAND_TO_RUN=%*

IF "%PYTHON_VERSION%"=="2.7" GOTO legacy
GOTO main

:legacy
powershell -Command "Invoke-WebRequest https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi -OutFile VCForPython27.msi"
msiexec /i VCForPython27.msi /quiet /qn /norestart

:main
ECHO Executing: %COMMAND_TO_RUN%
CALL %COMMAND_TO_RUN% || EXIT 1
