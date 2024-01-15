# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# models/user.py
from . import db

class User(db.Model):
    # User model definition

# models/product.py
from . import db

class Product(db.Model):
    # Product model definition

# models/cart.py
from . import db

class Cart(db.Model):
    # Cart model definition

# models/order.py
from . import db

class Order(db.Model):
    # Order model definition
