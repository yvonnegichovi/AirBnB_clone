#!/usr/bin/python3
"""
Module for testing the 'Review' class from 'models.review'.
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class test_review(test_basemodel):
    """
    Test class for the 'Review' class, inheriting from 'test_basemodel'.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Tests the 'place_id' attribute of the Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Tests the 'user_id' attribute of the Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Tests the 'text' attribute of the Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
