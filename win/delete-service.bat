@echo off
chcp 65001 >nul

set dir=%~dp0

rem 设置服务的名称
set SERVICE_NAME=bt-box

rem 创建服务
sc delete %SERVICE_NAME%

echo 删除 %SERVICE_NAME% 服务。

pause