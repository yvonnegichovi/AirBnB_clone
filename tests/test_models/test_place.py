#!/usr/bin/python3
"""
Module for testing the 'Place' class from 'models.place'.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test class for the 'Place' class, inheriting from 'test_basemodel'.
    """

    def setUp(self, *args, **kwargs):
        """
        Initializes the test instance with optional arguments and
        keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Tests the 'city_id' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Tests the 'user_id' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Tests the 'name' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Tests the 'description' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Tests the 'number_rooms' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Tests the 'number_bathrooms' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Tests the 'max_guest' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Tests the 'price_by_night' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Tests the 'latitude' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Tests the 'longitude' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Tests the 'amenity_ids' attribute of the Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
