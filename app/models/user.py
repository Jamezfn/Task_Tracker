#!/usr/bin/python3
"""User model for task tracker"""

from models.base_model import BaseModel

class User(BaseModel):
    """Representation of a User"""

    def __init__(self, *args, **kwargs):
        """Initializes the User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")

    def __str__(self):
        """String representation of the User class"""
        return "[User] ({}) {}".format(self.id, self.to_dict())

    def to_dict(self):
        """Returns a dictionary representation of the User"""
        user_dict = super().to_dict()
        return {
            "id": user_dict.get("id"),
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": user_dict.get("created_at"),
            "updated_at": user_dict.get("updated_at"),
        }
