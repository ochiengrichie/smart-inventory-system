from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import extract, func
from app.models import Item
from app import db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def landing():
    return render_template("landing.html")

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    # Get all items
    items = Item.query.all()
    total_products = len(items)
    total_quantity = sum(item.quantity for item in items)
    low_stock_items = Item.query.filter(Item.quantity < 5).all()
    recent_items = Item.query.order_by(Item.id.desc()).limit(5).all()

    # Get actual monthly counts from database
    results = (
        db.session.query(extract('month', Item.date_added).label('month'), func.count(Item.id))
        .group_by('month')
        .all()
    )

    # Prepare month labels and counts
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    counts = [0] * 12

    for month, count in results:
        counts[int(month) - 1] = count

    return render_template(
        "dashboard.html",
        total_products=total_products,
        total_quantity=total_quantity,
        low_stock_items=low_stock_items,
        recent_items=recent_items,
        months=months,
        counts=counts
    )

@dashboard_bp.route("/low_stock")
@login_required
def low_stock():
    low_stock_items = Item.query.filter(Item.quantity < 5).all()
    return render_template("low_stock.html", low_stock_items=low_stock_items)


