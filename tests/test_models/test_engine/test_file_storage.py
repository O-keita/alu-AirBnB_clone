import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path_exists(self):
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))

    def test_objects_attribute_exists(self):
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all_method(self):
        # Check if the all() method returns an empty dictionary initially
        self.assertEqual(self.storage.all(), {})

        # Create a new BaseModel instance and add it to the storage
        model = BaseModel()
        self.storage.new(model)
        
        # Check if the all() method returns a dictionary containing the added BaseModel instance
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("BaseModel.{}".format(model.id), self.storage.all())

    def test_new_method(self):
        model = BaseModel()
        self.storage.new(model)
        self.assertIn("BaseModel.{}".format(model.id), self.storage.all())

    def test_save_method(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)
if __name__ == "__main__":
    unittest.main()
