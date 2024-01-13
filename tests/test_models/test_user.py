#!/usr/bin/python3
"""
Module for testing the 'User' class from 'models.user'.
"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User

class test_User(test_basemodel):
    """
    Test class for the 'User' class, inheriting from 'test_basemodel'.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and keyword arguments.
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
