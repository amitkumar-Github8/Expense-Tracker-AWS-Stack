# Personal Expense Tracker (Flask)

A simple, clean Flask app to track spending, organize categories, and view a basic dashboard. Uses SQLite by default and works with Postgres/MySQL via `DATABASE_URL`.

## Features
- Login / Register (Flask-Login)
- Add expenses with amount, date, description, and category
- Manage categories
- Dashboard + simple reports (Chart.js)
- SQLAlchemy ORM + Flask-Migrate
- Bootstrap 5 UI

## Prerequisites
- Python 3.10+

## Setup (Windows)
From the `personal_expense_tracker` folder:

1) Create and activate a virtual environment

Git Bash:
```bash
python -m venv .venv
source .venv/Scripts/activate
```

PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) (Optional) Configure environment
- Copy `.env.example` to `.env`
- Set values like:
	- `SECRET_KEY` (any random string)
	- `DATABASE_URL` (defaults to `sqlite:///expense.db`)

## Run locally
```bash
python run.py
```
Open http://127.0.0.1:5000

On first run, SQLite tables are created automatically in development.

## Database migrations (optional)
If you later change models and want Alembic migrations:

Set the Flask app (only for CLI commands):

Git Bash:
```bash
export FLASK_APP='app:create_app'
```

PowerShell:
```powershell
$env:FLASK_APP = 'app:create_app'
```

Then run:
```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

## Tests
```bash
pytest -q
```

## Project structure (short)
```
personal_expense_tracker/
	app/               # Flask app (views, models, forms, templates, static)
	config/            # Config loaded by app factory
	migrations/        # Alembic (created after init)
	run.py             # Local dev entry point
	requirements.txt   # Python deps
```


---
Tip: In VS Code, you can use the “Install dependencies” task in `.vscode/tasks.json` to set up the environment.
