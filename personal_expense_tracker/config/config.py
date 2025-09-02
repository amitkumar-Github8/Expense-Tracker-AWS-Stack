import os

# Flask config variables loaded via from_pyfile
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///expense.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True

# Flask-Migrate
MIGRATE_DIRECTORY = os.getenv("MIGRATIONS_DIR", "migrations")
