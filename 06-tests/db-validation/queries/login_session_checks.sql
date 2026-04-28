-- Login session validation query examples.
-- Use only against a safe QA database.
-- Do not run against production without explicit human approval.

SELECT
  id,
  status
FROM users
WHERE id = :disabled_test_user_id;

SELECT
  id,
  user_id,
  created_at,
  revoked_at
FROM sessions
WHERE user_id = :disabled_test_user_id
  AND revoked_at IS NULL;
