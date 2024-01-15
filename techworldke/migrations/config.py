from flask import Flask
from models import db
from services import UserService, ProductService  # Import other services as needed
from config.development import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

# Initialize services
user_service = UserService()
product_service = ProductService()
# Initialize other services as needed

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
