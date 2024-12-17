#!/usr/bin/python3
"""Task model for task tracker"""

from models.base_model import BaseModel
from datetime import datetime

class Task(BaseModel):
    """Representation of a Task"""

    def __init__(self, *args, **kwargs):
        """Initializes a Task instance"""
        super().__init__(*args, **kwargs)
        self.title = kwargs.get("title", "")
        self.description = kwargs.get("description", "")
        self.status = kwargs.get("status", "pending")
        self.due_date = kwargs.get("due_date", None)
        self.tags = kwargs.get("tags", [])
        
        # Convert due_date string to datetime if provided
        if self.due_date and isinstance(self.due_date, str):
            try:
                self.due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
            except ValueError:
                self.due_date = None  # Reset if format is incorrect

    def __str__(self):
        """String representation of the Task class"""
        return "[Task] ({}) {}".format(self.id, self.to_dict())

    def to_dict(self):
        """Returns a dictionary representation of the Task"""
        task_dict = super().to_dict()
        return {
            "id": task_dict.get("id"),
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "due_date": self.due_date.strftime("%Y-%m-%d") if self.due_date else None,
            "tags": self.tags,
            "created_at": task_dict.get("created_at"),
            "updated_at": task_dict.get("updated_at"),
        }
