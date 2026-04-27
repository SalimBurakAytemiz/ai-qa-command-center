# Firebase Event Validation Patterns

## Purpose

This document defines practical Firebase and analytics event validation patterns for AI QA agents.

Use this reference when creating analytics validation plans, Firebase event checks, mobile event validation scenarios, web analytics scenarios, notification tracking checks, deep link tracking checks, release readiness drafts, and reporting outputs.

Important rule:

Generated Firebase validation scenarios are planning artifacts only.

They are not executed analytics results unless real evidence exists from Firebase DebugView, analytics logs, network inspection, event export, BigQuery, or other approved analytics validation tools.

---

## 1. Firebase Validation Scope

Firebase event validation may include:

- Event name validation
- Event parameter validation
- Screen view tracking
- User property validation
- Conversion event validation
- Funnel event validation
- Notification open tracking
- Deep link tracking
- Login and registration tracking
- Purchase or subscription tracking
- Error and crash event tracking
- Platform-specific event behavior
- Duplicate event risk
- Missing event risk
- Wrong user property risk

---

## 2. Event Validation Inputs

Before creating Firebase validation scenarios, collect:

| Input | Why Needed |
|---|---|
| Event name | Needed to validate exact event |
| Trigger action | Needed to know when event should fire |
| Platform | Web, iOS, Android, or mobile web |
| Required parameters | Needed for parameter validation |
| Optional parameters | Needed for completeness |
| User properties | Needed for user segmentation validation |
| Expected timing | Needed to detect early, late, or duplicate events |
| Debug tool | Needed for execution evidence |
| Analytics owner | Needed for clarification |

If this information is missing, mark it under Missing Information.

---

## 3. Event Naming Pattern

Good event names should be:

- Clear
- Stable
- Product-owned
- Lowercase or project-standard format
- Not overly generic
- Not tied to temporary UI copy

Good examples:

| Event Name | Trigger |
|---|---|
| login_success | User logs in successfully |
| login_failed | Login attempt fails |
| signup_completed | User completes registration |
| content_published | Content manager publishes content |
| notification_opened | User opens push notification |
| deep_link_opened | User opens app from deep link |

Bad examples:

| Event Name | Why Bad |
|---|---|
| click | Too generic |
| button_pressed | Does not explain business action |
| login_page_blue_button_click | Too tied to UI implementation |
| event1 | Meaningless |
| new_test_event | Temporary or unclear |

---

## 4. Event Parameter Pattern

Each event should define expected parameters.

Example:

| Event Name | Required Parameters | Optional Parameters |
|---|---|---|
| login_success | user_role, platform, auth_method | app_version |
| login_failed | failure_reason, platform | user_role |
| notification_opened | notification_id, notification_type | campaign_id |
| content_published | content_id, content_type, user_role | category_id |

Good parameter rules:

- Parameter names should be consistent.
- Required parameters should not be missing.
- Sensitive data must not be sent.
- IDs should follow privacy rules.
- Values should use expected enum or format.

---

## 5. Sensitive Data Rule

Do not send sensitive data in Firebase events.

Sensitive data includes:

- Password
- Password hash
- Access token
- Refresh token
- API key
- Email address unless explicitly approved and allowed
- Phone number
- Payment data
- Full name if not approved
- Personal customer data
- Internal security details

Bad event example:

| Event | Bad Parameter |
|---|---|
| login_failed | password=Password123 |
| signup_completed | email=user@example.com |
| payment_completed | card_number=4111111111111111 |

Good event example:

| Event | Safer Parameter |
|---|---|
| login_failed | failure_reason=invalid_credentials |
| signup_completed | signup_method=email |
| payment_completed | payment_method=card |

---

## 6. Firebase Event Test Case Format

Use this format:

| ID | Event Name | Trigger Action | Platform | Preconditions | Expected Parameters | Expected Result | Risk Area | Evidence Needed |
|---|---|---|---|---|---|---|---|---|

Example:

| ID | Event Name | Trigger Action | Platform | Preconditions | Expected Parameters | Expected Result | Risk Area | Evidence Needed |
|---|---|---|---|---|---|---|---|---|
| FB-LOGIN-001 | login_success | User logs in with valid credentials | iOS / Android / Web | Valid user exists | user_role, platform, auth_method | Event appears once with correct parameters | Funnel tracking | Firebase DebugView screenshot or event log |

---

## 7. Screen View Validation

Screen view events should confirm that important screens are tracked correctly.

| Screen | Expected Event | Required Parameters | Priority |
|---|---|---|---|
| Login screen | screen_view | screen_name=login | P1 |
| Dashboard screen | screen_view | screen_name=dashboard | P1 |
| Product detail screen | screen_view | screen_name=product_detail, product_id | P2 |
| Checkout screen | screen_view | screen_name=checkout | P1 |
| Admin dashboard | screen_view | screen_name=admin_dashboard | P2 |

Screen view risks:

- Wrong screen name
- Missing screen event
- Duplicate screen event
- Screen event fires before screen is visible
- Sensitive data included in screen parameters

---

## 8. Login Event Pattern

Common login analytics checks:

| Event | Trigger | Expected Behavior |
|---|---|---|
| login_started | User submits login form | Event fires once |
| login_success | Login succeeds | Event fires once after success |
| login_failed | Login fails | Event fires once with safe failure reason |
| logout | User logs out | Event fires once after logout |

Risk examples:

| Risk | Impact |
|---|---|
| login_success fires before API success | Funnel data becomes inaccurate |
| login_failed includes email | Sensitive data exposure |
| login_success fires twice | Conversion metrics inflated |
| login_failed not tracked | Failure funnel invisible |

---

## 9. Notification Event Pattern

Notification analytics should validate receive/open/action behavior when in scope.

