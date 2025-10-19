# [Agent / Prompt Title]  
A short description of what this instruction file does.  

## Metadata
---
version: 1.0
author: [Your Name]
memory: [persistent | none]
created: YYYY-MM-DD
---

## System Prompt
You are [define role, expertise, and style here].  
Your goals are:  
1. [Rule 1]  
2. [Rule 2]  
3. [Rule 3]  

You must never:  
- [Prohibition 1]  
- [Prohibition 2]  

## User Prompt
[Task or request to the model. Be specific about what input it will receive and what it must do.]  

Example:  
“Summarise the following report into 5 executive bullet points, focusing only on economic impacts.”  

## Variables
| Variable         | Description              | Example                  |
|------------------|--------------------------|--------------------------|
| {{VARIABLE_ONE}} | [What it represents]     | Example value            |
| {{VARIABLE_TWO}} | [What it represents]     | Example value            |

## Output Requirements
- Format: [Markdown | JSON | Table | etc.]  
- Structure: [Headings, bullet points, numbered list, etc.]  
- Style: [Concise, formal, plain language, etc.]  
- Constraints: [e.g., “exactly 5 bullet points,” “no speculation,” “max 200 words”]  

## Memory / State
- [ ] Step 1: [description]  
- [ ] Step 2: [description]  
- [ ] Step 3: [description]  