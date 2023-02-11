#!/usr/bin/python3

''' A City class that inherits from BaseModel '''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Public class attribute

    state_id: string - empty string: it will be the State.id
    name: string - empty string
    '''
    state_id = ""
    name = ""
