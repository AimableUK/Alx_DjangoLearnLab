# Permissions & Groups Setup

## Custom Permissions
Defined in `Post` model (`accounts/models.py`):
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → all permissions

## Usage in Views
- Protected with `@permission_required('accounts.can_edit', raise_exception=True)`
- Users are restricted based on assigned group.

## Testing
1. Create users in Django Admin.
2. Assign them to groups (Viewers, Editors, Admins).
3. Verify that only allowed actions are accessible.
