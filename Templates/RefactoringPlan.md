# Refactoring Plan Template
Structured approach to improving code quality without changing functionality.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
refactoring_type: [architectural | performance | readability | technical-debt]
risk_level: [low | medium | high]
target_model: [OpenAI GPT-4o, Claude Sonnet, etc.]
---

## Refactoring Objective
[What are we improving? Why is this refactoring needed now?]

## Current State Analysis

### Code Smells Identified
- [ ] **Duplicated Code**: [Where and how much]
- [ ] **Long Methods/Functions**: [Examples]
- [ ] **Large Classes**: [Examples]
- [ ] **Long Parameter Lists**: [Examples]
- [ ] **Divergent Change**: [One class changes for multiple reasons]
- [ ] **Shotgun Surgery**: [One change requires many small edits]
- [ ] **Feature Envy**: [Method uses another class more than its own]
- [ ] **Poor Naming**: [Unclear or misleading names]
- [ ] **Dead Code**: [Unused functions, variables]
- [ ] **Comments Explaining Bad Code**: [Should rewrite instead]

### Technical Debt Assessment
**Debt Type**: [Deliberate | Accidental | Outdated]
**Age**: [How long has this existed?]
**Impact**: [Performance, maintainability, security]
**Interest**: [Cost of not fixing: bugs, slowdowns, developer time]

### Metrics (Before Refactoring)
- **Lines of Code**: {{LOC}}
- **Cyclomatic Complexity**: {{COMPLEXITY}}
- **Test Coverage**: {{COVERAGE_PERCENT}}%
- **Code Duplication**: {{DUPLICATION_PERCENT}}%
- **Performance Benchmark**: {{BENCHMARK}} (e.g., 500ms response time)

## Scope

### Files/Components to Refactor
1. `{{FILE_PATH_1}}` - [Brief description of changes]
2. `{{FILE_PATH_2}}` - [Brief description of changes]
3. `{{MODULE_NAME}}` - [Brief description of changes]

### Out of Scope
[What we will NOT change in this refactoring]

## Proposed Changes

### Change 1: {{CHANGE_TITLE}}
**Current Code**:
```{{LANGUAGE}}
[Paste problematic code snippet]
```

**Refactored Code**:
```{{LANGUAGE}}
[Paste improved code snippet]
```

**Justification**: [Why this is better]

**Impact**: [What this affects, potential risks]

---

### Change 2: {{CHANGE_TITLE}}
[Repeat structure above]

## Refactoring Patterns to Apply
- [ ] **Extract Method**: Break down large functions
- [ ] **Extract Class**: Split large classes
- [ ] **Rename**: Improve variable/function names
- [ ] **Move Method**: Relocate to more appropriate class
- [ ] **Replace Conditional with Polymorphism**: Use inheritance
- [ ] **Introduce Parameter Object**: Group parameters
- [ ] **Remove Dead Code**: Delete unused code
- [ ] **Simplify Conditional**: Make logic clearer
- [ ] **Replace Magic Numbers**: Use named constants

## Testing Strategy

### Pre-Refactoring Tests
- [ ] Run full test suite and confirm all tests pass
- [ ] Document current test coverage: {{PERCENT}}%
- [ ] Capture performance benchmarks
- [ ] Create regression test suite

### During Refactoring
- [ ] Run tests after each change
- [ ] Add new tests for edge cases
- [ ] Maintain or improve test coverage

### Post-Refactoring Validation
- [ ] All existing tests still pass
- [ ] New tests pass
- [ ] Performance benchmarks met or improved
- [ ] Code review completed

## Implementation Plan

### Phase 1: Preparation
- [ ] Create feature branch: `refactor/{{BRANCH_NAME}}`
- [ ] Ensure test coverage is adequate
- [ ] Back up current code/database
- [ ] Communicate plan to team
- **Duration**: {{ESTIMATE}}

### Phase 2: Incremental Changes
- [ ] Change 1: [Description]
- [ ] Change 2: [Description]
- [ ] Change 3: [Description]
- [ ] Commit after each successful change
- **Duration**: {{ESTIMATE}}

### Phase 3: Validation
- [ ] Run full test suite
- [ ] Performance testing
- [ ] Code review
- [ ] Update documentation
- **Duration**: {{ESTIMATE}}

### Phase 4: Deployment
- [ ] Merge to main branch
- [ ] Deploy to staging
- [ ] Monitor for issues
- [ ] Deploy to production
- **Duration**: {{ESTIMATE}}

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Breaking existing functionality | Med | High | Comprehensive test suite |
| Performance regression | Low | Med | Benchmark before/after |
| Merge conflicts | High | Low | Frequent commits, communicate |
| Scope creep | Med | Med | Strict scope definition |

## Rollback Plan
**Trigger**: [When to rollback: critical bugs, performance degradation > X%]

**Steps**:
1. [Immediate action]
2. [Revert changes]
3. [Verify system stability]

## Success Criteria

### Quantitative
- [ ] Test coverage maintained or improved: {{TARGET_PERCENT}}%
- [ ] Code complexity reduced by: {{PERCENT}}%
- [ ] Code duplication reduced by: {{PERCENT}}%
- [ ] Performance improved or maintained: {{BENCHMARK}}
- [ ] Lines of code reduced by: {{PERCENT}}% (optional)

### Qualitative
- [ ] Code is easier to understand
- [ ] Code is easier to test
- [ ] Code is easier to extend
- [ ] Team agrees code quality improved

## Metrics (After Refactoring)
- **Lines of Code**: {{LOC}}
- **Cyclomatic Complexity**: {{COMPLEXITY}}
- **Test Coverage**: {{COVERAGE_PERCENT}}%
- **Code Duplication**: {{DUPLICATION_PERCENT}}%
- **Performance Benchmark**: {{BENCHMARK}}

## Documentation Updates Needed
- [ ] Update README
- [ ] Update API documentation
- [ ] Update architecture diagrams
- [ ] Update code comments
- [ ] Update team wiki/knowledge base

## AI Assistant Instructions
Please review the following code and:
1. Identify code smells and technical debt
2. Suggest specific refactoring patterns to apply
3. Prioritize changes by impact and risk
4. Generate refactored code examples
5. Identify potential risks and edge cases

**Code to Refactor**:
```{{LANGUAGE}}
[Paste code here]
```
