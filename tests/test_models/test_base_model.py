#!/usr/bin/python3
"""
Unittest for BaseModel
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Test class """

    def __init__(self, *args, **kwargs):
        """ Attributes intializer """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set up for tests"""
        pass

    def tearDown(self):
        """ Restore state after tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ Test default attributes """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test name value arguments """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skip("Not applicable")
    def test_kwargs_int(self):
        """ Test integer value """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skip("Not applicable")
    def test_save(self):
        """ Testing save  method """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skip("Not applicable")
    def test_str(self):
        """ Test string value """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skip("Not applicable")
    def test_todict(self):
        """ Test todict conversion method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skip("Not applicable")
    def test_kwargs_none(self):
        """ Test name argument with None key and value """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("Not applicable")
    def test_kwargs_one(self):
        """ Test one named agument """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    @unittest.skip("Not applicable")
    def test_id(self):
        """ Test id data type """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skip("Not applicable")
    def test_created_at(self):
        """ Test date and time of object creation """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skip("Not applicable")
    def test_updated_at(self):
        """ Test data and time of object update """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
