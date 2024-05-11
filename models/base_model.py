#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the base model, a foundation model
    for all our models and instances we will be using in this
    project
    """

    def __init__(self, *args, **kwargs):
        """
            The args and the keyword args will also be
            considered when making a model.
            if there is kwargs, we will use those
            for our objects, else we use the other ways
            round
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f'
                        )

                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

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
        dic_obj['updated_at'] = self.updated_at.isoformat()
        return dic_obj
