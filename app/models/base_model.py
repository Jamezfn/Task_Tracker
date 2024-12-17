#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """BaseModel for task tracker app"""
    
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at") and isinstance(kwargs["created_at"], str):
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at") and isinstance(kwargs["updated_at"], str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute and simulates saving to storage"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__

        # Format created_at and updated_at as strings for easy use in JSON
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)

        return new_dict

    def delete(self):
        """Simulates deleting the instance from storage"""
        pass

