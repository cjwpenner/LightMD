# User Story Template
Capture feature requirements from the user's perspective.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
story_id: [JIRA-123, US-001, etc.]
priority: [P0 | P1 | P2 | P3]
status: [backlog | in-progress | review | done]
---

## User Story
As a **{{USER_TYPE}}**,
I want to **{{ACTION}}**,
So that **{{BENEFIT}}**.

### Example
As a **customer**,
I want to **save items to a wishlist**,
So that **I can purchase them later without searching again**.

## Context
[Why is this feature needed? What's the business value? What problem does it solve?]

## Acceptance Criteria
Given **{{PRECONDITION}}**,
When **{{ACTION}}**,
Then **{{EXPECTED_RESULT}}**.

### Criteria List
- [ ] **AC-1**: [Specific, testable criterion]
- [ ] **AC-2**: [Specific, testable criterion]
- [ ] **AC-3**: [Specific, testable criterion]

### Example
- [ ] User can click a heart icon on any product page
- [ ] Item appears in "My Wishlist" section
- [ ] User receives confirmation message
- [ ] Wishlist persists across sessions

## User Flow
1. [Step 1: User action]
2. [Step 2: System response]
3. [Step 3: Next user action]
4. [Step 4: Final outcome]

## UI/UX Requirements
- **Mockups**: [Link to Figma, screenshots, or description]
- **Design Notes**: [Specific visual requirements]
- **Responsive**: [Mobile, tablet, desktop considerations]
- **Accessibility**: [WCAG compliance, keyboard navigation, screen readers]

## Technical Notes
- **Estimated Effort**: [Story points or time]
- **Dependencies**: [Other stories, APIs, services]
- **Technical Approach**: [Brief implementation notes]
- **API Changes**: [New endpoints or modifications needed]

## Edge Cases & Error Handling
- [ ] What happens if {{EDGE_CASE_1}}?
- [ ] What happens if {{EDGE_CASE_2}}?
- [ ] How do we handle errors in {{SCENARIO}}?

### Examples
- [ ] What happens if user is not logged in?
- [ ] What happens if item is out of stock?
- [ ] What happens if wishlist is at max capacity?

## Non-Functional Requirements
- **Performance**: [e.g., Action completes in < 1 second]
- **Security**: [e.g., Only authenticated users can access]
- **Scalability**: [e.g., Support 1M wishlists]
- **Analytics**: [e.g., Track wishlist additions and conversions]

## Definition of Done
- [ ] Code complete and peer-reviewed
- [ ] Unit tests written (coverage > {{PERCENT}}%)
- [ ] Integration tests passing
- [ ] UI matches design specs
- [ ] Accessibility requirements met
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] QA signed off
- [ ] Product Owner approved

## Questions & Assumptions
**Questions**:
1. [Unresolved question]
2. [Clarification needed]

**Assumptions**:
- [Assumption 1]
- [Assumption 2]

## Success Metrics
[How will we measure if this feature is successful?]
- Example: "20% of users add items to wishlist within first month"
- Example: "Wishlist users have 2x higher conversion rate"

## Related Stories
- [Link to related user stories]
- [Parent epic or feature]
- [Dependent stories]
