#!/usr/bin/python3


'''
A BaseModel class that defines all common
attributes/methods for other classes
'''
import uuid
import models
from datetime import datetime


class BaseModel:
    ''' BaseModel class '''
    def __init__(self, *args, **kwargs):
        '''
        Initialization of the model

        Args:
        *args: arguments passed in
        **kwargs: arguments with key value pairs (dictionary)

        Return:
        None
        '''
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.save()

        def __str__(self):
            '''
            Return:
            Print string representation of object
            '''
            return '[{}] ({}) {}'.format(self.__class__.__name__,
                                         self.id, self.__dict__)

        def save(self):
            ''' Updates the updated_at date attribute '''
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            ''' Returns a dictionary containing all keys/values of __dict__ '''
            mydict = self.__dict__.copy()
            mydict['__class__'] = self.__class__.__name__
            mydict['created_at'] = self.created_at.isoformat()
            mydict['updated_at'] = self.updated_at.isoformat()

            return mydict
