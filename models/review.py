#!/usr/bin/python3
<<<<<<< HEAD

''' A Review class that inherits from BaseModel '''
=======
"""
Defines the Review class
"""

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    '''
    Public class attribute

    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    '''
=======
    """Represent a Review
       Attributes:
           place_id = empty string
           user_id = empty string
           test = empty string
    """

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
    place_id = ""
    user_id = ""
    text = ""
