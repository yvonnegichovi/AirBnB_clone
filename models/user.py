#!/usr/bin/python3
"""This module establishes a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class describes a user based on different attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
