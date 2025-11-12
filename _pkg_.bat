

pip install pyinstaller

@echo off
set appName=pyside6-app

:: 直接使用变量
echo app name ==>: %appName%

@REM pyinstaller --onefile app.py
@REM pyinstaller --onefile -F -w app.py
pyinstaller --noconfirm --onedir -w --name %appName% app.py

copy .\conf.json .\dist\%appName%\
@REM move .\dist\app.exe .\dist\%appName%.exe
