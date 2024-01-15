# routes/product.py
from flask import Blueprint, render_template
from models import db, Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def product_list():
    products = Product.query.all()
    return render_template('product/product_list.html', products=products)

@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product/product_detail.html', product=product)
