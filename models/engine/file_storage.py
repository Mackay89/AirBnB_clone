#!/usr/bin/python3
"""
This module defines the Filestorage class.
"""

import json 
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represent an abstracted storage engine.
    Attributes:
        file_path (str): The name of the file to save objects to.
        _objects (dict): A dictionary of instantiated objects.
    """
    file_path = "file.json"
    _objects = {}


    def all(self):
        """
        Represent the return dictionary _objcts.
        """
        return self._objects


    def new(self, obj):
        """
        Set in _objects obj with key <obj_class_name>.id
        """

        ocname = obj.__class__.__name__
        self._objects["{}.{}".format(ocname, obj.id)] = obj


    def save(self):
        """
        Serialize _objects to the JSON file file_path.
        """

        objdict = {key: obj.to_dict() for key, obj in self._objects.items()}
        with open(self.file_path, "w") as f:
            json.dump(objdict, f)


    def reload(self):
        """
        Deserialize the JSON file_path to o__objects, if it exists.
        """

        try:
            with open(self.file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
