from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.expense import Expense


reports_bp = Blueprint("reports", __name__)


@reports_bp.route("/")
@login_required
def overview():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    total = sum([float(e.amount) for e in expenses])
    return render_template("reports/overview.html", total=total, count=len(expenses))
