#!/usr/bin/python3
"""
Module for testing the 'State' class from 'models.state'.
"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_state(test_basemodel):
    """
    Test class for the 'State' class, inheriting from 'test_basemodel'.
    """

    def __init__(self, *args, **kwargs):
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
