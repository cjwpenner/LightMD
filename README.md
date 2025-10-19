# LightMD - Lightweight Markdown Editor

A simple, lightweight WYSIWYG-style markdown editor designed for creating AI instruction documents and PRDs.

## Features

- **Clean Interface**: Simple text editor with markdown syntax highlighting
- **Variable Tracking**: Automatically detects and lists variables in `{{VARIABLE}}` format
- **Spell Checking**: Real-time spell checking with error highlighting (great for dyslexia support)
- **Light/Dark Themes**: Toggle between light and dark modes
- **File Operations**: New, Open, Save, Save As
- **Edit Tools**: Cut, Copy, Paste, Insert Table
- **Keyboard Shortcuts**: All major functions have keyboard shortcuts

## Installation

1. Make sure Python 3.7+ is installed on your system
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running LightMD

### Option 1: Double-click the batch file
Simply double-click `run_lightmd.bat` to start the application.

### Option 2: Create a desktop shortcut
Double-click `create_shortcut.vbs` to create a desktop shortcut for easy access.

### Option 3: Run from command line
```bash
python lightmd.py
```

## Keyboard Shortcuts

- **Ctrl+N**: New file
- **Ctrl+O**: Open file
- **Ctrl+S**: Save file
- **Ctrl+Shift+S**: Save As
- **Ctrl+X**: Cut
- **Ctrl+C**: Copy
- **Ctrl+V**: Paste
- **Ctrl+T**: Insert table template
- **Ctrl+D**: Toggle dark/light theme

## Usage

### Variables
Variables are automatically detected when you type them in the format `{{VARIABLE_NAME}}`. They must:
- Start with a letter or underscore
- Contain only uppercase letters, numbers, and underscores
- Be enclosed in double curly braces

All detected variables appear in the sidebar. Double-click a variable to insert it at your cursor position.

### Spell Checking
Misspelled words are highlighted with a colored background. The spell checker runs automatically as you type.

### Markdown Features
- Headings are highlighted (lines starting with `#`, `##`, etc.)
- Variables are highlighted in a distinct color
- Insert table templates with Ctrl+T or Edit > Insert Table

## Future Enhancements

Planned features include:
- AI integration window for LLM API calls
- Custom variable templates
- Export to PDF
- Preview pane with rendered markdown

## License

Free to use and modify.
