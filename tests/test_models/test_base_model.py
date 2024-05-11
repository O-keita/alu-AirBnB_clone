from models.base_model import BaseModel
import unittest


class TestBase(unittest.TestCase):
    """
    """

    def test_init(self):
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.update_at)


if __name__ == '__main__':
    unittest.main()