| Event | Trigger | Required Parameters |
|---|---|---|
| notification_received | Device receives notification | notification_id, notification_type |
| notification_opened | User taps notification | notification_id, notification_type |
| notification_dismissed | User dismisses notification if supported | notification_id |
| notification_deep_link_opened | Notification opens deep link | notification_id, target_screen |

Risks:

- Notification opens wrong screen.
- Wrong user receives event.
- Event fires without user action.
- Missing notification_id.
- Duplicate notification_opened event.

---

## 10. Deep Link Event Pattern

Deep link analytics should include session and authorization context when relevant.

| Event | Trigger | Expected Behavior |
|---|---|---|
| deep_link_opened | User opens app through deep link | Event fires with link source and target |
| deep_link_failed | Invalid link opened | Failure event fires safely if supported |
| deep_link_redirected_to_login | Guest opens protected deep link | Event records protected route behavior if supported |

Risks:

- Protected link exposes data.
- Event misses target screen.
- Event includes sensitive URL parameters.
- Event fires with wrong campaign attribution.

---

## 11. Conversion Event Pattern

Conversion events should be protected from duplicates.

Examples:

| Conversion Event | Trigger | Duplicate Risk |
|---|---|---|
| signup_completed | Registration success | User refresh or retry fires duplicate |
| purchase_completed | Payment success | Payment retry fires duplicate |
| subscription_started | Subscription success | Webhook and UI both fire event |
| content_published | Publish action success | Double submit fires duplicate |

Validation should check:

- Event fires only after success.
- Event fires once.
- Required parameters exist.
- Sensitive data is not included.
- Failed attempts do not trigger success conversion.

---

## 12. User Property Validation

User properties should be stable and privacy-safe.

Examples:

| User Property | Expected Values | Risk |
|---|---|---|
| user_role | guest, registered, admin | Wrong segmentation |
| subscription_status | free, trial, paid | Wrong funnel analysis |
| platform | web, ios, android | Platform reporting errors |
| language | en, tr, etc. | Localization reporting |
| account_status | active, disabled | Sensitive if misused |

Rules:

- Do not store secrets.
- Avoid personal data unless approved.
- Confirm values are standardized.
- Confirm update timing.

---

## 13. Duplicate Event Risk Pattern

Duplicate events can corrupt analytics.

Common causes:

- Double click
- Retry logic
- Page refresh
- App lifecycle resume
- Both frontend and backend tracking same conversion
- Notification opened multiple times
- Screen view fires on every render

Validation pattern:

| Risk | Recommended Check |
|---|---|
| Double submit fires duplicate event | Submit twice and check event count |
| Screen re-render fires duplicate screen_view | Navigate once and observe event count |
| Retry creates duplicate conversion | Simulate retry and check conversion count |
| Notification open fires duplicate | Tap once and confirm one event |

---

## 14. Missing Event Risk Pattern

Missing events cause blind spots in analytics.

Examples:

| Missing Event | Impact |
|---|---|
| login_failed missing | Cannot analyze auth failures |
| purchase_completed missing | Revenue funnel inaccurate |
| notification_opened missing | Campaign performance inaccurate |
| content_published missing | CMS usage not measurable |
| screen_view missing | User flow analysis incomplete |

---

## 15. Firebase Validation Report Format

Use this structure:

# Firebase Event Validation Plan

## 1. Scope Summary

## 2. Events Covered

| Event Name | Trigger | Platform | Priority |
|---|---|---|---|

## 3. Event Test Scenarios

| ID | Event Name | Trigger Action | Platform | Preconditions | Expected Parameters | Expected Result | Risk Area | Evidence Needed |
|---|---|---|---|---|---|---|---|---|

## 4. Screen View Checks

| Screen | Expected Event | Required Parameters | Priority |
|---|---|---|---|

## 5. User Property Checks

| User Property | Expected Values | Trigger | Risk |
|---|---|---|---|

## 6. Duplicate Event Risks

| Event | Duplicate Trigger | Recommended Validation |
|---|---|---|

## 7. Sensitive Data Risks

| Event or Parameter | Risk | Required Action |
|---|---|---|

## 8. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 9. Evidence Needed

| Evidence | Purpose |
|---|---|
| Firebase DebugView screenshot | Event existence and parameters |
| Event log export | Event count and timing |
| BigQuery export | Historical validation if enabled |
| Network log | Web analytics request validation |
| Device log | Native app event validation |

## 10. Human Approval Points

| Item | Reason |
|---|---|

---

## 16. Human Approval Required

Human approval is required for:

- Sending real user data to analytics
- Tracking personal data
- Using production analytics events
- Modifying conversion events
- Publishing analytics findings
- Testing push notifications against real users
- Using customer accounts
- Sharing analytics screenshots externally

---

## 17. Generated vs Executed Rule

Correct wording:

- Firebase validation scenario generated
- Event validation plan prepared
- Expected event parameters identified
- Evidence required from DebugView
- Duplicate event risk identified

Incorrect wording without evidence:

- Firebase event verified
- Analytics passed
- Event is firing correctly
- Conversion tracking is valid
- DebugView confirmed

---

## 18. Firebase Validation Quality Checklist

A good Firebase validation plan should include:

- Event names
- Trigger actions
- Platforms
- Required parameters
- Optional parameters if relevant
- Screen view checks
- User property checks
- Duplicate event risks
- Missing event risks
- Sensitive data checks
- Evidence needed
- Human approval points
- Generated vs executed distinction

A bad Firebase validation plan:

- Says "check analytics" without event names
- Does not list parameters
- Ignores duplicate events
- Ignores sensitive data
- Ignores platform differences
- Claims Firebase is verified without DebugView or event evidence
