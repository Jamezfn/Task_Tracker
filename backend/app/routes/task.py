"""Task routes for the task tracker"""
from flask import Flask, Blueprint, request, jsonify
from app.conroller.task_controller import task_controller

# Create a blueprint for task routes
task_routes = Blueprint('task_routes', __name__, url_prefix='/api')

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all user tasks"""
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(" ")[1]
        return task_controller.getTasks(token)
    return jsonify({"error": "Missing authorization header"}), 401

@task_routes.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Retrieve a specific task by ID"""
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(" ")[1]
        return task_controller.getTask(token, task_id)
    return jsonify({"error": "Missing authorization header"}), 401

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    if request.method == 'POST':
        task = request.get_json()
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(" ")[1]
        else:
            return jsonify({"error": "Missing authorization header"}), 401

        if not task["title"]: return jsonify({"error": "Missing title"}), 400
        if not task["description"]: return jsonify({"error": "Missing description"}), 400
        if not task["status"]: return jsonify({"error": "Missing status"}), 400
        if not task["start_date"]: return jsonify({"error": "Missing start date"}), 400
        if not task["due_date"]: return jsonify({"error": "Missing due date"}), 400

        return task_controller.createTask(token, task["title"], task["description"], task["status"], task["start_date"], task["due_date"])
    

@task_routes.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        task_data = request.get_json()
        if not task_data: return jsonify({"error": "No data provided"}), 400

        title = task_data.get("title")
        description = task_data.get("description")
        status = task_data.get("status")
        start_date = task_data.get("start_date")
        due_date = task_data.get("due_date")


        return task_controller.updateTask(token, task_id, title, description, status, start_date, due_date)
    return jsonify({"error": "Unthorised user or token expired"}), 401

@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        return task_controller.deleteTask(token, task_id)
    return jsonify({"error": "Unthorised user or token expired"}), 401

@task_routes.route('/tasks/<task_id>/tags', methods=['GET'])
def get_task_tags(task_id):
    """Retrieve all tags associated with a task"""
    pass

@task_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['POST'])
def add_tag_to_task(task_id, tag_id):
    """Add a tag to a task"""
    pass

@task_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['DELETE'])
def remove_tag_from_task(task_id, tag_id):
    """Remove a tag from a task"""
    pass

