from flask import Blueprint, request, render_template
from app.conroller.user_conroller import user_controller

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/api')


@auth_routes.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = request.get_json()
        if not user.get('email'):
            return "Missing email"
        if not user.get('name'):
            return "Missing name"
        if not user.get('password'):
            return "Missing password"
        
        return user_controller.create_user(user["name"], user["email"], user["password"])
    elif request.method == 'GET':
        return render_template('auth/register.html')
        
  
  
@auth_routes.route('/login', methods=['POST'])
def login():
    """Register a new user"""
    user = request.get_json()
    if not user.get('email'):
        return "Missing email"
    if not user.get('password'):
        return "Input password"
    return user_controller.login_user(user["email"], user["password"])
