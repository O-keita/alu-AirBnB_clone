#!/usr/bin/python3
import json
import models


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, self.id)
        self.__objects[key] = obj

    def save(self):
        serialize_obj = {}

        for key, obj in self.__objects.items():
            serialize_obj[key] = obj.to_dict()

            with open(self.__file_path, 'w') as file:

                json.dump(serialize_obj, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass