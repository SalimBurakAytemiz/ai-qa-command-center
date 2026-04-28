# Architecture Diagram

## 1. Purpose

This document shows the high-level architecture of AI QA Command Center.

The diagram is intentionally framework-focused.

It does not represent a completed SaaS application, live dashboard, autonomous execution engine, or live integration platform.

---

## 2. High-Level Architecture

Mermaid source:

~~~mermaid
flowchart TD
    A[Feature / Product Input] --> B[Input Templates]
    B --> C[Agent Registry]
    C --> D[Prompt Library]
    D --> E[Workflow Layer]

    E --> F[Generated QA Output Package]

    F --> F1[Product Testing Context]
    F --> F2[Test Strategy]
    F --> F3[Test Plan]
    F --> F4[Test Cases]
    F --> F5[API Validation Plan]
    F --> F6[DB Validation Plan]
    F --> F7[Release Readiness Draft]

    F --> G[Output Review]
    G --> H[Human Approval Gates]

    H --> I[Execution Planning]
    I --> J[Execution Evidence Template]

    F --> K[Automation Candidate Review]
    K --> L[Automation Draft Examples]

    F --> M[Integration Drafts]
    M --> N[Integration Dry-Run Examples]

    H --> O[Dashboard Operator Workflow]

    P[Reference Library] --> D
    Q[Templates] --> B
    R[Validation Scripts] --> S[GitHub Actions CI]
    S --> T[Repository Health Signal]

    U[Product Packaging Docs] --> V[Sales / Demo / Onboarding]
~~~

---

## 3. Layer Responsibilities

| Layer | Responsibility |
|---|---|
| Input Templates | Capture structured feature, API, DB, UI, and acceptance criteria context |
| Agent Registry | Defines agents, teams, model routing, token policy, and permission policy |
| Prompt Library | Provides role-specific instructions for QA agents |
| Workflow Layer | Defines how work moves from intake to routing, generation, review, and approval |
| Output Package | Contains generated planning artifacts |
| Output Review | Reviews generated outputs for quality, risk, and safety |
| Human Approval Gates | Prevents unsafe external actions and false release claims |
| Execution Evidence | Documents real manual or automated execution evidence |
| Automation Drafts | Shows future automation draft structure without claiming execution |
| Integration Dry-Runs | Shows external action previews without creating real tickets/messages |
| Dashboard Workflow | Defines how a future operator dashboard should behave |
| Validation Scripts | Validate repository structure and required file coverage |
| GitHub Actions CI | Runs validation automatically on push or pull request |
| Product Packaging Docs | Explains how to present, demo, price, and sell the framework honestly |

---

## 4. Generated vs Executed Boundary

~~~mermaid
flowchart LR
    A[Generated Planning Artifact] --> B[Human Review]
    B --> C{Execution Happened?}

    C -- No --> D[Planning Use Only]
    C -- Yes --> E[Execution Evidence]

    E --> F[Human Approval]
    F --> G[Decision / Release Input]

    D --> H[Do Not Claim Passed]
    D --> I[Do Not Claim Verified]
    D --> J[Do Not Claim Release Ready]
~~~

---

## 5. External Action Boundary

~~~mermaid
flowchart TD
    A[Generated Integration Draft] --> B[Dry-Run Preview]
    B --> C{Human Approval?}

    C -- No --> D[Do Not Send / Do Not Create]
    C -- Yes --> E[Approved External Action]

    E --> F[Jira / Trello / GitHub / Slack / Other]
~~~

---

## 6. Current Implementation Reality

Current implemented state:

- Repository framework exists.
- Prompt library exists.
- Demo feature packs exist.
- Output examples exist.
- Automation draft examples exist.
- Integration dry-run examples exist.
- Dashboard workflow documentation exists.
- Validation scripts exist.
- GitHub Actions CI exists.

Not implemented yet:

- Real SaaS dashboard.
- Real automation generation engine.
- Real test execution engine.
- Real live external integrations.
- Real execution evidence import pipeline.

---

## 7. Safety Principle

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.
