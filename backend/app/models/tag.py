#!/usr/bin/python3
"""Tag model for task tracker"""

from models.base_model import BaseModel

class Tag(BaseModel):
    """Representation of a Tag"""

    def __init__(self, *args, **kwargs):
        """Initializes a Tag instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")  # Name of the tag (e.g., "Urgent")

    def __str__(self):
        """String representation of the Tag class"""
        return "[Tag] ({}) {}".format(self.id, self.to_dict())

    def to_dict(self):
        """Returns a dictionary representation of the Tag"""
        tag_dict = super().to_dict()
        return {
            "id": tag_dict.get("id"),
            "name": self.name,
            "created_at": tag_dict.get("created_at"),
            "updated_at": tag_dict.get("updated_at"),
        }
