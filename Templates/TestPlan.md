# Test Plan Template
Define comprehensive testing strategy for features or systems.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
test_type: [unit | integration | e2e | performance | security]
target_model: [OpenAI GPT-4o, Claude Sonnet, etc.]
---

## Purpose
[What are we testing and why? What risks are we mitigating?]

## Scope
**In Scope**
- [Feature/component to be tested]
- [Specific functionality]

**Out of Scope**
- [What will NOT be tested]
- [Deferred to future testing]

## Feature/System Under Test
[Brief description or link to requirements]

**Acceptance Criteria**
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

## Test Strategy

### Unit Tests
- **Coverage Target**: {{COVERAGE_PERCENT}}%
- **Focus Areas**:
  - [ ] Individual functions/methods
  - [ ] Edge cases and boundary conditions
  - [ ] Error handling
  - [ ] Mock external dependencies

### Integration Tests
- **Focus Areas**:
  - [ ] API endpoints
  - [ ] Database interactions
  - [ ] External service integrations
  - [ ] Component interactions

### End-to-End Tests
- **User Flows**:
  1. [Critical user journey 1]
  2. [Critical user journey 2]
- **Browsers/Devices**: [Chrome, Firefox, Safari | iOS, Android]

### Performance Tests
- [ ] Load testing ({{CONCURRENT_USERS}} concurrent users)
- [ ] Stress testing (find breaking point)
- [ ] Response time targets: {{MAX_RESPONSE_TIME}}ms

### Security Tests
- [ ] Authentication/Authorization
- [ ] Input validation
- [ ] SQL injection
- [ ] XSS vulnerabilities
- [ ] CSRF protection

## Test Cases

### TC-001: [Test Case Title]
**Priority**: High | Medium | Low
**Type**: Functional | Non-functional

**Preconditions**:
- [Setup requirements]

**Steps**:
1. [Action]
2. [Action]
3. [Action]

**Expected Result**:
[What should happen]

**Actual Result**:
[To be filled during execution]

**Status**: Pass | Fail | Blocked | Not Run

---

### TC-002: [Test Case Title]
[Repeat format above]

## Test Data Requirements
| Data Type | Description | Example |
|-----------|-------------|---------|
| {{USER_DATA}} | Valid user account | john@example.com |
| {{INVALID_INPUT}} | Test error handling | null, empty strings |
| {{EDGE_CASES}} | Boundary values | 0, -1, MAX_INT |

## Test Environment
- **Environment**: [Dev | Staging | Production-like]
- **Database**: [Type and version]
- **Dependencies**: [External services, APIs]
- **Test Tools**: [pytest, Jest, Selenium, JMeter, etc.]

## Entry Criteria
- [ ] Code complete and in test environment
- [ ] Test data prepared
- [ ] Test environment configured
- [ ] Dependencies available/mocked

## Exit Criteria
- [ ] All high-priority tests passed
- [ ] Code coverage meets target
- [ ] No critical/high-severity bugs open
- [ ] Performance benchmarks met

## Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk description] | High/Med/Low | [How to address] |

## Deliverables
- [ ] Test cases documentation
- [ ] Test execution report
- [ ] Bug reports (if any)
- [ ] Code coverage report
- [ ] Performance test results

## Success Criteria
[How do we know testing is complete and the feature is ready to ship?]
