#!/usr/bin/python3
"""
Module for testing the 'City' class from 'models.city'.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City

class test_City(test_basemodel):
    """
    Test class for the 'City' class, inheriting from 'test_basemodel'.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Tests the 'state_id' attribute of the City instance.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Tests the 'name' attribute of the City instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
