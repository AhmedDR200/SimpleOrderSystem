from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from controllers.auth_controller import auth_bp, init_app
from errors import not_found, bad_request, unauthorized, internal_error, handle_exception

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGODB_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

# Initialize the auth controller with MongoDB instance
init_app(mongo)

# Register the auth blueprint
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return jsonify(message="Welcome to the User API")

# Custom error handler for 404 Not Found
app.errorhandler(404)(not_found)
app.errorhandler(400)(bad_request)
app.errorhandler(401)(unauthorized)
app.errorhandler(500)(internal_error)
app.errorhandler(Exception)(handle_exception)

if __name__ == '__main__':
    app.run(debug=True)
