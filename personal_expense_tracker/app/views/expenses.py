from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models.expense import Expense
from ..models.category import Category
from ..forms.expense import ExpenseForm


expenses_bp = Blueprint("expenses", __name__)


@expenses_bp.route("/", methods=["GET", "POST"])
@login_required
def list_create():
    form = ExpenseForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.filter_by(user_id=current_user.id).all()]
    if form.validate_on_submit():
        exp = Expense(
            amount=form.amount.data,
            description=form.description.data,
            date=form.date.data,
            user_id=current_user.id,
            category_id=form.category_id.data or None,
        )
        db.session.add(exp)
        db.session.commit()
        flash("Expense added", "success")
        return redirect(url_for("expenses.list_create"))
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    total = sum([float(e.amount) for e in expenses])
    cats = Category.query.filter_by(user_id=current_user.id).order_by(Category.name.asc()).all()
    return render_template("expenses/list.html", form=form, expenses=expenses, total=total, categories=cats)


@expenses_bp.route("/<int:expense_id>/delete", methods=["POST"]) 
@login_required
def delete(expense_id: int):
    exp = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first_or_404()
    db.session.delete(exp)
    db.session.commit()
    flash("Expense deleted", "info")
    return redirect(url_for("expenses.list_create"))
