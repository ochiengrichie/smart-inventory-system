# app/routes/inventory_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import db, Item
from app.forms import ItemForm
from app.routes.auth_routes import admin_required

inventory_bp = Blueprint("inventory", __name__)

# -----------------------------
# VIEW ALL ITEMS
# -----------------------------
@inventory_bp.route("/inventory")
@login_required
def inventory():
    """Display all items in inventory."""
    items = Item.query.order_by(Item.id.desc()).all()
    return render_template("inventory.html", items=items)


# -----------------------------
# ADD NEW ITEM
# -----------------------------
@inventory_bp.route("/inventory/add", methods=["GET", "POST"])
@login_required
def add_item():
    """Add a new item to the inventory."""
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(
            name=form.name.data,
            description=form.description.data,
            category=form.category.data,
            quantity=form.quantity.data,
            price=form.price.data,
            supplier=form.supplier.data,
        )
        db.session.add(item)
        db.session.commit()
        flash("New item added successfully!", "success")
        return redirect(url_for("inventory.inventory"))
    return render_template("inventory_form.html", form=form, title="Add Item")


# -----------------------------
# EDIT ITEM
# -----------------------------
@inventory_bp.route("/inventory/edit/<int:item_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_item(item_id):
    """Edit item details."""
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)

    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        item.category = form.category.data
        item.quantity = form.quantity.data
        item.price = form.price.data
        item.supplier = form.supplier.data

        db.session.commit()
        flash("Item updated successfully!", "info")
        return redirect(url_for("inventory.inventory"))

    return render_template("inventory_form.html", form=form, title="Edit Item")


# -----------------------------
# DELETE ITEM
# -----------------------------
@inventory_bp.route("/inventory/delete/<int:item_id>", methods=["POST"])
@login_required
@admin_required
def delete_item(item_id):
    """Delete an item from inventory."""
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Item deleted successfully!", "warning")
    return redirect(url_for("inventory.inventory"))
