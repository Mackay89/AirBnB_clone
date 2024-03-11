#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Represent the base model of the HBnB project.

    Attributes:
        id (str): The unique identifier of the BaseModel instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """


    def __init__(self, *args, **kwargs):
        """
        Initializes anew BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, t_format))
                else:
                    setattr(self, key, value)


    def save(self):
        """
        Update the update_at attribute with the currennt datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()


    def to_dict(self):
        """
        Return the dictionary representation of the BaseModel instance.

        Return:
            dict: Dictionary representation of the BaseMOdel instance.
        """
        return {
            **self.__dict__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }


    def __str__(self):
        """
        Return the string representation of the BaseModel instance.

        Return:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

