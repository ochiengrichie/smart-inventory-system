from flask import Blueprint, render_template, redirect, url_for, flash,abort
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, RegisterForm
from app.models import User
from app import db, login_manager
from functools import wraps

auth_bp = Blueprint("auth", __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function



@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar()
        if not user :
            flash("Email not found\n Register instead?", "info")
            return redirect(url_for("auth.register"))
        elif not check_password_hash(user.password, form.password.data):
            flash("Wrong password")
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for("dashboard.dashboard"))
    return render_template("login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar():
            flash("Email already registered\n Login instead?", "info")
            return redirect(url_for("auth.login"))
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            role=form.role.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("dashboard.dashboard"))
    return render_template("register.html", form=form)

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("dashboard.landing"))
