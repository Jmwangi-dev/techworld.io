# routes/__init__.py
# Leave this file empty

# routes/auth.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from services import user_service

auth_bp = Blueprint('auth', __name__)

# Auth routes and views

# routes/product.py
from flask import Blueprint, render_template
from models import db, Product

product_bp = Blueprint('product', __name__)

# Product routes and views

# routes/cart.py
from flask import Blueprint, render_template
from models import db, Cart
from services import cart_service

cart_bp = Blueprint('cart', __name__)

# Cart routes and views

# routes/order.py
from flask import Blueprint, render_template
from models import db, Order
from services import order_service

order_bp = Blueprint('order', __name__)

# Order routes and views

# routes/user.py
from flask import Blueprint, render_template
from models import db, User
from services import user_service

user_bp = Blueprint('user', __name__)

# User routes and views
