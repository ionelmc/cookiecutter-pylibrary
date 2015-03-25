#!/bin/bash -eE
:<<"::batch"
@echo off
powershell -ExecutionPolicy ByPass -File ci\test.ps1 %*
goto :end
::batch
ci/test.sh $*
exit $?
:<<"::done"
:end
::done
