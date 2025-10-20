# LightMD User Guide

Welcome to **LightMD** - a lightweight markdown editor designed specifically for creating AI instruction documents, PRDs, and agent descriptions.

---

## What is LightMD?

LightMD is a specialized markdown text editor built to help you write high-quality instructions for AI tools and language models. It combines:
- Clean, distraction-free writing environment
- Intelligent variable tracking and highlighting
- Built-in AI assistant (Claude) for document creation and editing
- Professional templates for common AI instruction formats
- Real-time spell checking to catch errors

---

## Quick Start

### 1. Using Templates
The **Templates** menu provides pre-built templates for common use cases:
- **Agent**: AI agent system prompts and instructions
- **PRD**: Prompt Requirements Documents
- **CodeReview**: Structured code review guidelines
- **DataAnalysis**: Data analysis instruction frameworks
- **APIDocumentation**: API documentation templates
- **TestPlan**: Testing strategy templates
- **TechnicalSpec**: Technical specification documents
- **UserStory**: Agile user stories with acceptance criteria
- **BugReport**: Bug documentation templates
- **MeetingSummary**: Meeting notes with action items
- **ResearchSummary**: Research findings and insights
- **RefactoringPlan**: Code refactoring strategy

**To use a template:**
1. Click **Templates** in the menu bar
2. Select your desired template
3. The template loads as a new unsaved document
4. Customize it for your needs and save with a new filename

### 2. Working with Variables

Variables are placeholders in your document that can be dynamically replaced. LightMD automatically detects and tracks them.

**Variable Format:** `{{variable_name}}`

**Rules for Variables:**
- Must be enclosed in double curly braces: `{{}}`
- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Case-insensitive: use any naming style you prefer

**Valid Examples:**
- `{{USER_NAME}}` - all caps (traditional style)
- `{{userName}}` - camelCase
- `{{user_name}}` - snake_case
- `{{apiKey123}}` - with numbers
- `{{_privateVar}}` - starting with underscore

**Invalid Examples:**
- `{{123user}}` - can't start with a number
- `{{user name}}` - no spaces allowed
- `{{user-name}}` - no hyphens allowed

**Variable Sidebar:**
- All detected variables appear in the right sidebar
- Variables are automatically sorted alphabetically
- Double-click any variable to insert it at your cursor position
- Great for maintaining consistency across your document

### 3. AI Assistant

The built-in AI assistant helps you create, edit, and improve your documents.

**Initial Setup:**
1. Click **"Configure API Key"** button in the AI Assistant panel (bottom right)
2. Enter your Anthropic API key
   - Get a key at: https://console.anthropic.com/
   - Your key is stored locally in `lightmd_config.json`
3. Choose your model from the dropdown:
   - **Haiku 4.5**: Faster, cost-effective for quick tasks
   - **Sonnet 4.5**: More capable, better for complex documents

**What the AI Assistant Knows:**
- **About LightMD**: The AI understands it's helping you use a markdown editor designed for AI instruction documents
- **Your Document**: The AI always has access to your current document content
- **Templates Available**: The AI dynamically knows about ALL templates in the Templates menu (including any custom ones you add!)
- **Standards & Best Practices**: The AI is trained on writing effective AI instructions and PRDs
- **Conversation History**: The AI remembers your last 10 exchanges for context

**How the AI Can Help:**

*Advice & Guidance:*
- "What's the best way to structure a PRD for a chatbot?"
- "What variables should I define for this agent description?"
- "How can I make these instructions clearer?"
- "Is this the right template for my use case?"

*Direct Document Edits:*
The AI can modify your document directly using special commands:
- **REPLACE**: Changes specific text in your document
- **INSERT**: Adds text at your cursor position
- **APPEND**: Adds text to the end

*Example Prompts:*
- "Help me write a system prompt for a customer service agent"
- "Add a section about error handling to this document"
- "Replace the placeholder examples with realistic ones"
- "What's missing from this PRD?"
- "Improve the clarity of the Purpose section"
- "Create a test plan for this feature"

**Tips for Best Results:**
- Be specific about what you want
- Reference sections or variables by name
- Ask clarifying questions if unsure
- Use "Clear Chat" to start fresh conversations

