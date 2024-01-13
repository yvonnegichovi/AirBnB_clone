#!/usr/bin/python3
"""
Module for testing the 'State' class from 'models.state'.
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test class for the 'State' class, inheriting from 'test_basemodel'.
    """

    def setUp(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Tests the 'name' attribute of the State instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
