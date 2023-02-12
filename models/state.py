#!/usr/bin/python3
<<<<<<< HEAD

''' A State class that inherits from BaseModel '''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    Public class attribute

    name: string - empty string
    '''
=======
"""
Defines the State class
"""

from models.base_model import BaseModel

class State(BaseModel):
    """Represent a state
       Attributes:
           name (str): The name of the state
    """

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
    name = ""
