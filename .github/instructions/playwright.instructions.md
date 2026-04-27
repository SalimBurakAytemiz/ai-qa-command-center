# Playwright Instructions

## Purpose

Use these instructions when creating, reviewing, or improving Playwright automation candidates, Playwright test examples, locator strategy, or web automation plans.

Generated Playwright code or plans are automation artifacts only until actually run.

## Core Rules

1. Prefer user-facing locators.
2. Avoid fragile CSS selectors.
3. Avoid fixed waits.
4. Every test must include meaningful assertions.
5. Use API setup for preconditions when it improves stability.
6. Test user behavior, not implementation details.
7. Separate smoke tests from regression tests.
8. Use stable test data.
9. Clean up generated test data when needed.
10. Do not claim execution unless Playwright actually ran and produced evidence.

## Locator Priority

Prefer locators in this order:

1. getByRole
2. getByLabel
3. getByPlaceholder
4. getByText when stable
5. getByTestId
6. CSS locator only when no better option exists

## Bad Locator Example

Avoid selectors like:

page.locator("div:nth-child(3) > button")

## Better Locator Example

Prefer selectors like:

page.getByRole("button", { name: "Save" })

## Meaningful Assertion Rule

Bad pattern:

- Navigate to page
- Click button
- No assertion

Good pattern:

- Navigate to page
- Fill required data
- Submit action
- Assert URL, visible message, saved state, or API/UI result

## Fixed Wait Rule

Do not use fixed waits such as waitForTimeout unless there is no better option.

Prefer waiting for visible UI state, URL change, network response, or expected text.

## Automation Candidate Criteria

A scenario is a good Playwright candidate if:

- It is stable
- It is repeatable
- Expected result is deterministic
- Test data can be controlled
- Selectors are stable
- It has regression value
- It does not require heavy human judgment
- It does not depend on unstable external systems

## Smoke vs Regression

Smoke tests should cover only critical availability and core flow.

Regression tests can cover broader feature behavior.

Do not put every test into smoke suite.

## Role-Based Access Rule

Do not only check whether admin menu is hidden.

Also test direct URL access.

## Output Format

Use this structure:

# Playwright Automation Plan

## 1. Scope Summary

## 2. Automation Candidates

| Scenario ID | Title | Priority | Recommended Suite | Reason |
|---|---|---|---|---|

## 3. Locator Strategy

| Element | Preferred Locator | Notes |
|---|---|---|

## 4. Test Data Strategy

| Test Data | Setup Method | Cleanup Needed |
|---|---|---|

## 5. Example Playwright Tests

Include code only when requested or useful.

## 6. Risks and Flakiness Concerns

| Risk | Impact | Mitigation |
|---|---|---|

## 7. Human Test Leader Notes

## References

Use these repository references when relevant:

- references/playwright/playwright-patterns.md
- references/anti-patterns/testing-anti-patterns.md
- 06-tests/web-playwright/
