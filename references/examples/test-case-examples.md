# Test Case Examples

## Purpose

This document provides good and bad examples of test cases.

AI QA agents should use these examples to understand what high-quality test cases look like.

---

## 1. Bad Test Case: Vague Expected Result

### Bad

| ID | Title | Steps | Expected Result |
|---|---|---|---|
| TC-001 | Check login | Enter valid email and password, click Login | System works correctly |

### Why This Is Bad

- Expected result is vague.
- It does not say where the user should land.
- It does not say what should be visible.
- It cannot be reliably verified by a tester or automation.

### Good

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-HP-001 | Verify registered user can log in with valid credentials | P0 | Web | Registered User | User account exists and is active | valid.user@example.com / CorrectPassword123 | 1. Open login page 2. Enter valid email 3. Enter valid password 4. Click Login | User is redirected to the dashboard and the dashboard displays the logged-in user's full name | Yes |

---

## 2. Bad Test Case: Missing Preconditions

### Bad

| ID | Title | Steps | Expected Result |
|---|---|---|---|
| TC-002 | Update profile | Change name and click Save | Profile is updated |

### Why This Is Bad

- It does not say whether the user must be logged in.
- It does not say which role is required.
- It does not define existing profile state.
- It does not define test data.

### Good

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|
| TC-PROFILE-HP-001 | Verify registered user can update profile name | P1 | Web | Registered User | User is logged in, profile page is accessible, API and DB are available | New name: Test User Updated | 1. Open Profile page 2. Change name field 3. Click Save 4. Refresh the page | Success message is displayed and the updated name remains visible after refresh | Yes |

---

## 3. Good Happy Path Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Acceptance Criteria Coverage | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-CMS-HP-001 | Verify content manager can publish a CMS article | P1 | CMS / Web | Content Manager | Content manager user exists, CMS is accessible, web frontend is available | Article title: Test Article, Status: Draft | 1. Log in to CMS 2. Open draft article 3. Click Publish 4. Open public web page | Article status changes to Published in CMS and article appears on public web page | AC-001, AC-002 | Later |

### Why This Is Good

- It has a clear user role.
- It has a platform.
- It has preconditions.
- It defines test data.
- It validates the result in both CMS and web.
- It links to acceptance criteria.
- It marks automation realistically.

---

## 4. Good Edge Case Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-PROFILE-EDGE-001 | Verify profile name field handles maximum allowed character length | P2 | Web | Registered User | User is logged in and profile page is accessible | Name with maximum allowed character count | 1. Open Profile page 2. Enter maximum allowed name length 3. Click Save | Profile is saved successfully and the full name is displayed without layout break | Boundary / UI Layout | Yes |

### Why This Is Good

- It tests a realistic boundary.
- It has clear expected behavior.
- It checks both functional and visual risk.
- It can be automated if test data and locator are stable.

---

## 5. Good Negative Case Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-NEG-001 | Verify login is rejected with invalid password | P1 | Web | Registered User | Active user account exists | valid.user@example.com / WrongPassword123 | 1. Open login page 2. Enter valid email 3. Enter invalid password 4. Click Login | Login is rejected, user remains on login page, and an invalid credentials message is displayed | Authentication | Yes |

### Why This Is Good

- It tests rejection behavior.
- It does not mix with happy path.
- It includes expected user-facing message.
- It is suitable for regression automation.

---

## 6. Good Permission Case Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-ADMIN-PERM-001 | Verify registered user cannot access admin user management page | P0 | Web Admin Panel | Registered User | Registered user exists without admin permission | Normal user credentials | 1. Log in as registered user 2. Navigate directly to admin user management URL | Access is denied and user sees a forbidden or unauthorized message | Authorization | Yes |

### Why This Is Good

- It validates role boundary.
- It tests direct URL access, not just hidden menu behavior.
- It is release-critical if admin access is sensitive.

---

## 7. Good API-Linked Test Case Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-PROFILE-API-001 | Verify profile update reflects API and UI state consistently | P1 | Web / API | Registered User | User is logged in and profile API is available | New name: API UI Sync Test | 1. Update profile name from UI 2. Capture profile API response 3. Refresh profile page | API returns updated name and UI displays the same updated name after refresh | API-UI Consistency | Later |

### Why This Is Good

- It connects UI behavior with API state.
- It identifies a consistency risk.
- It marks automation as Later because API access and test hooks may be needed.

---

## 8. Good DB-Linked Test Case Example

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-PROFILE-DB-001 | Verify profile update creates correct database state | P1 | Web / Database | Registered User | User exists, DB validation access is available | New name: DB Validation User | 1. Update profile name from UI 2. Check user entity in test database | User name is updated and updated_at timestamp changes | DB Consistency | Later |

### Why This Is Good

- It validates persistent state.
- It includes database dependency.
- It avoids pretending DB validation happened without access.

---

## 9. Test Case Quality Checklist

A good test case should include:

- Clear ID
- Clear title
- Priority
- Platform
- User role
- Preconditions
- Test data
- Executable steps
- Observable expected result
- Risk area
- Automation candidate value
- Notes if needed

## 10. Common Bad Patterns

Avoid:

- "System works correctly"
- "Verify feature"
- Missing expected result
- Missing preconditions
- Missing user role
- Missing platform
- Mixing valid and invalid scenarios
- No test data
- No risk priority
- Claiming execution without evidence