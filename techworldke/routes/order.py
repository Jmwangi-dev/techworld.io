# routes/order.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Order
from services import order_service, cart_service

order_bp = Blueprint('order', __name__)

@order_bp.route('/checkout')
@login_required
def checkout():
    cart_items = cart_service.get_cart_items(current_user.id)
    cart_subtotal = cart_service.calculate_cart_subtotal(cart_items)
    cart_total = cart_service.calculate_cart_total(cart_subtotal)
    return render_template('order/checkout.html', cart_items=cart_items, cart_subtotal=cart_subtotal, cart_total=cart_total)

@order_bp.route('/place_order', methods=['POST'])
@login_required
def place_order():
    order_id = order_service.create_order(current_user.id)
    flash('Order placed successfully. Thank you!', 'success')
    return redirect(url_for('order.view_order', order_id=order_id))

@order_bp.route('/order/<int:order_id>')
@login_required
def view_order(order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    return render_template('order/view_order.html', order=order)
