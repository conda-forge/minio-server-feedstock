@echo off
call run_conda_forge_build_setup
if %errorlevel% neq 0 exit /b %errorlevel%

:: Load the CI activation variables before deciding whether to run package tests.
call "%CONDA_PREFIX%\condabin\conda.bat" activate "%CONDA_PREFIX%"
if %errorlevel% neq 0 exit /b %errorlevel%
