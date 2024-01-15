# routes/cart.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Cart
from services import cart_service

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
@login_required
def view_cart():
    cart_items = cart_service.get_cart_items(current_user.id)
    cart_subtotal = cart_service.calculate_cart_subtotal(cart_items)
    cart_total = cart_service.calculate_cart_total(cart_subtotal)
    return render_template('cart/cart.html', cart_items=cart_items, cart_subtotal=cart_subtotal, cart_total=cart_total)

@cart_bp.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    cart_service.add_to_cart(current_user.id, product_id)
    flash('Item added to your cart', 'success')
    return redirect(url_for('product.product_list'))

@cart_bp.route('/remove_from_cart/<int:cart_item_id>')
@login_required
def remove_from_cart(cart_item_id):
    if cart_service.remove_from_cart(cart_item_id, current_user.id):
        flash('Item removed from your cart', 'success')
    else:
        flash('Failed to remove item from your cart', 'danger')

    return redirect(url_for('cart.view_cart'))
