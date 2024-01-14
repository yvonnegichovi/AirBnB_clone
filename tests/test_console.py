#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleHelp(unittest.TestCase):
    def setUp(self):
        """sets up the console class before every test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """passes"""
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit_command(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            expected_output = "" 
            output = mock_stdout.getvalue().strip()
            self.assertEqual(expected_output, output)


if __name__ == "__main__":
    unittest.main()
