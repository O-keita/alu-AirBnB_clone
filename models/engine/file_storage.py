#!/usr/bin/python3
import json
import models


class FileStorage:

    __file_path = 'file.json'
    __object = {}

    def all(self):
        return self.__object

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, self.id)
        self.__object[key] = obj

    def save(self):
        serialize_obj = {}

        for key, obj in self.__object.items():
            serialize_obj[key] = obj.to_dict()

            with open(self.__file_path, 'w') as file:

                json.dump(serialize_obj, file)

    def reload(self):

        try:
            with open(self.__file_path, 'r', encoding="UFT8") as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name = value.get('__class__')
                    if class_name:
                        cls = globals().get(class_name)
                    if cls:
                        obj = cls(**value)
                        self.__object[key] = obj

                    else:
                        print(f"{class_name} not found")

        except FileNotFoundError:
            pass
