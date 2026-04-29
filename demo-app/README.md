# Demo App

## Purpose

This is the first runnable target application for AI QA Command Center.

It provides a small FastAPI + SQLite login API that can be used by:

- API pytest skeleton
- AJV API contract tests
- DB validation skeleton
- future Playwright frontend tests

---

## Install

~~~bash
cd demo-app
pip install -r requirements.txt
~~~

---

## Seed Database

~~~bash
python -m app.seed
~~~

---

## Run API

~~~bash
uvicorn app.main:app --reload --port 3000
~~~

Health check:

~~~bash
GET http://localhost:3000/health
~~~

Login endpoint:

~~~bash
POST http://localhost:3000/api/auth/login
~~~

Request:

~~~json
{
  "email": "test@example.com",
  "password": "Password123!"
}
~~~

---

## Test With AJV API Contract Tests

From another terminal:

~~~bash
cd 06-tests/api-ajv
npm install
API_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=Password123! npm test
~~~

---

## Test With Python API Tests

~~~bash
cd 06-tests/api
pip install -r requirements.txt
API_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=Password123! pytest
~~~

---

## DB Validation

~~~bash
python demo-app/app/seed.py
SQLITE_DB_PATH=demo-app/demo.db DISABLED_TEST_USER_ID=user-disabled-1 python 06-tests/db-validation/validate_login_state.py
~~~

---

## Safety Note

This demo app is local-only.

Do not use production credentials or real customer data.
