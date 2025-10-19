# Installation Guide for LightMD

## Quick Start

Follow these simple steps to get LightMD running on your Windows machine:

### Step 1: Install Dependencies
Open Command Prompt or PowerShell in the LightMD folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Run LightMD

**Option A: Using the Batch File (Recommended)**
1. Double-click `run_lightmd.bat`
2. The application will start automatically

**Option B: Create Desktop Shortcut**
1. Double-click `create_shortcut.vbs`
2. A shortcut named "LightMD" will appear on your desktop
3. Double-click the desktop shortcut to launch LightMD anytime

**Option C: Run from Command Line**
```bash
python lightmd.py
```

## Troubleshooting

### Python Not Found
If you get an error about Python not being found:
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart your computer
4. Try again

### Dependencies Failed to Install
If pip install fails:
1. Make sure you have internet connection
2. Try running Command Prompt as Administrator
3. Update pip first: `python -m pip install --upgrade pip`
4. Then try installing dependencies again

### Application Won't Start
1. Make sure all dependencies installed successfully
2. Check that you're in the correct folder (C:\Users\Chris\LightMD)
3. Try running from command line to see error messages:
   ```bash
   python lightmd.py
   ```

## Next Steps

Once installed, check out README.md for:
- Feature descriptions
- Keyboard shortcuts
- Usage tips
- Variable syntax

Enjoy using LightMD!
