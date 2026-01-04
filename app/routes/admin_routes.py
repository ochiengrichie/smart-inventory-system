from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.models import db, User
from app.routes.auth_routes import admin_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/users")
@login_required
@admin_required
def manage_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)

@admin_bp.route("/users/role/<int:user_id>", methods=["POST"])
@login_required
@admin_required
def change_role(user_id):
    user = User.query.get_or_404(user_id)
    new_role = request.form.get("role")
    if new_role not in ["admin", "staff"]:
        abort(400)
    user.role = new_role
    db.session.commit()
    flash(f"Role for {user.name} changed to {new_role}.", "success")
    return redirect(url_for("admin.manage_users"))

@admin_bp.route("/users/delete/<int:user_id>", methods=["POST"])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash("You cannot delete your own account.", "warning")
        return redirect(url_for("admin.manage_users"))
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.name} deleted successfully.", "info")
    return redirect(url_for("admin.manage_users"))
