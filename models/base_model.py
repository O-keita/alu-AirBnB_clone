#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the base model, a foundation model
    for all our models and instances we will be using in this
    project
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            prints the
            - class name,
            - id
            - dictionary form of the object
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            stores the updated time of
            the instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        dic_obj = self.__dict__.copy()

        dic_obj['__class__'] = self.__class__.__name__
        dic_obj['created_at'] = self.created_at.isoformat()
        dic_obj['updated_at'] = self.update_at.isoformat()
        return dic_obj
