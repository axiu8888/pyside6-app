

pip install pyinstaller

pyinstaller --onefile app_single.py

@REM pyinstaller --onefile -F -w app_single.py

copy .\conf.json .\dist\
move .\dist\app_single.exe .\dist\pyside6-app.exe
