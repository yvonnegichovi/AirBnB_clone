#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """command class that serves as an entry point for the program"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
