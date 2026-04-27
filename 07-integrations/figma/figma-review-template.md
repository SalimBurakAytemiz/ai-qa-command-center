# Figma Review Template

## Purpose

Use this template to prepare Figma-based QA review drafts.

Important rule:

This is a review template only.

AI agents must not claim UI validation is completed unless the design and implementation were actually compared with evidence.

---

## 1. Design Metadata

| Field | Value |
|---|---|
| Figma File | |
| Feature | |
| Screen or Flow | |
| Platform | Web / Mobile Web / iOS / Android |
| Design Version | |
| Reviewer | |
| Human Approval Required | If design decision or release impact exists |

---

## 2. Screens Covered

| Screen | Platform | Priority | Notes |
|---|---|---|---|
| | | | |

---

## 3. UI Elements To Validate

| Element | Expected Design Behavior | Priority |
|---|---|---|
| Button | | |
| Form field | | |
| Error message | | |
| Empty state | | |
| Loading state | | |
| Success state | | |

---

## 4. Responsive or Device Checks

| Viewport or Device | Expected Behavior | Priority |
|---|---|---|
| Mobile small | | |
| Mobile large | | |
| Tablet | | |
| Desktop | | |

---

## 5. Accessibility Review Points

| Area | Expected Behavior | Notes |
|---|---|---|
| Labels | Inputs have clear labels | |
| Contrast | Text and background are readable | |
| Keyboard navigation | Main flow can be navigated | |
| Error visibility | Error messages are clear | |
| Touch target | Buttons are tappable on mobile | |

---

## 6. Design vs Implementation Risks

| Risk | Impact | Recommended Validation |
|---|---|---|
| Missing error state | Users may not understand failure | Compare implementation to design |
| Missing loading state | Duplicate submit risk | Validate UI behavior |
| Mobile layout break | Mobile users blocked | Responsive test required |
| Wrong role-specific UI | Permission confusion | Role-based UI validation |

---

## 7. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| | | |

---

## 8. Evidence Needed

| Evidence | Purpose |
|---|---|
| Figma screen link | Design reference |
| Implementation screenshot | Comparison |
| Video | Interaction review |
| Browser/device info | Reproducibility |

---

## 9. Final Note

Generated Figma review drafts are not executed UI validation results.

Human review is required for design-impacting decisions.
