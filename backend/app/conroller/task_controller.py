from app.db import db
from app.models.task import Task
from flask import jsonify
from app.conroller.user_conroller import user_controller
from datetime import date
from app.custom_exceptions import CustomJwtException

class TaskController:
    """Contains task methods"""
    def createTask(self, token, title, description, status, start_date, due_date):
        """creates new tasks"""
        try:
            user_id = user_controller.authorise_user(token)
        except CustomJwtException as e:
            return jsonify({"error": str(e)})
        start = start_date.split("-")
        due = due_date.split("-")
        db.session.add(Task(title=title, description=description, status=status,  user_id=user_id, start_date=date(int(start[0]), int(start[1]), int(start[2])), due_date=date(int(due[0]), int(due[1]), int(due[2]))))
        db.session.commit()
        return jsonify({"message": "task created succesfully"}), 201
                

    def getTasks(self, token):
        """Retrieve all tasks"""
        try:
            user_id = user_controller.authorise_user(token)
        except CustomJwtException as e:
            return jsonify({"error": str(e)}), 400
        tasks = db.session.query(Task).filter_by(user_id=user_id).all()
        if not tasks:
            return jsonify({"error": "User has no tasks"}), 400
        
        task_list = []
        for task in tasks:
            temp = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "start_date": task.start_date,
                "due_date": task.due_date
                }
            task_list.append(temp)
        return jsonify({"tasks": task_list}), 200

    def getTask(self, token, task_id):
        """Get specific task"""
        try:
            user_id = user_controller.authorise_user(token)
        except CustomJwtException as e:
            return jsonify({"error": str(e)}), 400
        task = db.session.query(Task).filter_by(id=task_id, user_id=user_id).first()
        if not task:
            return jsonify({"error": "Task not found"}), 400
        tasks_1 = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "start_date": task.start_date,
            "due_date": task.due_date
        }
        return jsonify({"task": tasks_1})

    def updateTask(self, token, task_id, title=None, description=None, status=None, start_date=None, due_date=None):
        """update task"""
        try:
            user_id = user_controller.authorise_user(token)
        except CustomJwtException as e:
            return jsonify({"error": str(e)}), 400
        task = db.session.query(Task).filter_by(id=task_id, user_id=user_id).first()
        if not task: return jsonify({"error": "Task not found"}), 400
        
        # updating task
        if title: task.title = title
        if description: task.description = description
        if status: task.status = status
        if start_date: task.start_date = start_date
        if due_date: task.due_date = due_date

        db.session.commit()

        return jsonify({"message": f"{task.title} updated succefully"})

    def deleteTask(self, token, task_id):
        """Delete task"""
        try:
            user_id = user_controller.authorise_user(token)
        except CustomJwtException as e:
            return jsonify({"error": str(e)}), 400
        task = db.session.query(Task).filter_by(id=task_id, user_id=user_id).first()
        if not task: return jsonify({"error": "Task not found"}), 400
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"}), 200
    

task_controller = TaskController()