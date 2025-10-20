# Bug Report Template
Detailed bug documentation for effective troubleshooting and resolution.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
bug_id: [BUG-123, JIRA-456, etc.]
severity: [critical | high | medium | low]
priority: [P0 | P1 | P2 | P3]
status: [new | investigating | in-progress | resolved | closed]
---

## Summary
[One-line description of the bug]

## Environment
- **Application Version**: {{VERSION}}
- **Environment**: [Production | Staging | Development | Local]
- **Operating System**: [Windows 11, macOS 14, Ubuntu 22.04, etc.]
- **Browser/Client**: [Chrome 120, Firefox 121, Mobile Safari, etc.]
- **Device**: [Desktop, iPhone 15, Samsung Galaxy S23, etc.]
- **User Role**: [Admin, Customer, Guest, etc.]

## Steps to Reproduce
1. [First action]
2. [Second action]
3. [Third action]
4. [Observe the bug]

### Example
1. Navigate to `/checkout` page
2. Add 10 items to cart
3. Click "Apply Coupon" button
4. Observe error message

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Reproduction Rate
- [ ] Always (100%)
- [ ] Frequently (>50%)
- [ ] Sometimes (<50%)
- [ ] Rarely (<10%)
- [ ] Unable to reproduce

## Visual Evidence
[Screenshots, screen recordings, or error logs]

```
[Paste error messages, stack traces, or console logs here]
```

## Impact Assessment
**User Impact**: [How many users affected? What functionality is broken?]

**Business Impact**: [Revenue loss? SLA breach? Reputation damage?]

**Workaround Available**: Yes/No
[If yes, describe the workaround]

## Severity Definition
- **Critical**: System down, data loss, security breach
- **High**: Major functionality broken, no workaround
- **Medium**: Functionality impaired, workaround exists
- **Low**: Minor issue, cosmetic problem

## Technical Analysis
**Root Cause Hypothesis**: [Initial theory about what's causing the bug]

**Affected Components**:
- [Component 1]
- [Component 2]

**Related Code**:
- File: `{{FILE_PATH}}`
- Function: `{{FUNCTION_NAME}}`
- Line: {{LINE_NUMBER}}

**Logs/Traces**:
```
[Paste relevant logs here]
```

## Additional Context
- **First Observed**: [Date/time when bug first appeared]
- **Recent Changes**: [Recent deployments, configuration changes, etc.]
- **Related Bugs**: [Links to similar issues]
- **User Session ID**: {{SESSION_ID}}
- **Request ID**: {{REQUEST_ID}}

## Acceptance Criteria for Resolution
- [ ] Bug is no longer reproducible
- [ ] Root cause identified and fixed
- [ ] Unit tests added to prevent regression
- [ ] Deployed to production
- [ ] Verified by QA
- [ ] Verified by reporter

## Investigation Notes
[Space for developers to document their investigation]

**Findings**:
- [Investigation finding 1]
- [Investigation finding 2]

**Fix Applied**:
[Description of the solution implemented]

**Commit/PR**: [Link to code changes]

## Variables for AI Analysis
| Variable | Value |
|----------|-------|
| {{ERROR_CODE}} | [e.g., 500, ERR_CONNECTION_REFUSED] |
| {{TIMESTAMP}} | [When the bug occurred] |
| {{USER_ID}} | [Affected user identifier] |
| {{REQUEST_PAYLOAD}} | [API request that triggered bug] |

## Questions for AI Assistant
1. What could be causing this error based on the stack trace?
2. Are there similar known issues in this codebase?
3. What are potential root causes given the symptoms?
4. What additional information should I collect?
