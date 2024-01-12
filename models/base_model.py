#!/usr/bin/python3
"""This module has class BaseModel that defines all common attributes/ methods
for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes all instances attributes used"""
        if kwargs:
            """Re-create an instance from dictionary representation"""
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            """create a new instance"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """returns an informal string representation of the instance"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__ of the
        object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
