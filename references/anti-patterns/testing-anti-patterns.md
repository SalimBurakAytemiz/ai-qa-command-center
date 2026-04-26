# Testing Anti-Patterns

## Purpose

This document lists common testing mistakes that AI QA agents must avoid.

It should be used when generating test cases, automation plans, API validation, DB validation, bug reports, or QA reports.

---

## 1. Vague Expected Results

### Problem

A vague expected result cannot be verified by a tester or automation.

### Bad

The system works correctly.

### Good

The user is redirected to the dashboard and the dashboard displays the logged-in user's full name.

### Rule

Expected results must be observable, specific, and testable.

---

## 2. Mixing Happy Path and Negative Cases

### Problem

Mixing successful and failure scenarios makes test coverage unclear.

### Bad

Verify login with valid email, invalid password, empty email, and successful dashboard redirect.

### Good

Happy path:

Verify login with valid email and valid password.

Negative case:

Verify login is rejected when the password is invalid.

### Rule

Happy path, edge case, and negative case outputs must be separated.

---

## 3. Testing Implementation Instead of Behavior

### Problem

Tests should verify product behavior, not internal implementation details.

### Bad

expect(userService.validatePassword).toHaveBeenCalled();

### Good

const response = await request.post("/api/login", {
  data: {
    email: "valid.user@example.com",
    password: "CorrectPassword123"
  }
});

expect(response.status()).toBe(200);

### Rule

Prefer behavior validation over internal method validation unless unit testing is explicitly required.

---

## 4. Over-Mocking

### Problem

Mocking everything creates tests that pass while production behavior can still break.

### Bad

const mockUserService = {
  getUser: jest.fn().mockReturnValue({ id: "1", name: "Test" }),
  validateAccess: jest.fn().mockReturnValue(true)
};

test("user has access", () => {
  expect(mockUserService.validateAccess()).toBe(true);
});

### Good

test("user can access protected resource with valid role", async ({ request }) => {
  await request.post("/api/test-users", {
    data: {
      name: "Test User",
      role: "viewer"
    }
  });

  const response = await request.get("/api/protected-resource");

  expect(response.status()).toBe(200);
});

### Rule

Use mocks only when they reduce external instability. Do not mock the behavior you are trying to validate.

---

## 5. No Test Data Control

### Problem

Tests become flaky when test data is unknown, shared, or manually created.

### Bad

Use any existing admin user.

### Good

Create a dedicated test admin user before execution and delete or reset it after the test.

### Rule

Every test should define required test data and cleanup expectations.

---

## 6. No Cleanup Strategy

### Problem

Tests pollute the environment and create false failures later.

### Bad

Create a new CMS article and leave it in the environment.

### Good

Create a test CMS article, validate visibility, then archive or delete it after validation.

### Rule

State-changing tests should include cleanup or reset expectations.

---

## 7. Ignoring Authorization

### Problem

Many critical bugs happen because wrong users can access restricted actions.

### Bad

Verify admin page loads.

### Good

Verify admin page is accessible to Admin User and forbidden for Registered User.

### Rule

Always include role-based access checks when roles or permissions are involved.

---

## 8. Ignoring Database State

### Problem

A UI or API may appear successful while database state is incorrect.

### Bad

Verify profile update returns success message.

### Good

Verify profile update returns success message and the user record is updated with the new name and updated_at timestamp.

### Rule

For state-changing actions, consider DB validation when relevant.

---

## 9. Flaky Selectors

### Problem

Automation tests become unstable when selectors depend on layout, text that changes often, or generated IDs.

### Bad

await page.locator("div:nth-child(3) > button").click();

### Good

await page.getByRole("button", { name: "Save" }).click();

### Better

await page.getByTestId("profile-save-button").click();

### Rule

Prefer stable locators such as role, label, accessible name, or test id.

---

## 10. No Clear Preconditions

### Problem

A test without preconditions cannot be reliably executed.

### Bad

Check that user can update profile.

### Good

Precondition: Registered user exists, user is logged in, profile page is accessible, API and DB are available.

### Rule

Every test case must define preconditions.

---

## 11. No Risk Priority

### Problem

A flat list of test cases does not help the human test leader make decisions.

### Bad

All test cases have the same priority.

### Good

Login success: P0  
Invalid password handling: P1  
Password field placeholder text: P3

### Rule

Every test case and risk must include priority.

---

## 12. Reporting Generated Plans as Executed Tests

### Problem

This creates false confidence.

### Bad

Login feature passed testing.

This is wrong if only test cases were generated.

### Good

Login feature test plan and test cases were generated. Execution has not started yet.

### Rule

Always distinguish generated, planned, reviewed, executed, blocked, and approved.

---

## 13. No Assertion

### Problem

A test without assertion does not prove anything.

### Bad

await page.goto("/login");
await page.fill("#email", "user@example.com");
await page.fill("#password", "Password123");
await page.click("#login");

### Good

await page.goto("/login");
await page.getByLabel("Email").fill("user@example.com");
await page.getByLabel("Password").fill("Password123");
await page.getByRole("button", { name: "Login" }).click();

await expect(page).toHaveURL(/dashboard/);
await expect(page.getByText("Welcome")).toBeVisible();

### Rule

Every automation test must include meaningful assertions.

---

## 14. Only Testing the UI

### Problem

A UI test may pass while API or database behavior is wrong.

### Bad

Verify that the success toast is displayed after saving the profile.

### Good

Verify that the success toast is displayed, the API returns success, and the database stores the updated profile data.

### Rule

For critical state-changing flows, consider UI, API, and DB consistency together.

---

## 15. Ignoring Error States

### Problem

Many product failures happen in error, empty, loading, or retry states.

### Bad

Verify the profile page opens.

### Good

Verify the profile page opens successfully, displays loading state while data is loading, shows an empty state when no data exists, and shows an error message when the API fails.

### Rule

UI validation should include default, loading, empty, success, and error states when relevant.