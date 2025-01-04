#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.state = State()
        self.state.name = "California"
        self.storage._FileStorage__objects = {
            "BaseModel.1234": self.base_model,
            "State.5678": self.state,
        }

    def test_all_no_cls(self):
        """Test `all` method with no class filter."""
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)

    def test_all_with_cls(self):
        """Test `all` method with a class filter."""
        filtered_objects = self.storage.all(State)
        self.assertEqual(len(filtered_objects), 1)
        self.assertIn("State.5678", filtered_objects)
        self.assertNotIn("BaseModel.1234", filtered_objects)

    def test_all_with_nonexistent_cls(self):
        """Test `all` method with a class that doesn't exist in storage."""
        class FakeClass:
            pass

        filtered_objects = self.storage.all(FakeClass)
        self.assertEqual(len(filtered_objects), 0)

    def test_delete_existing_object(self):
        """Test `delete` method with an existing object."""
        self.storage.delete(self.base_model)
        all_objects = self.storage.all()
        self.assertNotIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)

    def test_delete_nonexistent_object(self):
        """Test `delete` method with an object not in storage."""
        class FakeObject:
            pass

        fake_obj = FakeObject()
        self.storage.delete(fake_obj)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)

    def test_delete_with_none(self):
        """Test `delete` method with None."""
        self.storage.delete(None)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)


if __name__ == "__main__":
    unittest.main()
