#!/usr/bin/python3

''' A FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances
'''
import json
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' FileStorage class '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Return:
        Dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects obj, with key classname.id

        Args:
        object
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' serializes __objects to JSON file '''
        newdict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for i, j in self.__objects.items():
                newdict[i] = j.to_dict()
            json.dump(newdict, f)

    def reload(self):
        ''' Deseriallizes the JSON file '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newobjects = json.load(f)
                for i, j in newobjects.items:
                    reloadedobj = eval('{}(**j)'.format(j['__class__']))
                    self.__objects[i] reloadedobj

        except IOError:
            pass
