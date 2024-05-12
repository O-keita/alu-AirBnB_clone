#!/usr/bin/python3
from models.base_model import BaseModel
"""This is a doc string"""

class User(BaseModel):
    """
        User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""