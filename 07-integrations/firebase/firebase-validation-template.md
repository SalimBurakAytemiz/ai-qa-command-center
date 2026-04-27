# Firebase Validation Template

## Purpose

Use this template to prepare Firebase analytics validation drafts.

Important rule:

This is a planning template only.

Firebase events are not verified unless evidence exists from DebugView, analytics logs, BigQuery export, network logs, or approved tooling.

---

## 1. Feature or Flow

| Field | Value |
|---|---|
| Feature | |
| Platform | Web / iOS / Android / Mobile Web |
| Analytics Owner | |
| Human Approval Required | If production analytics or real user data is involved |

---

## 2. Events Covered

| Event Name | Trigger Action | Platform | Priority |
|---|---|---|---|
| | | | |

---

## 3. Event Parameters

| Event Name | Required Parameters | Optional Parameters | Sensitive Data Risk |
|---|---|---|---|
| | | | |

---

## 4. Screen View Checks

| Screen | Expected Event | Required Parameters | Priority |
|---|---|---|---|
| | | | |

---

## 5. User Property Checks

| User Property | Expected Values | Trigger | Risk |
|---|---|---|---|
| | | | |

---

## 6. Duplicate Event Risks

| Event | Duplicate Trigger | Recommended Validation |
|---|---|---|
| | | |

---

## 7. Missing Event Risks

| Event | Impact | Recommended Validation |
|---|---|---|
| | | |

---

## 8. Evidence Needed

| Evidence | Purpose |
|---|---|
| Firebase DebugView screenshot | Event existence and parameters |
| Event log export | Event count and timing |
| BigQuery export | Historical validation if enabled |
| Network log | Web analytics request validation |
| Device log | Native app event validation |

---

## 9. Human Approval

| Approval Item | Required | Reason |
|---|---|---|
| Use production analytics | Yes | Production data risk |
| Track personal data | Yes | Privacy risk |
| Send findings externally | Yes | External communication |

---

## 10. Final Note

Generated Firebase validation plans are not executed analytics results.