### 4. Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+N** | New file |
| **Ctrl+O** | Open file |
| **Ctrl+S** | Save file |
| **Ctrl+Shift+S** | Save As |
| **Ctrl+X** | Cut |
| **Ctrl+C** | Copy |
| **Ctrl+V** | Paste |
| **Ctrl+T** | Insert table template |
| **Ctrl+D** | Toggle light/dark theme |

### 5. Markdown Features

**Syntax Highlighting:**
- Headings (lines starting with `#`) are highlighted in blue/cyan
- Variables (`{{VARIABLE}}`) are highlighted in orange
- Misspelled words have a colored background

**Insert Table:**
Press **Ctrl+T** to insert a markdown table template:
```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

### 6. Spell Checking

- Real-time spell checking as you type
- Misspelled words are highlighted with a colored background
- Particularly helpful for users with dyslexia
- Variables and markdown syntax are excluded from spell checking

### 7. Themes

Toggle between light and dark themes with **Ctrl+D** or via **Theme** menu.

Your preference is automatically saved to `lightmd_config.json` and persists across sessions.

---

## Best Practices for AI Instructions

When writing instructions for AI tools using LightMD:

### 1. Use Clear Structure
- Start with a descriptive title
- Include metadata (version, author, created date)
- Organize with clear headings and sections

### 2. Define Variables Consistently
- Use meaningful variable names: `{{customer_name}}` not `{{x}}`
- Document what each variable represents
- Use consistent naming conventions throughout

### 3. Be Specific and Actionable
- Clearly state the purpose and goals
- Define expected inputs and outputs
- List any constraints or requirements
- Provide concrete examples

### 4. Include Context
- Explain the "why" behind instructions
- Note any dependencies or prerequisites
- Document assumptions

### 5. Test and Iterate
- Use the AI Assistant to review your instructions
- Ask "What's unclear about this?"
- Request examples or test cases
- Refine based on feedback

---

## Creating Your Own Templates

Want to add custom templates?

1. Create a new `.md` file in the `Templates` folder
2. Name it descriptively (e.g., `ChatbotPrompt.md`, `EmailTemplate.md`)
3. Add your template content with variables and structure
4. Restart LightMD or reopen the Templates menu
5. Your template appears automatically!

**Tips:**
- Start filenames with numbers to control sort order (e.g., `1_Help.md`, `2_MyTemplate.md`)
- Include metadata sections for consistency
- Use `{{VARIABLES}}` as placeholders
- Add comments to guide users

---

## Configuration

LightMD stores preferences in `lightmd_config.json`:
- Theme preference (light/dark)
- Anthropic API key (encrypted storage recommended in production)

---

## Troubleshooting

**AI Assistant not responding?**
- Check that you've configured your API key
- Verify your API key is valid at console.anthropic.com
- Check your internet connection

**Variables not highlighting?**
- Ensure double curly braces: `{{}}`
- Check that variables start with a letter or underscore
- Variables must not contain spaces or special characters

**Templates not appearing?**
- Verify `.md` files are in the `Templates` folder
- Restart LightMD to refresh the template list

**Spell check highlighting too aggressive?**
- This is normal - it highlights any non-dictionary words
- Technical terms and acronyms may be flagged
- Variables should be automatically excluded

---

## Tips & Tricks

1. **Quick Variable Reuse**: Double-click variables in the sidebar to insert them instantly

2. **Chat Context**: The AI remembers your conversation, so you can refine iteratively
   - "Now make it more concise"
   - "Add error handling to that section"

3. **Template Customization**: Load a template, customize it, then save as your own template file

4. **Version Control**: Save your documents in a git repository to track changes over time

5. **Keyboard Shortcuts**: Learn the shortcuts - they make editing much faster

6. **AI Model Selection**:
   - Use **Haiku 4.5** for quick questions and simple edits
   - Use **Sonnet 4.5** for complex document creation and analysis

7. **Clear Chat**: Use "Clear Chat" when switching to a completely different topic or document

---

## Questions?

If you have questions while using LightMD:
1. Ask the AI Assistant! It understands the tool and can help
2. Review this Help document
3. Check the README.md in the installation folder
4. Experiment - the tool autosaves prompts you before losing work

---

**Version**: 1.0
**Last Updated**: 2025-10-20

Happy writing! 📝
