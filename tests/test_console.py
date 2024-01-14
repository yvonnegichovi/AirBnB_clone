#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsoleHelp(unittest.TestCase):
    """
    Test class for console
    """

    def setUp(self):
        """sets up the console class before every test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """passes"""
        pass

    def test_help_quit_command(self):
        """tests help quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_help_EOF_command(self):
        """tests help EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_help_emptyline_command(self):
        """Tests emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_help_command_type(self):
        """tests the type of instance help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

    def test_help_create_command(self):
        """Tests the help create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Create a new instance of BaseModel.")

    def test_create_command(self):
        """tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Create a new instance of BaseModel.")

    def test_help_show_command(self):
        """tests the help shhow command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Show the string representation of an instance.")

    def test_help_destroy_command(self):
        """tests the help destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Delete an instance based on the class name and id.")

    def test_help_all_command(self):
        """tests the help all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Print the string representation.")

    def test_help_update_command(self):
        """tests the help upfate command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Update an instance by adding or updating an attribute.")

    def test_help_count_command(self):
        """tests the help count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue().strip(),
                    "Counts and retrieves the number of instances of a class")

    def test_create_valid_instance(self):
        """tests the create valid instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip())

    def test_create_invalid_instance(self):
        """tests when you create an invalid instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            expected_output = "** class doesn't exist **"
            self.assertIn(expected_output, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
