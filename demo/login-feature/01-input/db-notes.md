# Login Feature Database Notes

## 1. Feature Name

User Login

---

## 2. Database Overview

The login feature may read user records and update authentication-related fields.

The exact schema is not confirmed, so this demo uses entity-level validation instead of strict table names.

---

## 3. Entities or Tables

| Entity or Table | Purpose | Notes |
|---|---|---|
| users | Stores user account data | Exact table name needs confirmation |
| sessions | Stores active sessions if server-side session is used | May not exist if JWT-only |
| refresh_tokens | Stores refresh tokens if refresh token flow exists | Needs confirmation |
| audit_logs | Stores security-sensitive login events if supported | Optional |

---

## 4. Expected State Changes

| User Action or API Action | Before State | After State | Priority |
|---|---|---|---|
| Successful login | Active user exists | last_login_at may update and session/token may be created | P1 |
| Failed login | User exists or does not exist | failed login state may be recorded if supported | P2 |
| Disabled user login attempt | Disabled user exists | No active session should be created | P1 |
| Logout | Active session exists | Session/token should be invalidated if server-side tracking exists | P2 |

---

## 5. Insert Behavior

Possible inserts:

- session record
- refresh token record
- audit log record

Exact behavior needs confirmation.

---

## 6. Update Behavior

Possible updates:

- users.last_login_at
- users.failed_login_count
- sessions.revoked_at
- refresh_tokens.revoked_at

Exact fields need confirmation.

---

## 7. Delete or Soft Delete Behavior

Login should not delete user data.

Logout may revoke or expire session/token data.

---

## 8. Relationship Rules

- Session or token record should belong to the correct user.
- Admin and registered users must not share session ownership.
- Disabled users must not get active sessions.

---

## 9. Audit and Timestamp Rules

Possible audit/timestamp checks:

- last_login_at updates after successful login
- failed login event recorded if supported
- session created_at exists
- session revoked_at exists after logout if supported

---

## 10. Duplicate and Orphan Risks

| Risk | Trigger | Recommended Validation |
|---|---|---|
| Duplicate sessions | Multiple login attempts | Confirm expected session behavior |
| Orphan sessions | User disabled or deleted | Confirm sessions are invalidated |
| Wrong user session | Auth bug | Confirm session belongs to correct user |

---

## 11. Missing DB Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact table names | Needed for DB validation | Cannot write exact DB checks |
| Token/session storage method | Needed for session validation | Cannot confirm DB impact |
| Audit logging rules | Needed for security validation | Audit expectations unclear |
| Disabled user handling | Needed for negative DB validation | Session prevention must be confirmed |
