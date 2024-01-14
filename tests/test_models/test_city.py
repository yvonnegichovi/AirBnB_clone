#!/usr/bin/python3
"""
Module for testing the 'City' class from 'models.city'.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test class for the 'City' class, inheriting from 'test_basemodel'.
    """

    def setUp(self, *args, **kwargs):
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
