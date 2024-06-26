#!/usr/bin/python3
""" Unit test City """

import unittest
import models
import os
from models.city import City


class TestCity(unittest.TestCase):
    """ Test for class city"""

    def test_docstring(self):
        '''test if funcions, methods, classes
        and modules have docstring'''
        # msj = "Módulo does not has docstring"
        # self.assertIsNotNone(models.city.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(City.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/city.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/city.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/city.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_city(self):
        """test if an object is an type city"""
        my_object = City()
        self.assertIsInstance(my_object, City)

    def test_id(self):
        """ test that id is unique """
        my_objectId = City()
        my_objectId1 = City()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_strobject = City()
        _dict = my_strobject.__dict__
        string1 = "[City] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = City()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = City()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'City':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()