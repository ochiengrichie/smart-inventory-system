from flask import Blueprint, render_template, request
from flask_login import login_required
from app.models import Sale
from datetime import datetime, date, timedelta
import calendar
from app.routes.auth_routes import admin_required

report_bp = Blueprint("report", __name__)

@report_bp.route("/reports")
@login_required
@admin_required
def reports():
    today = date.today()
    filter_option = request.args.get("filter", "this_month")

    # Default range
    start_date = today.replace(day=1)
    end_date = today.replace(day=calendar.monthrange(today.year, today.month)[1])

    # Handle filters
    if filter_option == "last_month":
        first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_last_month = first_day_last_month.replace(day=calendar.monthrange(first_day_last_month.year, first_day_last_month.month)[1])
        start_date, end_date = first_day_last_month, last_day_last_month

    elif filter_option == "this_year":
        start_date = date(today.year, 1, 1)
        end_date = date(today.year, 12, 31)

    elif filter_option == "custom":
        start_date_str = request.args.get("start_date")
        end_date_str = request.args.get("end_date")
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

    # Query sales
    sales = Sale.query.filter(Sale.date >= start_date, Sale.date <= end_date).order_by(Sale.date.asc()).all()

    # Prepare chart data
    chart_labels = [s.date.strftime("%Y-%m-%d") for s in sales]
    chart_values = [s.total_price for s in sales]

    return render_template(
        "reports.html",
        chart_labels=chart_labels,
        chart_values=chart_values,
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
        filter_option=filter_option
    )
