# Runnable Test Skeleton

## Purpose

This folder contains the first runnable test skeleton for AI QA Command Center.

Current scope:

- Playwright web test skeleton
- API pytest skeleton
- DB validation Python skeleton
- k6 performance smoke skeleton

These tests are intentionally environment-driven.

If the required environment variables are not provided, tests should skip or behave safely.

---

## Playwright

Location:

- `06-tests/playwright/`

Install:

~~~bash
cd 06-tests/playwright
npm install
npx playwright install
~~~

Run:

~~~bash
WEB_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=password npm test
~~~

---

## API Tests

Location:

- `06-tests/api/`

Install:

~~~bash
cd 06-tests/api
pip install -r requirements.txt
~~~

Run:

~~~bash
API_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=password pytest
~~~

---

## DB Validation

Location:

- `06-tests/db-validation/`

Run:

~~~bash
SQLITE_DB_PATH=./demo.db DISABLED_TEST_USER_ID=user-disabled-1 python validate_login_state.py
~~~

---

## Performance Smoke

Location:

- `06-tests/performance/`

Run:

~~~bash
k6 run login-smoke.k6.js
~~~

With environment variables:

~~~bash
PERF_BASE_URL=http://localhost:3000 PERF_TEST_USER_EMAIL=test@example.com PERF_TEST_USER_PASSWORD=password k6 run login-smoke.k6.js
~~~

---

## Safety Note

Runnable test skeletons are not proof of product quality by themselves.

Execution evidence must be captured separately using:

- `templates/execution-evidence-template.md`

Do not claim pass/fail status unless the tests actually ran and evidence exists.
