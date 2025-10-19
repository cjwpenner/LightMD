"""
LightMD - Lightweight Markdown Editor
A simple WYSIWYG-style markdown editor for creating AI instruction documents
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font as tkfont
import re
from spellchecker import SpellChecker
import os
import glob
import json


class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("LightMD - Markdown Editor")
        self.root.geometry("1200x800")

        # Current file tracking
        self.current_file = None
        self.is_modified = False

        # Templates directory
        self.templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Templates")

        # Config file path
        self.config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lightmd_config.json")

        # Load user preferences
        self.load_preferences()

        # Spell checker
        self.spell_checker = SpellChecker()

        # Color schemes
        self.themes = {
            'light': {
                'bg': '#FFFFFF',
                'fg': '#000000',
                'sidebar_bg': '#F0F0F0',
                'sidebar_fg': '#000000',
                'select_bg': '#0078D7',
                'select_fg': '#FFFFFF',
                'heading_fg': '#0066CC',
                'variable_fg': '#CC6600',
                'spell_error_bg': '#FFE6E6'
            },
            'dark': {
                'bg': '#1E1E1E',
                'fg': '#D4D4D4',
                'sidebar_bg': '#252526',
                'sidebar_fg': '#CCCCCC',
                'select_bg': '#094771',
                'select_fg': '#FFFFFF',
                'heading_fg': '#4FC1FF',
                'variable_fg': '#FFAB70',
                'spell_error_bg': '#4A1F1F'
            }
        }

        self.setup_ui()
        self.apply_theme()
        self.bind_events()

        # Start spell checking after a delay
        self.spell_check_id = None

    def setup_ui(self):
        """Setup the user interface"""
        # Menu Bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Insert Table", command=self.insert_table, accelerator="Ctrl+T")

        # Insert Menu (for templates)
        self.insert_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Insert", menu=self.insert_menu)
        self.populate_templates_menu()

        # Theme Menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Toggle Light/Dark", command=self.toggle_theme, accelerator="Ctrl+D")

        # Main container
        main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Editor Frame (left side)
        editor_frame = ttk.Frame(main_container)
        main_container.add(editor_frame, weight=4)

        # Text Editor with scrollbar
        text_scroll = ttk.Scrollbar(editor_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_editor = tk.Text(
            editor_frame,
            wrap=tk.WORD,
            undo=True,
            font=('Consolas', 11),
            yscrollcommand=text_scroll.set,
            padx=10,
            pady=10
        )
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scroll.config(command=self.text_editor.yview)

        # Variables Sidebar (right side)
        sidebar_frame = ttk.Frame(main_container)
        main_container.add(sidebar_frame, weight=1)

        sidebar_label = ttk.Label(sidebar_frame, text="Variables", font=('Arial', 10, 'bold'))
        sidebar_label.pack(pady=5)

        # Variables listbox
        var_scroll = ttk.Scrollbar(sidebar_frame)
        var_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.variables_listbox = tk.Listbox(
            sidebar_frame,
            yscrollcommand=var_scroll.set,
            font=('Consolas', 10)
        )
        self.variables_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        var_scroll.config(command=self.variables_listbox.yview)

        # Status Bar
        self.status_bar = ttk.Label(
            self.root,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure text tags for syntax highlighting
        self.text_editor.tag_configure('heading', foreground='#0066CC', font=('Consolas', 11, 'bold'))
        self.text_editor.tag_configure('variable', foreground='#CC6600', font=('Consolas', 11, 'bold'))
        self.text_editor.tag_configure('spell_error', background='#FFE6E6')

    def bind_events(self):
        """Bind keyboard shortcuts and events"""
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_file_as())
        self.root.bind('<Control-x>', lambda e: self.cut_text())
        self.root.bind('<Control-c>', lambda e: self.copy_text())
        self.root.bind('<Control-v>', lambda e: self.paste_text())
        self.root.bind('<Control-t>', lambda e: self.insert_table())
        self.root.bind('<Control-d>', lambda e: self.toggle_theme())

        # Track modifications
        self.text_editor.bind('<<Modified>>', self.on_text_modified)
        self.text_editor.bind('<KeyRelease>', self.on_key_release)

        # Variable insertion on double-click
        self.variables_listbox.bind('<Double-Button-1>', self.insert_variable_from_sidebar)

        # Close window event
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

    def on_text_modified(self, event=None):
        """Handle text modification"""
        if self.text_editor.edit_modified():
            self.is_modified = True
            self.update_title()
            self.text_editor.edit_modified(False)

    def on_key_release(self, event=None):
        """Handle key release for syntax highlighting and spell check"""
        # Cancel previous spell check if scheduled
        if self.spell_check_id:
            self.root.after_cancel(self.spell_check_id)

        # Schedule new spell check after 500ms of inactivity
        self.spell_check_id = self.root.after(500, self.update_highlighting)

    def update_highlighting(self):
        """Update syntax highlighting and spell checking"""
        self.highlight_syntax()
        self.update_variables_list()
        self.check_spelling()

    def highlight_syntax(self):
        """Highlight markdown syntax"""
        # Remove existing tags
        self.text_editor.tag_remove('heading', '1.0', tk.END)
        self.text_editor.tag_remove('variable', '1.0', tk.END)

        content = self.text_editor.get('1.0', tk.END)

        # Highlight headings
        for match in re.finditer(r'^#{1,6}\s+.+$', content, re.MULTILINE):
            start_idx = self.text_editor.index(f'1.0 + {match.start()} chars')
            end_idx = self.text_editor.index(f'1.0 + {match.end()} chars')
            self.text_editor.tag_add('heading', start_idx, end_idx)

        # Highlight variables
        for match in re.finditer(r'\{\{[A-Z_][A-Z0-9_]*\}\}', content):
            start_idx = self.text_editor.index(f'1.0 + {match.start()} chars')
            end_idx = self.text_editor.index(f'1.0 + {match.end()} chars')
            self.text_editor.tag_add('variable', start_idx, end_idx)

    def update_variables_list(self):
        """Update the variables sidebar"""
        content = self.text_editor.get('1.0', tk.END)
        variables = set(re.findall(r'\{\{([A-Z_][A-Z0-9_]*)\}\}', content))

        # Update listbox
        self.variables_listbox.delete(0, tk.END)
        for var in sorted(variables):
            self.variables_listbox.insert(tk.END, f'{{{{{var}}}}}')

    def check_spelling(self):
        """Check spelling and highlight errors"""
        # Remove existing spell error tags
        self.text_editor.tag_remove('spell_error', '1.0', tk.END)

        content = self.text_editor.get('1.0', tk.END)

        # Extract words (exclude variables and markdown syntax)
        words_with_positions = []
        for match in re.finditer(r'\b[a-zA-Z]+\b', content):
            word = match.group()
            # Skip if part of a variable or heading marker
            start_pos = match.start()
            if start_pos > 0 and content[start_pos-1:start_pos+len(word)+1] in ['{{', '}}']:
                continue
            words_with_positions.append((word, match.start(), match.end()))

        # Check spelling
        for word, start, end in words_with_positions:
            if word.lower() not in self.spell_checker:
                start_idx = self.text_editor.index(f'1.0 + {start} chars')
                end_idx = self.text_editor.index(f'1.0 + {end} chars')
                self.text_editor.tag_add('spell_error', start_idx, end_idx)

    def insert_variable_from_sidebar(self, event=None):
        """Insert variable at cursor position when clicked in sidebar"""
        selection = self.variables_listbox.curselection()
        if selection:
            variable = self.variables_listbox.get(selection[0])
            self.text_editor.insert(tk.INSERT, variable)
            self.text_editor.focus_set()

    def new_file(self):
        """Create a new file"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Save Changes",
                "Do you want to save changes to the current file?"
            )
            if response:  # Yes
                self.save_file()
            elif response is None:  # Cancel
                return

        self.text_editor.delete('1.0', tk.END)
        self.current_file = None
        self.is_modified = False
        self.update_title()
        self.update_variables_list()

    def open_file(self):
        """Open an existing file"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Save Changes",
                "Do you want to save changes to the current file?"
            )
            if response:
                self.save_file()
            elif response is None:
                return

        file_path = filedialog.askopenfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_editor.delete('1.0', tk.END)
                    self.text_editor.insert('1.0', content)
                    self.current_file = file_path
                    self.is_modified = False
                    self.update_title()
                    self.update_highlighting()
                    self.status_bar.config(text=f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")

    def save_file(self):
        """Save the current file"""
        if self.current_file:
            try:
                content = self.text_editor.get('1.0', tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.is_modified = False
                self.update_title()
                self.status_bar.config(text=f"Saved: {self.current_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
        else:
            self.save_file_as()

    def save_file_as(self):
        """Save the file with a new name"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )

        if file_path:
            self.current_file = file_path
            self.save_file()

    def cut_text(self):
        """Cut selected text"""
        try:
            self.text_editor.event_generate("<<Cut>>")
        except:
            pass
        return "break"

    def copy_text(self):
        """Copy selected text"""
        try:
            self.text_editor.event_generate("<<Copy>>")
        except:
            pass
        return "break"

    def paste_text(self):
        """Paste text from clipboard"""
        try:
            self.text_editor.event_generate("<<Paste>>")
        except:
            pass
        return "break"

    def insert_table(self):
        """Insert a markdown table template"""
        table_template = """| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
"""
        self.text_editor.insert(tk.INSERT, table_template)

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme()
        self.save_preferences()

    def apply_theme(self):
        """Apply the current theme colors"""
        theme = self.themes['dark' if self.is_dark_theme else 'light']

        # Apply to text editor
        self.text_editor.config(
            bg=theme['bg'],
            fg=theme['fg'],
            selectbackground=theme['select_bg'],
            selectforeground=theme['select_fg'],
            insertbackground=theme['fg']
        )

        # Apply to variables listbox
        self.variables_listbox.config(
            bg=theme['sidebar_bg'],
            fg=theme['sidebar_fg'],
            selectbackground=theme['select_bg'],
            selectforeground=theme['select_fg']
        )

        # Update syntax highlighting tags
        self.text_editor.tag_configure('heading', foreground=theme['heading_fg'])
        self.text_editor.tag_configure('variable', foreground=theme['variable_fg'])
        self.text_editor.tag_configure('spell_error', background=theme['spell_error_bg'])

        # Re-apply highlighting
        self.update_highlighting()

    def update_title(self):
        """Update window title"""
        file_name = os.path.basename(self.current_file) if self.current_file else "Untitled"
        modified_marker = "*" if self.is_modified else ""
        self.root.title(f"LightMD - {file_name}{modified_marker}")

    def load_preferences(self):
        """Load user preferences from config file"""
        default_preferences = {
            'theme': 'light'
        }

        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    preferences = json.load(f)
                    self.is_dark_theme = preferences.get('theme', 'light') == 'dark'
            else:
                self.is_dark_theme = False
        except Exception as e:
            print(f"Error loading preferences: {e}")
            self.is_dark_theme = False

    def save_preferences(self):
        """Save user preferences to config file"""
        preferences = {
            'theme': 'dark' if self.is_dark_theme else 'light'
        }

        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(preferences, f, indent=2)
        except Exception as e:
            print(f"Error saving preferences: {e}")

    def get_templates(self):
        """Get all markdown templates from the Templates directory"""
        if not os.path.exists(self.templates_dir):
            return []

        template_files = glob.glob(os.path.join(self.templates_dir, "*.md"))
        templates = []

        for template_path in template_files:
            template_name = os.path.splitext(os.path.basename(template_path))[0]
            templates.append((template_name, template_path))

        return sorted(templates)

    def populate_templates_menu(self):
        """Populate the Insert menu with available templates"""
        # Clear existing menu items
        self.insert_menu.delete(0, tk.END)

        templates = self.get_templates()

        if not templates:
            self.insert_menu.add_command(label="No templates found", state=tk.DISABLED)
        else:
            for template_name, template_path in templates:
                self.insert_menu.add_command(
                    label=template_name,
                    command=lambda path=template_path: self.load_template(path)
                )

    def load_template(self, template_path):
        """Load a template into the editor"""
        # Check if current document has unsaved changes
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Save Changes",
                "Do you want to save changes to the current file?"
            )
            if response:  # Yes
                self.save_file()
            elif response is None:  # Cancel
                return

        try:
            with open(template_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_editor.delete('1.0', tk.END)
                self.text_editor.insert('1.0', content)

                # Clear current file - this is a new document based on template
                self.current_file = None
                self.is_modified = True  # Mark as modified since it's unsaved
                self.update_title()
                self.update_highlighting()

                template_name = os.path.basename(template_path)
                self.status_bar.config(text=f"Template loaded: {template_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load template:\n{str(e)}")

    def exit_app(self):
        """Exit the application"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Save Changes",
                "Do you want to save changes before exiting?"
            )
            if response:
                self.save_file()
                self.root.destroy()
            elif response is False:
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
