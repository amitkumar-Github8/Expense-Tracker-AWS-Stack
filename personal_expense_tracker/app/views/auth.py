from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models.user import User
from .. import db
from ..forms.auth import LoginForm, RegisterForm


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash("Logged in successfully.", "success")
            next_page = request.args.get("next") or url_for("main.dashboard")
            return redirect(next_page)
        flash("Invalid email or password", "danger")
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for("main.index"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter((User.email == form.email.data.lower()) | (User.username == form.username.data)).first():
            flash("Email or username already exists", "warning")
            return render_template("auth/login.html", form=form, register=True)
        user = User(email=form.email.data.lower(), username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/login.html", form=form, register=True)
