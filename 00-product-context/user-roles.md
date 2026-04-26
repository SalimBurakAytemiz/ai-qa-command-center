# User Roles

## Guest User

A user who can access public areas without authentication.

Validation focus:

- Public pages
- Login-required actions
- Redirect behavior
- Unauthorized access restrictions

## Registered User

A normal authenticated user.

Validation focus:

- Login session
- Profile actions
- Content access
- Notifications
- Web and mobile consistency
- Firebase event tracking

## Admin User

A user who performs operational actions in the admin panel.

Validation focus:

- CRUD operations
- User management
- Content management
- Permission boundaries
- Audit log creation
- Bulk actions

## Super Admin

A user with the highest level of permission.

Validation focus:

- Role management
- Permission management
- System configuration
- Critical actions
- Security-sensitive operations

## Content Manager

A user responsible for creating and publishing CMS content.

Validation focus:

- Content creation
- Content editing
- Content publishing
- Content visibility on web and mobile
- CMS-to-product synchronization

## Operation User

A user responsible for approval, monitoring, and operational workflows.

Validation focus:

- Approval and rejection flows
- Status changes
- Reporting
- Operational history
- Admin panel consistency