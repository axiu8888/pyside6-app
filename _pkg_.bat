

pip install pyinstaller

pyinstaller --onefile app.py

@REM pyinstaller --onefile -F -w app.py

copy .\conf.json .\dist\
move .\dist\app.exe .\dist\pyside6-app.exe
