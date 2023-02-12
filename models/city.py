#!/usr/bin/python3
<<<<<<< HEAD

''' A City class that inherits from BaseModel '''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Public class attribute

    state_id: string - empty string: it will be the State.id
    name: string - empty string
    '''
=======
"""
Defines the City class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Represent a City
       Attributes:
           state_id (str): The id of the state
           name (str): The name of the state
    """

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
    state_id = ""
    name = ""
