#!/usr/bin/python3
"""This module contains a test for class BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """This class tests all instances and methods of class BaseModel"""

    def setUp(self):
        """Creates a dict every time a test is created"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        """Deletes a dict every time the test comes to an end"""
        del self.my_model

    def test_attributes(self):
        """Checks if the class has the following attributes"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertTrue(hasattr(self.my_model, '__str__'))
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertTrue(hasattr(self.my_model, 'to_dict'))

    def test_uuid(self):
        """Tests if id is a valid uuid"""
        with self.subTest(msg="Check UUID format for new instance"):
            uuid_obj = uuid.UUID(self.my_model.id, version=4)
            self.assertEqual(str(uuid_obj), self.my_model.id)

    def test_id_type(self):
        """Identifies the type of instance id is"""
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_type(self):
        """identifies the type of instance created_at is"""
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_updated_at_type(self):
        """Identifies the type of instance updated_at is"""
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str_method(self):
        """Checks if the str method works"""
        expected_str = "[BaseModel] ({}) {}".format(
                self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        """Checks if the save method works"""
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(original_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """Checks if the to_dict method works"""
        obj_dict = self.my_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('my_number', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)

    def test_to_dict_created_at_format(self):
        """Checks the format of to_dict.created_at"""
        obj_dict = self.my_model.to_dict()
        created_at_str = obj_dict['created_at']
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(created_at_str, expected_format)
        except ValueError:
            self.fail("Incorrect format for created_at in to_dict")

    def test_to_dict_updated_at_format(self):
        """Checks the format of to_dict.created_at"""
        obj_dict = self.my_model.to_dict()
        updated_at_str = obj_dict['updated_at']
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(updated_at_str, expected_format)
        except ValueError:
            self.fail("Incorrect format for updated_at in to_dict")


if __name__ == '__main__':
    unittest.main()
