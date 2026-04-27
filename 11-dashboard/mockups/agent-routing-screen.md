# Agent Routing Screen Mockup

## Purpose

This mockup defines the future agent routing screen.

## Main Goal

The screen should show:

- Which agents will run
- Why each agent was selected
- Which agents were skipped
- What context each agent receives
- Which model profile is recommended
- Whether fallback or review is required
- Human approval points

## Example Routing

| Agent | Status | Reason | Model Profile |
|---|---|---|---|
| Product Intake Agent | Selected | Product context needed | reasoning |
| Test Strategy Agent | Selected | Risk strategy needed | reasoning |
| Test Planning Agent | Selected | Test plan needed | reasoning |
| API Test Agent | Selected | API endpoints affected | api_backend |
| DB Validation Agent | Selected | Session/token DB impact | database |
| Web Functional Agent | Selected | Login UI affected | ui_web |
| Output Reviewer Agent | Selected | Critical output review | review |
| Native Mobile Agent | Skipped | Native mobile out of scope | none |
| Firebase Agent | Skipped | No analytics events defined | none |
| Performance Agent | Skipped | Performance out of current scope | none |

## Agent Status Values

| Status | Meaning |
|---|---|
| Selected | Agent should run |
| Skipped | Agent not needed |
| Optional | Agent may run if human approves |
| Blocked | Agent cannot run due to missing information |
| Review Required | Output must be reviewed |

## Safety Rule

The routing screen must not run all agents by default.

It should run only the agents needed for feature scope and risk.
