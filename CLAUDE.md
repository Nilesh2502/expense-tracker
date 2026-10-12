# CLAUDE.md

This is an expense tracker which helps user tracker and split expenses.

## Build and Run
- Run the application: `python app.py` (runs on port 5001 by default)
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`

## Architecture
The project is a Flask-based web application for tracking expenses.

- `app.py`: Main application entry point and route definitions.
- `database/`: Contains database logic.
    - `db.py`: Expected to contain SQLite connection management (`get_db`), initialization (`init_db`), and seeding (`seed_db`).
- `templates/`: Jinja2 HTML templates for the frontend.
- `static/`: CSS and JavaScript assets.
