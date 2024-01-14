#!/usr/bin/python3
"""
Module for testing the 'User' class from 'models.user'.
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test class for the 'User' class, inheriting from 'test_basemodel'.
    """

    def setUp(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and
        keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Tests the 'first_name' attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Tests the 'last_name' attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Tests the 'email' attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Tests the 'password' attribute of the User instance.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
