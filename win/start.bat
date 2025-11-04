@echo off
chcp 65001 >nul

if "%1" == "h" goto begin 
start mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
 
set dir=%~dp0

@REM cd %~dp0

set exeName=bt-box.exe
rem 检查进程是否运行
tasklist /FI "IMAGENAME eq %exeName%" 2>NUL | find /I /N "%exeName%">NUL
if "%ERRORLEVEL%"=="0" (
    echo %exeName% is running.
) else (
    echo %exeName% is not running.
	start /b %exeName%
)
