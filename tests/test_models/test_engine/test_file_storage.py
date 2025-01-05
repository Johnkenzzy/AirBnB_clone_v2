#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
import os

store = os.getenv('HBNB_TYPE_STORAGE', 'default_store')


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        if store == 'db':
            return
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        if store == 'db':
            return
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        if store == 'db':
            return
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        if store == 'db':
            return
        new = BaseModel()
        temp = None
        obj = None
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        if store == 'db':
            return
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        if store == 'db':
            return
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        if store == 'db':
            return
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        if store == 'db':
            return
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skip("Not applicable")
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        if store == 'db':
            return
        new = BaseModel()
        storage.save()
        storage.reload()
        loaded = None
        obj = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        if store == 'db':
            return
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        if store == 'db':
            return
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        if store == 'db':
            return
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        if store == 'db':
            return
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        if store == 'db':
            return
        self.assertEqual(type(storage.all()), dict)

    @unittest.skip("Not applicable")
    def test_key_format(self):
        """ Key is properly formatted """
        if store == 'db':
            return
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        if store == 'db':
            return
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment."""
        if store == 'db':
            return
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
        if store == 'db':
            return
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)

    def test_all_with_cls(self):
        """Test `all` method with a class filter."""
        if store == 'db':
            return
        filtered_objects = self.storage.all(State)
        self.assertEqual(len(filtered_objects), 1)
        self.assertIn("State.5678", filtered_objects)
        self.assertNotIn("BaseModel.1234", filtered_objects)

    def test_all_with_nonexistent_cls(self):
        """Test `all` method with a class that doesn't exist in storage."""
        if store == 'db':
            return

        class FakeClass:
            pass

        filtered_objects = self.storage.all(FakeClass)
        self.assertEqual(len(filtered_objects), 0)

    def test_delete_existing_object(self):
        """Test `delete` method with an existing object."""
        if store == 'db':
            return
        self.storage.delete(self.base_model)
        all_objects = self.storage.all()
        self.assertNotIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)

    def test_delete_nonexistent_object(self):
        """Test `delete` method with an object not in storage."""
        if store == 'db':
            return

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
        if store == 'db':
            return
        self.storage.delete(None)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("BaseModel.1234", all_objects)
        self.assertIn("State.5678", all_objects)


if __name__ == "__main__":
    unittest.main()
