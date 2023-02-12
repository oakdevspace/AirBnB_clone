#!/usr/bin/python3
<<<<<<< HEAD

''' A class user that inherits from BaseModel '''
=======
"""
Defines the User class.
"""
>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    '''
    Public class Atrributes

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    '''
=======
    """Represent a User
    Attributes:
            email (str): user email
            password (str): user password
            first_name (str): first name
            last_name (str): last name
        """
>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
    email = ""
    password = ""
    first_name = ""
    last_name = ""
