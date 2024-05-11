#!/usr/bin/python3
import json
from models.base_model import BaseModel 


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialize_obj = {}

        for key, obj in self.__objects.items():
            serialize_obj[key] = obj.to_dict()

            with open(self.__file_path, 'w') as file:

                json.dump(serialize_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name = value.get('__class__')

                    if class_name:
                        cls = globals().get(class_name)
                        if cls:
                            obj = cls(**value)
                            self.__objects[key] = obj
                        else:
                            print(f"Class {class_name} not found")
                    else:
                        print("Class name not found in serialized data")

        except FileNotFoundError:
            print(f"File '{self.__file_path}' not found")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
