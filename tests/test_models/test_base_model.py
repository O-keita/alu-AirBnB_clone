from models.base_model import BaseModel
import unittest


class TestBase(unittest.TestCase):
    """
    """

    def test_init(self):
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = BaseModel()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_str(self):
        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        #   self.assertEqual(model_dict['created_at'], model.created_at)
        #   self.assertEqual(model_dict['updated_at'], model.updated_at)
        self.assertEqual(model_dict['id'], model.id)

    def test_updated(self):
        model = BaseModel()

        initial = model.updated_at

        model.save()

        updated = model.updated_at

        self.assertNotEqual(initial, updated)


if __name__ == '__main__':
    unittest.main()
