# LightMD - Lightweight Markdown Editor

A simple, lightweight WYSIWYG-style markdown editor designed for creating AI instruction documents and PRDs.

## Features

- **Clean Interface**: Simple text editor with markdown syntax highlighting
- **AI Assistant**: Integrated Claude AI chat to help create and edit documents
- **Template System**: Dynamic template insertion from the Templates folder
- **Variable Tracking**: Automatically detects and lists variables in `{{VARIABLE}}` format
- **Spell Checking**: Real-time spell checking with error highlighting (great for dyslexia support)
- **Light/Dark Themes**: Toggle between light and dark modes with persistent preference
- **File Operations**: New, Open, Save, Save As
- **Edit Tools**: Cut, Copy, Paste, Insert Table, Bold, Italics
- **Keyboard Shortcuts**: All major functions have keyboard shortcuts

## Installation

1. Make sure Python 3.7+ is installed on your system
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running LightMD

### Option 1: Double-click the batch file
Simply double-click `run_lightmd.bat` from your file system to start the application.

### Option 2: Create a desktop shortcut
Double-click `create_shortcut.vbs` from your file manager to create a desktop shortcut for easy access.

### Option 3: Run from command line
cd to the LightMD folder and run:
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
- **Ctrl+Z**: Undo
- **Ctrl+B**: Bold (adds "**" at the beginning and end of the highlighted section)
- **Ctrl+I**: Italics (adds "*" at the beginning and end of the highlighted section)
- **Ctrl+T**: Insert table template
- **Ctrl+D**: Toggle dark/light theme

## Usage

### Templates
The **Templates** menu dynamically shows all `.md` files from the `Templates` folder. Simply:
1. Click **Templates** in the menu bar
2. Select a template (e.g., Agent, PRD)
3. The template content loads into a new document
4. Save with a new filename - your original template remains unchanged

To add your own templates:
- Place any `.md` file in the `Templates` folder
- Restart LightMD or reopen the Templates menu
- Your new templates will appear automatically

### Variables
Variables are automatically detected when you type them in the format `{{variable_name}}`. They must:
- Be enclosed in double curly braces `{{}}`
- Start with a letter (a-z, A-Z) or underscore
- Contain only letters, numbers, and underscores (no spaces or hyphens)
- Can use any naming style: `{{USER_NAME}}`, `{{userName}}`, `{{user_name}}`

All detected variables appear in the sidebar. Double-click a variable to insert it at your cursor position.

### Spell Checking
Misspelled words are highlighted with a colored background. The spell checker runs automatically as you type. The Dictionary is not very large, but you can add words to it to make it more tuned to your use case.

### Markdown Features
- Headings are highlighted (lines starting with `#`, `##`, etc.)
- Variables are highlighted in a distinct color
- Insert table templates with Ctrl+T or Edit > Insert Table

### AI Assistant
The integrated AI assistant helps you create and edit markdown documents:

**Getting Started**:
1. Click "Configure API Key" in the AI Assistant panel
2. Enter your Anthropic API key (get one at https://console.anthropic.com/)
3. Select your preferred model: Claude Sonnet 4.5  or Claude Haiku 4.5 (less expensive, default)
4. Start chatting!
5. For extended instructions to the AI, you can simply write your query in the main document and then in the AI chat input ask the LLM to execute the instructions in the document.

**What the AI Can Do**:
- **Provide Advice**: Ask questions about your document structure, content, or best practices
- **Ask Clarifying Questions**: The AI helps you think through your requirements
- **Direct Edits**: The AI can directly modify your document using special commands:
  - REPLACE: Changes specific text in your document
  - INSERT: Adds text at your cursor position
  - APPEND: Adds text to the end of your document

**Context Awareness**:
- The AI always has access to your current document content
- Chat history is maintained for contextual conversations
- Ask about variables, structure, or request edits to specific sections

**Example Prompts**:
- "Help me structure a PRD for a markdown editor"
- "Add a section about error handling"
- "Improve the clarity of the introduction"
- "What variables should I define for this agent description?"

### Theme Preferences
Your theme choice (light or dark) is automatically saved to `lightmd_config.json` and will persist across sessions. Simply toggle the theme once, and LightMD will remember your preference the next time you open it.

## Future Enhancements

Planned features include:
- Export to PDF
- Extended testing and enhancmeent of the AI commands for more complex document transformations

## Third-Party Libraries

LightMD is built using the following open source libraries:

- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - Python's standard GUI library (part of Python Standard Library)
  - Used for: Application interface and windowing
  - License: Python Software Foundation License

- **[pyspellchecker](https://github.com/barrust/pyspellchecker)** (v0.7.2) by Tyler Barrus
  - Used for: Real-time spell checking functionality
  - License: MIT License

- **[Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)** (v0.40.0+)
  - Used for: Claude AI integration for the AI Assistant feature
  - License: MIT License

- **[Pillow (PIL Fork)](https://python-pillow.org/)** (v10.2.0)
  - Used for: Image processing capabilities
  - License: HPND License (Historical Permission Notice and Disclaimer)

We are grateful to the maintainers and contributors of these projects for their excellent work.

## License

LightMD is dual-licensed:

### Open Source License (GPLv3)
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software under the terms of GPLv3, which requires that derivative works also be open-source and licensed under GPLv3.

### Commercial License
If you wish to use LightMD in a proprietary or closed-source application without the requirements of GPLv3, a commercial license is available. See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) for more information.

**Contact for commercial licensing:**
- Email: marie@thyrel.co.uk
- Website: www.thyrel.co.uk

### Why Dual Licensing?
- **Open Source (GPLv3)**: Encourages community contributions and showcases innovation
- **Commercial**: Allows businesses to integrate LightMD without open-source obligations while supporting ongoing development
