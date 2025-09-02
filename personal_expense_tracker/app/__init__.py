from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .utils.error_handlers import register_error_handlers
from .utils.template_helpers import register_template_helpers
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(test_config: dict = None) -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    # Load configuration
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.py")
    app.config.from_pyfile(config_path, silent=True)

    if test_config:
        app.config.update(test_config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from .views.main import main_bp
    from .views.auth import auth_bp
    from .views.expenses import expenses_bp
    from .views.categories import categories_bp
    from .views.reports import reports_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(expenses_bp, url_prefix="/expenses")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.register_blueprint(reports_bp, url_prefix="/reports")

    # Helpers & errors
    register_template_helpers(app)
    register_error_handlers(app)

    # Require login globally except for auth and static endpoints
    @app.before_request
    def require_login():
        from flask_login import current_user
        from flask import flash
        endpoint = request.endpoint or ""
        is_auth = endpoint.startswith("auth.")
        is_static = endpoint == "static"
        if not is_auth and not is_static and not current_user.is_authenticated:
            if request.method == "GET":
                flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login", next=request.url))

    # Create DB tables in dev if not exists
    with app.app_context():
        from .models import user, category, expense, budget  # noqa: F401
        db.create_all()

    return app
