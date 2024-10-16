from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from src.controllers.auth_controller import auth_bp, init_app
from src.controllers.payment_controller import payment_bp
from src.controllers.order_controller import order_bp
from flask_mail import Mail
from src.middlewares.errors import ErrorHandlers
import logging

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGODB_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Mail Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialize MongoDB
mongo = PyMongo(app)

# Initialize the auth controller with MongoDB instance
init_app(mongo)

# Initialize Mail
mail = Mail(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()
    ]
)

# Register the auth blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(order_bp)
app.register_blueprint(payment_bp)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return jsonify(message="Welcome to the Order Processing API")

# Register the error handlers
app.register_error_handler(404, ErrorHandlers.not_found)
app.register_error_handler(400, ErrorHandlers.bad_request)
app.register_error_handler(401, ErrorHandlers.unauthorized)
app.register_error_handler(500, ErrorHandlers.internal_error)
app.register_error_handler(Exception, ErrorHandlers.handle_exception)

if __name__ == '__main__':
    app.run(debug=True)
