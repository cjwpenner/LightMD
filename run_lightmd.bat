@echo off
REM LightMD Launcher Script
cd /d "%~dp0"
python lightmd.py
if errorlevel 1 (
    echo.
    echo Error: Failed to start LightMD
    echo Please make sure Python is installed and dependencies are installed.
    echo Run: pip install -r requirements.txt
    pause
)
