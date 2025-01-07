#!/usr/bin/python3
"""
Unittest class for Amenity class
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skip("Not applicable")
    def test_name2(self):
        """ Test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)
