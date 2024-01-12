#!/usr/bin/python3
"""This module contains a test for class BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        del self.my_model

    def test_attributes(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertTrue(hasattr(self.my_model, '__str__'))
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertTrue(hasattr(self.my_model, 'to_dict'))

    def test_id_type(self):
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(
                self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(original_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
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
        obj_dict = self.my_model.to_dict()
        created_at_str = obj_dict['created_at']
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(created_at_str, expected_format)
        except ValueError:
            self.fail("Incorrect format for created_at in to_dict")

    def test_to_dict_updated_at_format(self):
        obj_dict = self.my_model.to_dict()
        updated_at_str = obj_dict['updated_at']
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(updated_at_str, expected_format)
        except ValueError:
            self.fail("Incorrect format for updated_at in to_dict")


if __name__ == '__main__':
    unittest.main()
