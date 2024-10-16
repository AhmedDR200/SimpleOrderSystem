from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

# Initialize the blueprint
auth_bp = Blueprint('auth', __name__)

# Initialize MongoDB (Assuming mongo is already initialized in app.py)
mongo = None

# Function to set the MongoDB instance
def init_app(mongo_instance):
    global mongo
    mongo = mongo_instance

# Function to generate JWT token
def generate_token(user_id):
    token = create_access_token(identity=user_id)
    return token

# Signup route
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    age = data.get('age')

    if mongo.db.users.find_one({'email': email}):
        return jsonify(message="Email already exists"), 400
    
    hashed_password = generate_password_hash(password)
    new_user = {
        'username': username,
        'password': hashed_password,
        'email': email,
        'age': age
    }
    mongo.db.users.insert_one(new_user)

    token = generate_token(email)


    # Prepare the response with the user's details (excluding the password)
    response_user = {
        'username': username,
        'email': email,
        'age': age,
    }
    return jsonify(message="User created successfully", user=response_user, token = token), 201

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = mongo.db.users.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        # Generate JWT token upon login
        token = generate_token(str(user['_id']))
        
        # Prepare the response with the user's details (excluding the password)
        response_user = {
            'username': user['username'],
            'email': user['email'],
            'age': user['age']
        }
        return jsonify(message="Login successful", user=response_user, token = token), 200
    return jsonify(message="Invalid email or password"), 401
