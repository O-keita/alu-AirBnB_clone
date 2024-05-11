import os
import json


class FileStorage:
    """
    """
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.__objects[key] = obj

    def all(self):
        return self.__objects
    
    def save(self):
        """
        """
        all_obj = self.__objects
        obj_dic = {}

        for obj in all_obj.keys():
            obj_dic[obj] = all_obj[obj].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dic, file)


    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:

                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance

                except Exception:
                    pass




