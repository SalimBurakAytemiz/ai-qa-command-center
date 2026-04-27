# Security Testing Checklist

## Purpose

This document provides a practical security testing checklist for AI QA agents.

Use this reference when creating security-aware test strategies, risk analysis, API validation plans, web validation plans, release readiness drafts, and output reviews.

Important rule:

This checklist does not replace a professional security assessment, penetration test, or secure code review.

Generated security checks are planning artifacts only unless real execution evidence exists.

---

## 1. Security Testing Scope

Security testing should consider:

- Authentication
- Authorization
- Session management
- Token handling
- Direct URL access
- Role-based access control
- Sensitive data exposure
- Account enumeration
- Input validation
- API abuse
- Rate limiting
- Error message safety
- File upload safety
- Password and credential handling
- Production data safety
- Audit and logging
- Human approval gates

---

## 2. Authentication Checklist

Authentication checks should validate whether users can prove their identity correctly.

| Check | Expected Behavior | Priority |
|---|---|---|
| Valid user login | User can log in with valid credentials | P0 |
| Invalid password | Login is rejected | P1 |
| Unknown email or username | Login is rejected safely | P1 |
| Disabled user login | Login is rejected | P1 |
| Empty credentials | Request is rejected or UI validation is shown | P2 |
| Invalid email format | Request is rejected or UI validation is shown | P2 |
| Logout | Session or token is invalidated if supported | P2 |
| Expired session | Protected access is rejected | P1 |

Good rule:

Authentication failures should not reveal sensitive account information.

---

## 3. Authorization Checklist

Authorization checks validate whether the authenticated user has permission to perform an action.

| Check | Expected Behavior | Priority |
|---|---|---|
| Guest accesses protected page | Access denied or redirect to login | P0 |
| Normal user accesses admin page | Access denied | P0 |
| User accesses another user's data | Access denied | P0 |
| Disabled user accesses protected resource | Access denied | P1 |
| User performs action outside role | Action rejected | P1 |
| Hidden UI action is called directly through API | API rejects action | P0 |

Important rule:

Do not only test whether UI buttons are hidden.

Always test direct URL or direct API access when possible.

---

## 4. Direct URL Access Checks

Direct URL access is a common access-control risk.

| Scenario | Expected Result | Priority |
|---|---|---|
| Guest opens dashboard URL directly | Redirect to login or unauthorized page | P0 |
| Normal user opens admin URL directly | Access denied | P0 |
| User opens another user's detail page URL | Access denied | P0 |
| Disabled user opens protected URL | Access denied | P1 |

Bad validation:

The admin menu is hidden for normal user.

Better validation:

The normal user directly opens the admin URL and access is denied.

---

## 5. API Security Checklist

API security checks should cover authentication, authorization, request validation, and data exposure.

| Check | Expected Behavior | Priority |
|---|---|---|
| Protected endpoint without token | 401 Unauthorized | P1 |
| Protected endpoint with invalid token | 401 Unauthorized | P1 |
| Protected endpoint with wrong role | 403 Forbidden | P0/P1 |
| User accesses another user's resource | Access denied | P0 |
| Invalid payload | Validation error | P2 |
| Unexpected field injection | Ignored or rejected | P2 |
| Sensitive fields in response | Must not expose secrets | P0/P1 |
| Unauthorized request changes DB | No DB state change | P0 |

Sensitive fields that should not be exposed:

- password
- password_hash
- access_token unless intentionally returned by auth flow
- refresh_token unless intentionally returned by auth flow
- secret
- private_key
- API key
- internal notes
- payment details
- personal data not required by the client

---

## 6. Account Enumeration Checklist

Account enumeration occurs when the system reveals whether an account exists.

| Scenario | Bad Behavior | Good Behavior |
|---|---|---|
| Login with wrong password | "Password incorrect for this email" | Generic invalid credentials message |
| Login with unknown email | "Email not found" | Generic invalid credentials message |
| Password reset with unknown email | "No account found" | Generic neutral response |
| Registration with existing email | Must be handled carefully | Product-specific safe behavior |

Risk:

Attackers may discover valid accounts.

Recommended validation:

Compare error message, status code, and response body for existing vs unknown accounts.

---

## 7. Session and Token Security Checklist

| Check | Expected Behavior | Priority |
|---|---|---|
| Token created after login | Token belongs to correct user | P0 |
| Token used after logout | Rejected if invalidation is supported | P1 |
| Expired token | Rejected | P1 |
| Token from user A used for user B data | Access denied | P0 |
| Disabled user token | Rejected or invalidated | P1 |
| Token exposed in URL | Should not happen | P1 |
| Session persists unexpectedly after logout | Should not happen | P1 |

Human review is recommended for token/session design assumptions.

---

## 8. Sensitive Data Exposure Checklist

Check whether sensitive data appears in:

- UI
- API response
- Browser storage
- URL parameters
- Logs
- Error messages
- Reports
- Screenshots
- Jira/Trello drafts
- Generated AI outputs

