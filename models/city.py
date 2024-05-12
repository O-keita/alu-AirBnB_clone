#!/usr/bin/python3
from models.base_model import BaseModel
"""This is a doc string"""


class City(BaseModel):
    """
        City Module
        state_id = string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
