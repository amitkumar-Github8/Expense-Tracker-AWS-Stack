from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models.category import Category
from ..forms.category import CategoryForm


categories_bp = Blueprint("categories", __name__)


@categories_bp.route("/", methods=["GET", "POST"])
@login_required
def list_create():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = Category(name=form.name.data, user_id=current_user.id)
        db.session.add(cat)
        db.session.commit()
        flash("Category added", "success")
        return redirect(url_for("categories.list_create"))
    categories = Category.query.filter_by(user_id=current_user.id).order_by(Category.name.asc()).all()
    return render_template("categories/list.html", form=form, categories=categories)
