@echo off
chcp 65001 >nul

set dir=%~dp0

rem 设置 NSSM 的路径
set NSSM_PATH=%dir%nssm.exe

rem 设置服务的名称
set SERVICE_NAME=bt-box

rem 设置要作为服务运行的可执行文件或脚本的路径
set APP_PATH=%dir%start.bat

rem 创建服务
%NSSM_PATH% install %SERVICE_NAME% %APP_PATH%

rem 设置服务为自动启动
%NSSM_PATH% set %SERVICE_NAME% Start SERVICE_AUTO_START

rem 启动服务
%NSSM_PATH% start %SERVICE_NAME%

echo 服务 %SERVICE_NAME% 已创建并启动。

pause