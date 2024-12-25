from flask import Blueprint

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/api')

@auth_routes.route('/register', methods=['POST', 'GET'])
def register():
    return "<h1>Welcome to register page</h1>"

@auth_routes.route('/login', methods=['POST', 'GET'])
def login():
    """Register a new user"""
    return "<h1>Welcome to login page</h1>"