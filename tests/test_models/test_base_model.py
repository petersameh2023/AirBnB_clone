import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        # Test initialization with kwargs
        iso_date = "2023-10-27T12:00:00"
        kwargs = {"id": "123", "created_at": iso_date, "updated_at": iso_date}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, datetime.fromisoformat(iso_date))
        self.assertEqual(model.updated_at, datetime.fromisoformat(iso_date))

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model.name = "Test Model"
        model.number = 123

        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertEqual(model_dict['number'], 123)

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_includes_class_name(self):
        """Test that to_dict includes the class name."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        class_name = model.__class__.__name__
        obj_dict = model.__dict__
        expected_string = "[{}] ({}) {}".format(class_name, model.id, obj_dict)
        self.assertEqual(str(model), expected_string)

    def test_to_dict_includes_all_attributes(self):
        """Test that to_dict includes all attributes."""
        model = BaseModel()
        model.name = "Model"
        model.number = 234
        model_dict = model.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)

    def test_to_dict_converts_datetime_to_isoformat(self):
        """Test that to_dict converts datetime to isoformat."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['__class__'], str)

    def test_unique_id(self):
        """Test that each instance has a unique ID."""
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = model1
        self.assertNotEqual(model1.id, model2.id)
        self.assertEqual(model1.id, model3.id)

    def test_not_equality_of_created_at_and_updated_at(self):
        """Test that created_at and updated_at are different."""
        model = BaseModel()
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_to_dict_is_not__dict__(self):
        """Test that to_dict does not modify the original object."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertNotEqual(model.__dict__, model_dict)

    def test_to_dict_alwayes_returns_new_dict(self):
        """Test that to_dict returns a new dictionary."""
        model = BaseModel()
        model_dict1 = model.to_dict()
        model_dict2 = model.to_dict()
        self.assertNotEqual(id(model_dict1), id(model_dict2))

    def test_save_does_not_modify_created_at(self):
        """Test that save does not modify the created_at attribute."""
        model = BaseModel()
        initial_created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, initial_created_at)

    def test_two_saves(self):
        """Test that save updates the updated_at attribute twice."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        first_save_updated_at = model.updated_at
        self.assertNotEqual(first_save_updated_at, initial_updated_at)
        model.save()
        second_save_updated_at = model.updated_at
        self.assertNotEqual(second_save_updated_at, first_save_updated_at)


class TestBaseModel_instantiation(unittest.TestCase):
    """Test instantiation of BaseModel"""

    def test_no_args(self):
        """Test instantiation with no arguments."""
        model = BaseModel(None)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_with_kwargs(self):
        """Test instantiation with keyword arguments."""
        kwargs = {"id": "123", "name": "test_model", "my_number": 123}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.name, "test_model")
        self.assertEqual(model.my_number, 123)

    def test_kwargs_overrides_default(self):
        """Test that keyword arguments override default values."""
        kwargs = {"id": "abc", "created_at": "2023-10-27T12:00:00"}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "abc")
        created = "2023-10-27T12:00:00"
        self.assertEqual(model.created_at, datetime.fromisoformat(created))


if __name__ == '__main__':
    unittest.main()
