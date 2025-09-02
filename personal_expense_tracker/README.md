# Expense Tracker Pro (Flask, AWS-ready)

A full-featured Flask web application for tracking personal expenses, managing budgets, and viewing analytics. The app is structured for local development and can be deployed on AWS (EC2 for hosting, RDS for DB, CloudWatch for logs/metrics, and SNS for alerts).

## Features
- User authentication (login/register)
- Expense and category management
- Dashboard and simple reports (Chart.js)
- SQLAlchemy models and Flask-Migrate
- Bootstrap 5 UI with a clean, professional design

## Quick Start

1) Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

2) Optional: set env vars (see `.env.example`)

3) Initialize the database (auto-creates in dev when running)

```bash
python run.py
```

Visit http://127.0.0.1:5000

## Database migrations

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

## Tests

```bash
pytest -q
```

## Deploying to AWS (outline)
- Use RDS PostgreSQL/MySQL and set `DATABASE_URL`.
- Run behind Gunicorn/Nginx on EC2/Elastic Beanstalk or containers.
- Configure environment variables (SECRET_KEY, DATABASE_URL, etc.).
- Optionally serve static files via S3/CloudFront.

---
This repo is a solid foundation—extend with richer reports, validations, and role-based permissions as needed.
