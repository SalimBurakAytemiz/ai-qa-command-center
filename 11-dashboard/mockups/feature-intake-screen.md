# Feature Intake Screen Mockup

## Purpose

This mockup defines the future feature intake screen.

## Main Goal

The feature intake screen should collect:

- Feature name
- Feature summary
- Business purpose
- User roles
- Platforms
- Acceptance criteria
- API notes
- DB notes
- UI notes
- Known risks
- Missing information
- Human instructions

## Main Sections

| Section | Purpose |
|---|---|
| Feature Name | Identify feature |
| Feature Summary | Explain what the feature does |
| Business Purpose | Explain why feature exists |
| Affected Platforms | Support agent routing |
| User Roles | Support permission and scenario design |
| Acceptance Criteria | Support traceable test cases |
| API Notes | Support API validation |
| DB Notes | Support DB validation |
| UI Notes | Support web/mobile validation |
| Known Risks | Support risk analysis |
| Missing Information | Prevent unsupported assumptions |
| Human Notes | Add human test leader instruction |

## Required Fields

| Field | Required | Reason |
|---|---|---|
| Feature Name | Yes | Needed for traceability |
| Feature Summary | Yes | Needed for product understanding |
| Affected Platforms | Yes | Needed for agent routing |
| User Roles | Yes | Needed for permission and scenario design |
| Acceptance Criteria | Recommended | Needed for test coverage |

## Validation Rules

The screen should warn when:

- Feature summary is empty
- No platform is selected
- No user role is defined
- Acceptance criteria are missing
- API is selected but API notes are empty
- Database is selected but DB notes are empty
- Security-sensitive data is pasted
- Production data is pasted

## Safety Rule

The screen should warn users not to paste API keys, passwords, production credentials, customer personal data, payment data, or security secrets.
