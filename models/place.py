#!/usr/bin/python3
<<<<<<< HEAD

''' A Place class that inherits from BaseModel '''
=======
"""
Defines the Place class
"""

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    '''
    Public class attribute

    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list:
    '''
=======
    """Represent a Place
       Attributes:
            city_id (str): City id
            user_id (str): User id
            name (str): name of the place.
            description (str): description of the place
            number_rooms (int): number of rooms of the place
            number_bathrooms (int): number of bathrooms of the place
            max_guest (int): maximum number of guests of the place
            price_by_night (int): price by night of the place
            latitude (float): latitude of the place
            longitude (float): longitude of the place
            amenity_ids (list): list of Amenity ids
    """

>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
    city_id = ""
    user_id = ""
    name = ""
    description = ""
<<<<<<< HEAD
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
=======
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
