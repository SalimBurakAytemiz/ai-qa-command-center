# Playwright Login Draft Example

## Purpose

This document shows an example Playwright automation draft for the login feature.

Important rule:

This is not an executed Playwright result.

It is a generated automation draft example only.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | User Login |
| Scenario ID | TC-LOGIN-HP-001 |
| Test Type | Smoke / Regression |
| Priority | P1 |
| Platform | Web |
| Source Test Case | Verify registered user can log in with valid credentials |
| Automation Candidate Decision | Yes |
| Human Approval Required | No for safe QA environment. Yes for production. |

---

## 2. Preconditions

- QA web environment is available.
- Valid registered test user exists.
- Login page route is confirmed.
- Dashboard route is confirmed.
- Credentials are stored in environment variables.
- No production user account is used.

---

## 3. Draft Playwright Test

~~~typescript
import { test, expect } from '@playwright/test';

test('registered user can log in with valid credentials', async ({ page }) => {
  const baseUrl = process.env.WEB_BASE_URL;
  const email = process.env.TEST_USER_EMAIL;
  const password = process.env.TEST_USER_PASSWORD;

  if (!baseUrl || !email || !password) {
    throw new Error('Missing required environment variables.');
  }

  await page.goto(`${baseUrl}/login`);

  await expect(page.getByLabel(/email/i)).toBeVisible();
  await page.getByLabel(/email/i).fill(email);

  await expect(page.getByLabel(/password/i)).toBeVisible();
  await page.getByLabel(/password/i).fill(password);

  await page.getByRole('button', { name: /login/i }).click();

  await expect(page.getByRole('heading', { name: /dashboard/i })).toBeVisible();
});
~~~

---

## 4. Flakiness Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Dashboard heading text unknown | Assertion may fail | Confirm dashboard UI text |
| Login route unknown | Navigation may fail | Confirm route |
| Shared test user state | Test may be unstable | Use dedicated synthetic user |
| Slow environment | Timeout failures | Wait for observable UI state |

---

## 5. Generated vs Executed Note

This Playwright output is a generated automation draft example.

It must not be reported as passed, verified, executed, or release-ready unless it is actually run and execution evidence exists.
