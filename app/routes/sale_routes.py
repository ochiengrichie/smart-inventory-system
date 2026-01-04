from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import db, Item, Sale
from app.forms import SaleForm
from datetime import datetime

sale_bp = Blueprint("sale", __name__)

# View all sales
@sale_bp.route("/")
@login_required
def sales():
    all_sales = Sale.query.order_by(Sale.id.desc()).all()
    return render_template("sales.html", sales=all_sales)

# Record a new sale
@sale_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_sale():
    form = SaleForm()
    form.item.choices = [(item.id, item.name) for item in Item.query.order_by(Item.name).all()]

    if form.validate_on_submit():
        item = Item.query.get(form.item.data)

        # Validate quantity
        if form.quantity.data > item.quantity:
            flash(f"Not enough stock. Available: {item.quantity}", "danger")
            return redirect(url_for("sale.new_sale"))

        # Reduce stock
        item.quantity -= form.quantity.data

        # Compute total price automatically
        total_price = form.quantity.data * item.price

        # Create sale record
        sale = Sale(
            item_id=item.id,
            quantity=form.quantity.data,
            total_price=total_price,
            date=datetime.utcnow()
        )

        db.session.add(sale)
        db.session.commit()

        flash("Sale recorded successfully!", "success")
        return redirect(url_for("sale.sales"))

    return render_template("sales_form.html", form=form)
