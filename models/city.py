#!/usr/bin/python3
""" Module pertaining to the state in the HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The class for cities includes the state ID and name """
    state_id = ""
    name = ""
