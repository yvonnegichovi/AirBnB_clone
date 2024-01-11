#!/usr/bin/python3
""" Module designed for reviewing within the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class for storing review information. """
    place_id = ""
    user_id = ""
    text = ""
