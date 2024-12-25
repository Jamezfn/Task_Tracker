#!/usr/bin/python3
"""Task routes for the task tracker"""

from flask import Blueprint, jsonify, request
from models.task import Task
from models.tag import Tag
import models

# Create a blueprint for task routes
task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks"""
    tasks = models.storage.all(Task).values()
    task_list = [task.to_dict() for task in tasks]
    return jsonify(task_list), 200

@task_routes.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Retrieve a specific task by ID"""
    task = models.storage.get(Task, task_id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    title = data.get('title')
    description = data.get('description', '')
    if not title:
        return jsonify({"error": "Task title is required"}), 400

    task = Task(title=title, description=description)
    models.storage.new(task)
    models.storage.save()
    return jsonify(task.to_dict()), 201

@task_routes.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    task = models.storage.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    task.save()
    return jsonify(task.to_dict()), 200

@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    task = models.storage.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    models.storage.delete(task)
    models.storage.save()
    return jsonify({"message": "Task deleted successfully"}), 200

@task_routes.route('/tasks/<task_id>/tags', methods=['GET'])
def get_task_tags(task_id):
    """Retrieve all tags associated with a task"""
    task = models.storage.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    tags = [tag.to_dict() for tag in task.tags]
    return jsonify(tags), 200

@task_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['POST'])
def add_tag_to_task(task_id, tag_id):
    """Add a tag to a task"""
    task = models.storage.get(Task, task_id)
    tag = models.storage.get(Tag, tag_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    if tag not in task.tags:
        task.tags.append(tag)
        task.save()
        return jsonify({"message": "Tag added to task successfully"}), 200

    return jsonify({"error": "Tag already associated with task"}), 400

@task_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['DELETE'])
def remove_tag_from_task(task_id, tag_id):
    """Remove a tag from a task"""
    task = models.storage.get(Task, task_id)
    tag = models.storage.get(Tag, tag_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    if tag in task.tags:
        task.tags.remove(tag)
        task.save()
        return jsonify({"message": "Tag removed from task successfully"}), 200

    return jsonify({"error": "Tag not associated with task"}), 400

