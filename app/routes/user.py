#!/usr/bin/python3
"""User routes for the task tracker"""

from flask import Blueprint, jsonify, request
from models.user import User
import models

# Create a blueprint for user routes
user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User(**data)
    models.storage.new(user)
    models.storage.save()
    return jsonify(user.to_dict()), 201


@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID"""
    user = models.storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    models.storage.delete(user)
    models.storage.save()
    return jsonify({"message": "User deleted successfully"}), 200

