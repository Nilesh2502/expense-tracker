# Spec: Registration

## Overview
This feature allows new users to create an account on Spendly. It provides a registration form that collects a user's name, email, and password, validates the input, and stores the user securely in the database. This is a foundational step to enable personalized expense tracking. On success it shows user a success message and then redirect to the login page.

## Depends on
Step 01 (Database Setup)

## Routes
- `GET /register` — Displays the registration form — public
- `POST /register` — Processes the registration form and creates the user — public

## Database changes
No database changes. The `users` table already exists with `name`, `email`, `password_hash`, and `created_at` columns.

## Templates
- **Create:** None (the registration page already exists as a placeholder)
- **Modify:** `templates/register.html` — update to use a proper HTML form with POST method

## Files to change
- `app.py` — implement the POST `/register` handler and add form validation
- `templates/register.html` — update the form to send data to `/register`

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
- [ ] User can navigate to `/register` and see the registration form.
- [ ] Submitting the form with valid data creates a new user in the `users` table.
- [ ] Password is stored as a hash in the database, not as plain text.
- [ ] Duplicate emails are handled gracefully with an error message.
- [ ] User is redirected to the login page after successful registration.
