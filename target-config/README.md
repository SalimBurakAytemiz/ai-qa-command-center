# Target Configuration

## Purpose

Target configuration defines what product or environment AI QA Command Center should analyze and test.

This is the future input contract for:

- test selection
- agent routing
- orchestrator CLI
- web/API/socket/mobile execution
- evidence collection
- SaaS dashboard project setup

---

## Files

| File | Purpose |
|---|---|
| `target-config.example.yaml` | Safe example target configuration |
| `target-config.schema.json` | JSON Schema validation contract |

---

## Safety Rules

Do not commit real secrets.

Do not commit:

- real passwords
- real access tokens
- real refresh tokens
- production database URLs
- customer data
- private APK/AAB files
- private certificates
- production credentials

Use environment variable names instead.

Example:

~~~yaml
test_users:
  synthetic_user_env:
    email: "TEST_USER_EMAIL"
    password: "TEST_USER_PASSWORD"
~~~

The values are not stored in the config.

Only the environment variable names are stored.

---

## Production Safety

The default schema forbids unsafe production behavior:

- `allow_production` must be false
- `allow_real_customer_data` must be false
- `allow_destructive_db_actions` must be false
- `allow_high_load_performance_tests` must be false
- external integrations must stay in dry-run unless explicitly approved

---

## Future Use

This config will later be consumed by:

- target config validator
- orchestrator CLI
- test runner selector
- evidence collector
- dashboard backend
- SaaS workspace/project setup
