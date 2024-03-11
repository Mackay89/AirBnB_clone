#!/usr/bin/python3
"""
This module defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Aclass to represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity istance.

        Args:
            args: Variable lenght argument list.
            **kwargs: Arbitrary keyword arguments
        """

        super().__init__(*args, **kwargs)
        self.name = ""
