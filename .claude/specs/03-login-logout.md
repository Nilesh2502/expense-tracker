# Spec: Login and Logout

## Overview
This feature allows users to securely authenticate their identity to access their personalized expense tracking dashboard. It implements a session-based authentication system where users provide their email and password, which are verified against the database. Once authenticated, a session is established to protect user-specific routes. Logout ensures that the session is terminated, preventing unauthorized access.

## Depends on
Step 02 (Registration)

## Routes
- `GET /login` — Displays the login form — public
- `POST /login` — Authenticates user and creates session — public
- `GET /logout` — Terminates user session and redirects to landing — logged-in

## Database changes
No database changes.

## Templates
- **Create:** None
- **Modify:** `templates/login.html` — update to use a proper HTML form with POST method

## Files to change
- `app.py` — implement the POST `/login` handler, the `/logout` handler, and session management using Flask's `session` object.
- `templates/login.html` — update the form to send data to `/login`.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] User can navigate to `/login` and see the login form.
- [ ] Submitting the form with valid credentials creates a session and redirects the user to a protected page (e.g., `/profile`).
- [ ] Submitting the form with invalid credentials shows a clear error message.
- [ ] Navigating to `/logout` clears the session and redirects the user to the landing page.
- [ ] Protected routes (like `/profile`) are inaccessible to users who are not logged in.
