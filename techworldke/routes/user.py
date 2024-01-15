# routes/user.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, User
from services import user_service

user_bp = Blueprint('user', __name__)

@user_bp.route('/account')
@login_required
def account():
    orders = user_service.get_user_orders(current_user.id)
    return render_template('user/user_account.html', orders=orders)

### `services/user_service.py`:
```python
# services/user_service.py
from models import db, User, Order

def get_user_orders(user_id):
    return Order.query.filter_by(user_id=user_id).all()

### `routes/base.py`:
```python
# routes/base.py
from flask import Blueprint, render_template
from flask_login import current_user

base_bp = Blueprint('base', __name__)

@base_bp.route('/')
def index():
    return render_template('base/index.html', user=current_user)

