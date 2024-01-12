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


if __name__ == '__main__':
    unittest.main()
