from flask import render_template
from flask_login import login_required

@admin_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Add logic to retrieve statistics data from your database
    total_sales = get_total_sales()
    total_orders = get_total_orders()
    total_revenue = get_total_revenue()

    return render_template('admin/index.html', total_sales=total_sales, total_orders=total_orders, total_revenue=total_revenue)
