#!/usr/bin/python3
"""
Importing the 'test_basemodel' class from the 'tests.test_models.test_base_model' module and the 'Amenity' class
from the 'models.amenity' module for testing purposes.
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):

def __init__(self, *args, **kwargs):
"""Initialize the test instance with optional arguments and keyword arguments."""
super().__init__(*args, **kwargs)
self.name = "Amenity"
self.value = Amenity

def test_name2(self):
"""Test the 'name' attribute of the Amenity instance."""
new = self.value()
self.assertEqual(type(new.name), str)
