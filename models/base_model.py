#!/usr/bin/python3
"""BaseModel Class"""
import models
from datetime import datetime
import uuid


class BaseModel():
    """Base Model class parent for all classes"""

    def __init__(self, *args, **kwargs):
        """Intialization of BaseModel object"""

        if len(kwargs) != 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """The custom representation for printing BaseModel object"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """to update time after each new save of an object"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance with class name as a value and key __class__"""

        my_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                my_dict[key] = datetime.isoformat(value)
            else:
                my_dict[key] = value
        return my_dict
