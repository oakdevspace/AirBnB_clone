#!/usr/bin/python3
<<<<<<< HEAD

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
=======
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
from models.amenity import Amenity
from models.review import Review


class FileStorage:
<<<<<<< HEAD
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
=======
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
>>>>>>> 89e061e798383b89c94363797173e1990e89f63c
