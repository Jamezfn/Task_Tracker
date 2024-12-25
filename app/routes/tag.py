#!/usr/bin/python3
"""Tag routes for the task tracker"""

from flask import Blueprint, jsonify, request
from models.tag import Tag
from models.task import Task
import models

# Create a blueprint for tag routes
tag_routes = Blueprint('tag_routes', __name__)

@tag_routes.route('/tags', methods=['GET'])
def get_tags():
    """Retrieve all tags"""
    tags = models.storage.all(Tag).values()
    tag_list = [tag.to_dict() for tag in tags]
    return jsonify(tag_list), 200

@tag_routes.route('/tags/<tag_id>', methods=['GET'])
def get_tag(tag_id):
    """Retrieve a specific tag by ID"""
    tag = models.storage.get(Tag, tag_id)
    if tag:
        return jsonify(tag.to_dict()), 200
    return jsonify({"error": "Tag not found"}), 404

@tag_routes.route('/tags', methods=['POST'])
def create_tag():
    """Create a new tag"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    if not name:
        return jsonify({"error": "Tag name is required"}), 400

    tag = Tag(name=name)
    models.storage.new(tag)
    models.storage.save()
    return jsonify(tag.to_dict()), 201

@tag_routes.route('/tags/<tag_id>', methods=['PUT'])
def update_tag(tag_id):
    """Update a tag"""
    tag = models.storage.get(Tag, tag_id)
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    if name:
        tag.name = name

    tag.save()
    return jsonify(tag.to_dict()), 200

@tag_routes.route('/tags/<tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    """Delete a tag"""
    tag = models.storage.get(Tag, tag_id)
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    models.storage.delete(tag)
    models.storage.save()
    return jsonify({"message": "Tag deleted successfully"}), 200

@tag_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['POST'])
def assign_tag_to_task(task_id, tag_id):
    """Assign a tag to a task"""
    task = models.storage.get(Task, task_id)
    tag = models.storage.get(Tag, tag_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    task.tags.append(tag)
    task.save()
    return jsonify({"message": "Tag assigned to task successfully"}), 200

@tag_routes.route('/tasks/<task_id>/tags/<tag_id>', methods=['DELETE'])
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

