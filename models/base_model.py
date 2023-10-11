#!/usr/bin/python3

"""
Defines a base class model
"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initialize the data."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the object"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""

        d = self.__dict__.copy()
        d["created_at"] = d["created_at"].isoformat()
        d["updated_at"] = d["updated_at"].isoformat()
        d["__class__"] = type(self).__name__
        return d