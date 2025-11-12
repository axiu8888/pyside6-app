

pip install pyinstaller

@echo off
set appName=pyside6-app

:: 直接使用变量
echo app name ==>: %appName%

@REM pyinstaller --onefile app_single.py
@REM pyinstaller --onefile -F -w app_single.py
pyinstaller --noconfirm --onedir -w --name %appName% app_single.py

copy .\conf.json .\dist\%appName%\
@REM move .\dist\app_single.exe .\dist\%appName%.exe
