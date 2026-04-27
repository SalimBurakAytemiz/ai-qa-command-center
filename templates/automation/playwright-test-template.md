# Playwright Test Template

## Purpose

Use this template when preparing Playwright test drafts from approved automation candidates.

Important rule:

Generated Playwright tests are automation drafts only.

They are not executed test results unless Playwright is actually run and execution evidence exists.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | |
| Scenario ID | |
| Test Type | Smoke / Regression / Security Regression / E2E |
| Priority | P0 / P1 / P2 / P3 |
| Platform | Web / Mobile Web |
| Source Test Case | |
| Automation Candidate Decision | Yes / Later |
| Human Approval Required | If sensitive, destructive, or production-related |

---

## 2. Preconditions

List required setup before the test can run.

Examples:

- Test environment is available.
- Test user exists.
- User has required role.
- Required feature flag is enabled.
- API setup is available if needed.

---

## 3. Test Data

| Data | Value or Source | Notes |
|---|---|---|
| Test user | | |
| Password | Use environment variable | Do not hardcode secrets |
| Base URL | Use environment variable | |
| Feature data | | |

---

## 4. Locator Strategy

Use stable, user-facing locators when possible.

Preferred order:

1. getByRole
2. getByLabel
3. getByPlaceholder
4. getByText when stable
5. getByTestId
6. CSS locator only when no better option exists

| Element | Preferred Locator | Notes |
|---|---|---|
| | | |

---

## 5. Test Steps

| Step | Action | Expected UI or State |
|---:|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

---

## 6. Expected Assertions

Every Playwright test must include meaningful assertions.

| Assertion | Reason |
|---|---|
| | |

Good assertion examples:

- URL changed to expected route.
- Success message is visible.
- User full name is visible.
- Access denied message is visible.
- API-created state appears in UI.

Bad assertion pattern:

- Click button with no assertion.
- Wait fixed time and assume success.

---

## 7. Draft Playwright Test

Use this section only when code generation is requested.

Template guidance:

- Import test and expect from Playwright.
- Use environment variables for URLs and credentials.
- Avoid hardcoded secrets.
- Avoid fixed waits.
- Use stable locators.
- Add meaningful assertions.
- Keep the test focused.

Example structure without real secrets:

import { test, expect } from '@playwright/test';

test('scenario title here', async ({ page }) => {
  await page.goto(process.env.WEB_BASE_URL || 'http://localhost:3000');

  // Add setup, actions, and assertions here.

  await expect(page).toHaveURL(/expected-route/);
});

---

## 8. Flakiness Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Unstable selector | Test may fail randomly | Use role/label/test id locator |
| Shared test data | Parallel runs may conflict | Use isolated synthetic data |
| Slow environment | Timeout failures | Wait for observable state |
| External dependency | Unstable results | Mock or control dependency if possible |

---

## 9. Cleanup Needs

| Cleanup Item | Required | Method |
|---|---|---|
| Test data cleanup | Yes / No | |
| Session cleanup | Yes / No | |
| Created records cleanup | Yes / No | |

---

## 10. Human Approval Points

| Item | Approval Needed | Reason |
|---|---|---|
| Production environment execution | Yes | Must not run without approval |
| Real customer account usage | Yes | Sensitive data risk |
| Destructive action | Yes | Data loss risk |
| Security-sensitive automation | Yes | Human review required |

---

## 11. Generated vs Executed Note

This Playwright output is a generated automation draft.

It must not be reported as passed, verified, executed, or release-ready unless the test is actually run and execution evidence exists.

---

## 12. References

- references/playwright/playwright-patterns.md
- references/automation/automation-generation-patterns.md
- .github/instructions/playwright.instructions.md
- .github/skills/web-functional-testing/SKILL.md
