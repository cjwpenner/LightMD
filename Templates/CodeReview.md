# Code Review Template
A structured approach to reviewing code changes with AI assistance.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
review_type: [security | performance | style | architecture | general]
target_model: [OpenAI GPT-4o, Claude Sonnet, etc.]
---

## Purpose
[Define the goal of this code review: security audit, performance optimization, style consistency, architectural assessment, or general quality check]

## Code to Review
```{{LANGUAGE}}
[Paste code here or reference file/PR]
```

## Review Focus Areas
- [ ] **Security**: Vulnerabilities, input validation, authentication/authorization
- [ ] **Performance**: Time complexity, memory usage, database queries
- [ ] **Readability**: Naming, comments, code structure
- [ ] **Maintainability**: DRY principle, modularity, testability
- [ ] **Error Handling**: Edge cases, exceptions, logging
- [ ] **Best Practices**: Language idioms, design patterns

## Specific Questions
1. [Any particular concerns or areas to focus on?]
2. [Example: "Are there any SQL injection vulnerabilities?"]
3. [Example: "Can this be optimized for large datasets?"]

## Context
- **Framework/Stack**: [e.g., React, Django, Node.js]
- **Dependencies**: [Key libraries or versions]
- **Known Issues**: [Any existing bugs or technical debt]

## Output Requirements
- Format: Markdown with severity labels (CRITICAL | HIGH | MEDIUM | LOW)
- Structure:
  1. Summary assessment
  2. Issues found (grouped by category)
  3. Recommendations with code examples
  4. Positive observations
- Style: Constructive, specific, actionable

## Example Output Format
### Summary
[2-3 sentence overview of code quality]

### Issues Found
**CRITICAL**
- Line X: [Issue description and suggested fix]

**MEDIUM**
- Line Y: [Issue description and suggested fix]

### Recommendations
1. [Suggestion with code example]

### Strengths
- [Positive aspects of the code]
