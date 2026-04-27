# Appium Test Template

## Purpose

Use this template when preparing Appium test drafts from approved mobile automation candidates.

Important rule:

Generated Appium tests are automation drafts only.

They are not executed mobile test results unless Appium is actually run on a real device, emulator, simulator, or device farm and execution evidence exists.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | |
| Scenario ID | |
| Test Type | Smoke / Regression / Mobile E2E / Permission / Deep Link |
| Priority | P0 / P1 / P2 / P3 |
| Platform | iOS / Android |
| Device Type | Real Device / Emulator / Simulator / Device Farm |
| Source Test Case | |
| Automation Candidate Decision | Yes / Later |
| Human Approval Required | If sensitive, production-related, payment-related, or real-user-impacting |

---

## 2. Preconditions

List required setup before the Appium test can run.

Examples:

- App build is available.
- Device or emulator is available.
- Appium server is configured.
- Test user exists.
- Required permissions are known.
- Required backend environment is available.
- Deep link schema is confirmed if deep link is tested.

---

## 3. Device Matrix

| Platform | Device | OS Version | Priority | Notes |
|---|---|---|---|---|
| iOS | | | | |
| Android | | | | |

Do not claim broad mobile coverage if only one device was used.

---

## 4. Environment Variables

Do not hardcode secrets.

| Variable | Purpose | Required |
|---|---|---|
| MOBILE_TEST_USER_EMAIL | Test user email | If login needed |
| MOBILE_TEST_USER_PASSWORD | Test user password | If login needed |
| APP_PATH | Local app build path | If local run |
| APPIUM_SERVER_URL | Appium server URL | Yes |
| MOBILE_PLATFORM | iOS or Android | Yes |
| DEVICE_NAME | Device or emulator name | Yes |
| PLATFORM_VERSION | OS version | If required |
| APP_PACKAGE | Android app package | Android only |
| APP_ACTIVITY | Android app activity | Android only |
| BUNDLE_ID | iOS bundle id | iOS only |

---

## 5. Locator Strategy

Prefer stable mobile locators.

Recommended locator priority:

1. Accessibility ID
2. Resource ID
3. iOS predicate string
4. Android UIAutomator
5. Visible text when stable
6. XPath only as a last resort

| Element | Preferred Locator | Notes |
|---|---|---|
| | | |

Bad locator pattern:

- Deep XPath based on layout hierarchy

Better locator pattern:

- Accessibility ID or stable resource ID

---

## 6. Test Steps

| Step | Action | Expected Result |
|---:|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

---

## 7. Expected Assertions

Every Appium test must include meaningful assertions.

| Assertion | Reason |
|---|---|
| Correct screen is visible | Confirms navigation |
| Success message is visible | Confirms action result |
| Access denied message is visible | Confirms authorization behavior |
| User remains logged in or logged out according to rule | Confirms session behavior |
| Permission denial message appears | Confirms permission handling |

---

## 8. Draft Appium Test

Use this section only when code generation is requested.

Generic JavaScript Appium draft structure:

import { remote } from 'webdriverio';

async function main() {
  const driver = await remote({
    protocol: 'http',
    hostname: '127.0.0.1',
    port: 4723,
    path: '/',
    capabilities: {
      platformName: process.env.MOBILE_PLATFORM || 'Android',
      'appium:deviceName': process.env.DEVICE_NAME,
      'appium:platformVersion': process.env.PLATFORM_VERSION,
      'appium:automationName': process.env.MOBILE_PLATFORM === 'iOS' ? 'XCUITest' : 'UiAutomator2',
      'appium:app': process.env.APP_PATH
    }
  });

  try {
    // Add actions and assertions here.
  } finally {
    await driver.deleteSession();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

---

## 9. Mobile-Specific Validation Areas

| Area | Example Scenario | Priority |
|---|---|---|
| App lifecycle | Background and foreground app | P1 |
| Session | Reopen app after login | P1 |
| Permission | Deny camera/location/notification permission | P1/P2 |
| Deep link | Open protected deep link | P1 |
| Push notification | Tap notification and open correct screen | P1 |
| Poor network | Request fails gracefully | P2 |
| Offline | App shows offline state | P1/P2 |
| Crash risk | App does not crash during core flow | P1 |

---

## 10. Flakiness Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Device performance variation | Test may be slow | Use realistic timeout and stable waits |
| Unstable locator | Random failures | Use accessibility IDs |
| Push delivery timing | Non-deterministic test | Use controlled notification tooling |
| Network instability | False failures | Control network where possible |
| App animation timing | Timing failures | Wait for visible screen/state |
| Device farm queue | Delayed execution | Mark as environment dependency |

---

## 11. Cleanup Needs

| Cleanup Item | Required | Method |
|---|---|---|
| App session cleanup | Yes / No | Logout or reset app state |
| Test user state | Yes / No | Reset backend state if needed |
| Created data | Yes / No | API cleanup or test data reset |
| Device permissions | Yes / No | Reset permissions if needed |

---

## 12. Human Approval Points

| Item | Approval Needed | Reason |
|---|---|---|
| Real customer account usage | Yes | Sensitive data risk |
| Production app/environment | Yes | Production impact risk |
| Push notification to real users | Yes | External user impact |
| Payment flow | Yes | Financial risk |
| Device farm cost usage | If applicable | Cost control |
| Security-sensitive mobile scenario | Yes | Human review required |

---

## 13. Generated vs Executed Note

This Appium output is a generated automation draft.

It must not be reported as passed, verified, executed, or release-ready unless the test is actually run and execution evidence exists.

---

## 14. References

- references/mobile-testing/mobile-testing-patterns.md
- references/automation/automation-generation-patterns.md
- .github/instructions/playwright.instructions.md
