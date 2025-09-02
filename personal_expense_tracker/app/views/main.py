from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models.expense import Expense


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    return redirect(url_for("main.dashboard"))


@main_bp.route("/dashboard")
@login_required
def dashboard():
    # Simple summary for demo
    total = 0
    if current_user.is_authenticated:
        total = sum([float(e.amount) for e in Expense.query.filter_by(user_id=current_user.id).all()])
    return render_template("main/dashboard.html", total_spent=total)
