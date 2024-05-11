
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