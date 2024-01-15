# admin_panel.py
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, render_template
from models import db, Product, Order, User
# Import other necessary models and modules

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        # Customize the admin index view as needed
        return render_template('admin/index.html')

class ProductModelView(ModelView):
    # Customize the product model view
    column_searchable_list = ['name']
    form_columns = ['name', 'description', 'price', 'featured']

class OrderModelView(ModelView):
    # Customize the order model view
    column_searchable_list = ['user.username', 'status']
    form_columns = ['user', 'items', 'total', 'status']

class UserModelView(ModelView):
    # Customize the user model view
    column_searchable_list = ['username', 'email']
    form_columns = ['username', 'email', 'password', 'is_admin']

admin = Admin(app, name='Admin Panel', index_view=MyAdminIndexView(template='admin/index.html'))
admin.add_view(ProductModelView(Product, db.session))
admin.add_view(OrderModelView(Order, db.session))
admin.add_view(UserModelView(User, db.session))
# Add more model views for other entities as needed
