# Mobile Testing Patterns

## Purpose

This document defines practical mobile testing patterns for AI QA agents.

Use this reference when creating mobile test strategies, mobile test cases, responsive validation plans, mobile risk analysis, release readiness drafts, and automation candidate recommendations.

Important rule:

Generated mobile test scenarios are planning artifacts only.

They are not executed mobile test results unless real execution evidence exists from a device, emulator, simulator, Appium run, manual test session, crash report, device log, analytics event, or monitoring tool.

---

## 1. Mobile Testing Scope

Mobile testing may include:

- Native iOS app behavior
- Native Android app behavior
- Mobile web behavior
- Responsive layout
- Device compatibility
- OS version compatibility
- App installation and update behavior
- Login and session behavior
- Push notification behavior
- Deep link behavior
- Offline and poor network behavior
- App lifecycle behavior
- Permission handling
- Crash and freeze behavior
- Mobile API integration behavior
- Analytics and Firebase event validation

---

## 2. Platform Separation Rule

Do not mix these without marking the platform clearly:

- iOS native app
- Android native app
- Mobile web
- Tablet web
- Responsive desktop browser emulation

Good:

| Platform | Scenario |
|---|---|
| iOS | User logs in and remains authenticated after app background/foreground |
| Android | User receives push notification and opens deep link |
| Mobile Web | Login page remains usable when keyboard is open |

Bad:

Mobile login works.

Why bad:

- Platform is unclear.
- Device is unclear.
- OS is unclear.
- Expected behavior is vague.

---

## 3. Device Matrix Pattern

Use a device matrix for mobile validation.

| Platform | Device | OS Version | Priority | Reason |
|---|---|---|---|---|
| iOS | Latest iPhone model | Latest stable iOS | P1 | Current primary iOS coverage |
| iOS | Older supported iPhone | Oldest supported iOS | P1 | Compatibility risk |
| Android | Popular Samsung device | Latest supported Android | P1 | High market coverage |
| Android | Low-end Android device | Supported Android version | P2 | Performance and layout risk |
| Mobile Web | Chrome Android | Latest stable | P2 | Responsive web coverage |
| Mobile Web | Safari iOS | Latest stable | P2 | iOS web behavior |

Do not claim broad mobile coverage if only one device was used.

---

## 4. Mobile Risk Categories

| Risk Category | Description | Example |
|---|---|---|
| Device Compatibility Risk | Behavior differs by device | Layout breaks on small Android screen |
| OS Compatibility Risk | Behavior differs by OS version | Permission dialog differs on Android versions |
| Network Risk | Behavior fails on slow or unstable network | Login hangs on poor connection |
| Session Risk | App loses auth state unexpectedly | User is logged out after backgrounding |
| Permission Risk | Camera/location/notification permission fails | App crashes after permission denied |
| Deep Link Risk | Link opens wrong screen | Push notification opens home instead of order detail |
| Push Notification Risk | Notification not received or wrong payload | User misses important alert |
| Offline Risk | App behaves badly without connection | Infinite loading instead of offline message |
| Crash Risk | App closes unexpectedly | Crash after tapping submit |
| Performance Risk | App slow or freezes | Long list scroll stutters |

---

## 5. Mobile Test Case Format

Use this format:

| ID | Title | Priority | Platform | Device / OS | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|---|

Example:

| ID | Title | Priority | Platform | Device / OS | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MOB-LOGIN-001 | Verify user stays logged in after app background and foreground | P1 | iOS | iPhone, supported iOS | Registered User | User is logged in | Valid user account | 1. Log in 2. Background app 3. Wait 2 minutes 4. Reopen app | User remains authenticated or is asked to re-authenticate according to product rule | Session | Later |

---

## 6. App Lifecycle Checks

Mobile apps must handle lifecycle events.

| Scenario | Expected Behavior | Priority |
|---|---|---|
| App backgrounded and reopened | State is preserved or restored correctly | P1 |
| App killed and reopened | User session follows product rule | P1 |
| Device locked and unlocked | App resumes safely | P2 |
| App interrupted by phone call | App resumes without crash | P3 |
| App updated from previous version | User data/session handled correctly | P1 |
| App opened from cold start | Initial screen loads correctly | P1 |

---

## 7. Network Condition Checks

Validate behavior under different network states.

| Network Condition | Expected Behavior | Priority |
|---|---|---|
| Wi-Fi | Normal behavior | P2 |
| 4G / 5G | Normal behavior | P2 |
| Slow 3G | Loading state or timeout handled | P2 |
| Offline | Offline or error state displayed | P1 |
| Network drops during request | Safe error or retry behavior | P1 |
| Network returns after offline | App recovers or allows retry | P2 |

Do not assume all mobile users have stable network.

---

## 8. Permission Handling Checks

Use if the app requests permissions.

