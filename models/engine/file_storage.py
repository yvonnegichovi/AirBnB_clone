#!/usr/bin/python3
"""This is a storage module that serializes instances to a JSON file and
deserializes JSON file"""


import json
from os import path


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for obj in data.values():
                    class_name = obj["__class__"]
                    self.new(eval(class_name)(**obj))
        else:
            return
