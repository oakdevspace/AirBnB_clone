#!/usr/bin/python3
"""
Defines the Amenit class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity
       Attributes:
           name (str): The name of the amenity
    """

    name = ""