| Permission | Allow Behavior | Deny Behavior | Priority |
|---|---|---|---|
| Camera | Feature works | User sees useful message | P1 |
| Location | Location feature works | Fallback or message shown | P1 |
| Notifications | Push can be received | App explains how to enable if needed | P2 |
| Photos | Upload works | User sees permission guidance | P2 |
| Microphone | Recording works | Feature blocked safely | P2 |

Good rule:

Permission denied should not cause crash.

---

## 9. Deep Link Checks

Use if app supports deep links.

| Scenario | Expected Behavior | Priority |
|---|---|---|
| Logged-in user opens valid deep link | Correct screen opens | P1 |
| Guest opens protected deep link | Login required, then correct destination if supported | P1 |
| Invalid deep link | Safe fallback screen shown | P2 |
| Deep link with expired session | Re-authentication flow works | P1 |
| Deep link to unauthorized resource | Access denied | P0/P1 |

Deep link tests must include role and session state.

---

## 10. Push Notification Checks

Use if push notifications are in scope.

| Scenario | Expected Behavior | Priority |
|---|---|---|
| Notification received in foreground | App shows expected in-app behavior | P2 |
| Notification received in background | System notification displayed | P2 |
| User taps notification | Correct screen opens | P1 |
| Notification payload missing data | Safe fallback behavior | P2 |
| Guest taps protected notification | Login required | P1 |
| Wrong user receives notification | Must not happen | P0 |

Push notification validation may require Firebase or provider logs.

---

## 11. Mobile Web Responsive Checks

Use for mobile web.

| Scenario | Expected Behavior | Priority |
|---|---|---|
| Small viewport | Layout does not break | P2 |
| Keyboard open | Important button remains usable or page scrolls | P2 |
| Orientation change | Layout remains usable | P3 |
| Long text | Does not overflow critical UI | P3 |
| Touch target size | Main buttons are tappable | P2 |
| No horizontal scroll | Page fits viewport | P2 |

Example:

Login button should remain reachable when password field is focused and mobile keyboard is open.

---

## 12. Mobile Performance Checks

Mobile performance should consider:

- App launch time
- Screen load time
- Scroll smoothness
- Image loading
- Large list rendering
- Battery usage
- Memory usage
- Offline cache performance
- Slow network handling

| Scenario | Metric | Priority |
|---|---|---|
| App cold start | Time to first usable screen | P2 |
| Login screen load | Time to interactive | P2 |
| Large list scroll | Jank or stutter | P2 |
| Image-heavy screen | Load time and memory | P2 |
| Repeated navigation | Memory growth | P2 |

Do not invent thresholds. Use "Needs Confirmation" when targets are missing.

---

## 13. Mobile Automation Candidate Guidance

Good Appium candidates:

- Stable login flow
- Navigation smoke tests
- Permission allow/deny flows
- Deep link routing
- Basic form validation
- Critical regression flows

Poor automation candidates:

- Visual polish requiring human judgment
- Highly unstable third-party flows
- Random push delivery timing without control
- Complex gestures without stable selectors
- Tests requiring production data
- Device-specific bugs without stable reproduction

Use:

- Yes
- No
- Later

---

## 14. Mobile Missing Information Examples

| Missing Item | Why Needed | Impact |
|---|---|---|
| Supported devices | Needed for device matrix | Coverage may be incomplete |
| Supported OS versions | Needed for compatibility testing | Old OS risks may be missed |
| Deep link schema | Needed for deep link testing | Cannot validate routing |
| Push payload format | Needed for notification testing | Cannot validate payload behavior |
| Permission requirements | Needed for permission testing | Deny/allow cases may be missed |
| Offline behavior requirement | Needed for network testing | Expected result unclear |
| App session rule | Needed for lifecycle testing | Auth behavior unclear |

---

## 15. Mobile Reporting Rules

Correct wording:

- Mobile test scenario generated
- Mobile validation plan prepared
- Device matrix proposed
- Appium candidate identified
- Execution evidence required

Incorrect wording without evidence:

- Mobile testing completed
- iOS verified
- Android passed
- App is stable
- No crash found
- Mobile release ready

---

## 16. Human Approval Required

Human approval is required for:

- Production user data on devices
- Real customer account testing
- Push notification tests to real users
- Payment or financial mobile flows
- Release readiness decisions
- Publishing crash/security findings
- Device farm cost usage if applicable
- External ticket creation

---

## 17. Mobile Testing Quality Checklist

A good mobile test plan should include:

- Platform separation
- Device matrix
- OS version coverage
- Network condition checks
- Lifecycle checks
- Permission checks
- Deep link checks if relevant
- Push notification checks if relevant
- Mobile web responsive checks if relevant
- Session behavior
- Missing information
- Automation candidate decision
- Human approval points
- Generated vs executed distinction

A bad mobile test plan:

- Says "test mobile" without platform
- Ignores device/OS coverage
- Ignores poor network behavior
- Ignores app lifecycle
- Claims mobile passed without execution
- Mixes iOS, Android, and mobile web without clarity
