#!/usr/bin/python3
"""
Module for testing the 'Review' class from 'models.review'.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test class for the 'Review' class, inheriting from 'test_basemodel'.
    """

    def setUp(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and
        keyword arguments.
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