| Data Type | Risk | Priority |
|---|---|---|
| Password or password hash | Severe credential exposure | P0 |
| Access token | Account takeover risk | P0 |
| Refresh token | Long-term access risk | P0 |
| Personal customer data | Privacy risk | P0/P1 |
| Payment data | Financial and compliance risk | P0 |
| Internal system details | Attack surface exposure | P1 |
| Stack trace | Implementation leakage | P2 |

---

## 9. Error Message Safety

Error messages should be useful but not dangerous.

Bad examples:

- Email exists but password is wrong.
- SQL syntax error near users table.
- Token validation failed because user_id 123 is disabled.
- Stack trace with file paths.
- Database connection string visible.

Good examples:

- Invalid credentials.
- Access denied.
- Something went wrong. Please try again.
- Invalid request.

Error message validation should include:

- UI error message
- API error response
- Console errors if relevant
- Server logs if accessible and safe

---

## 10. Input Validation Security

Input validation should protect the system from invalid or dangerous input.

Common checks:

| Input Type | Example Case | Expected Behavior |
|---|---|---|
| Required field | Missing email | Validation error |
| Type mismatch | Number instead of string | Validation error |
| Long string | Very long text | Rejected or safely handled |
| HTML input | Script-like content | Stored/displayed safely |
| SQL-like input | Quote or SQL-like payload | Treated as data, not query |
| File input | Unsupported file type | Rejected |
| ID field | Access another ID | Access denied or not found |

Do not claim vulnerability unless executed evidence exists.

Use "security risk" or "validation scenario" when planning.

---

## 11. File Upload Security Checklist

Use if file upload exists.

| Check | Expected Behavior | Priority |
|---|---|---|
| Unsupported file type | Rejected | P1 |
| Oversized file | Rejected | P2 |
| File with dangerous extension | Rejected | P1 |
| File name with special characters | Safely handled | P2 |
| Uploaded file direct public access | Controlled by permission | P1 |
| User accesses another user's file | Access denied | P0 |

---

## 12. Production Data Safety

Production data must not be used without explicit human approval.

Rules:

- Do not use real customer personal data.
- Do not use production credentials.
- Do not use production database snapshots without approval.
- Do not paste real secrets into AI tools.
- Use synthetic test users and sanitized test data.
- Mask secrets in logs, reports, tickets, and generated outputs.

Human approval is required for:

- Production data usage
- Sensitive data review
- Security-sensitive architecture review
- Payment or personal data validation
- Destructive DB validation

---

## 13. Security Risk Priority Examples

| Risk | Suggested Priority | Reason |
|---|---|---|
| Guest can access protected dashboard | P0 | Unauthorized access |
| Normal user can access admin API | P0 | Privilege escalation |
| User can access another user's data | P0 | Privacy and data exposure |
| Disabled user can log in | P1 | Access control failure |
| Error reveals whether email exists | P1 | Account enumeration |
| Stack trace visible to user | P2 | Information leakage |
| Missing loading state | P3 | Not security unless duplicate critical action occurs |

---

## 14. Security Test Case Pattern

Use this structure:

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Security Risk | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|

Example:

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Security Risk | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| SEC-AUTHZ-001 | Verify guest cannot access dashboard directly | P0 | Web | Guest User | User is not logged in | Dashboard URL | 1. Open dashboard URL directly | User is redirected to login or access is denied | Unauthorized access | Yes |

---

## 15. Security Reporting Rules

Correct wording:

- Security risk identified
- Security validation planned
- Access-control scenario generated
- Human review required
- Execution evidence required

Incorrect wording without execution evidence:

- Security verified
- Vulnerability confirmed
- System is secure
- Penetration testing completed
- Release safe

---

## 16. Security Checklist For Output Reviewer

Output Reviewer Agent should check:

- Did the output include authentication risks?
- Did the output include authorization risks?
- Did it test direct URL/API access?
- Did it avoid exposing secrets?
- Did it distinguish generated planning from executed evidence?
- Did it mark human approval needs?
- Did it avoid unsupported vulnerability claims?
- Did it identify missing security information?
- Did it prioritize P0/P1 correctly?

---

## 17. Human Approval Gates

Human approval is required for:

- P0 security classification
- Security-sensitive bug creation
- Release go/no-go decision
- Production data usage
- Sensitive data sharing with external AI
- Destructive DB validation
- Security report publication
- Final executive risk communication

---

## 18. Security Testing Quality Checklist

A good security checklist output should include:

- Authentication checks
- Authorization checks
- Direct URL/API access checks
- Session/token checks
- Sensitive data checks
- Safe error message checks
- Account enumeration checks
- Missing information
- Risk priority
- Human approval points
- Generated vs executed distinction

A bad security checklist output:

- Only tests happy path login
- Only checks hidden UI buttons
- Ignores direct API access
- Ignores role-based risks
- Claims system is secure without evidence
- Marks all risks P0 without justification
