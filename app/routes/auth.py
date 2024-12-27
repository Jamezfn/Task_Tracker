from flask import Blueprint, request
from app.conroller.user_conroller import user_controller

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/api')


@auth_routes.route('/register', methods=['POST'])
def register():
    user = request.get_json()
    if not user.get('email'):
        return "Missing email"
    if not user.get('name'):
        return "Missing name"
    if not user.get('password'):
        return "Missing password"
    
    user_controller.create_user(user["name"], user["email"], user["password"])
        
    
    
    # register logic
    return "User registered successfully"
  
@auth_routes.route('/login', methods=['POST'])
def login():
    """Register a new user"""
    user = request.get_json()
    if not user.get('email'):
        return "Missing email"
    if not user.get('password'):
        return "Input password"
    for person in users:
        if person["email"] == user["email"]:
            if person["password"] == user["password"]:
                return "Login Successful"
            return "Incorrect passwords"
        return "User does not exist"