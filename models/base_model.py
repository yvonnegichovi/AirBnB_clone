#!/usr/bin/python3
"""This module has class BaseModel that defines all common attributes/ methods
for other classes"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes all instances attributes used"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns an informal string representation of the instance"""
        print("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__ of the
        object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
