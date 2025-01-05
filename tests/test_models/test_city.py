#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(unittest.TestCase):
    """ City test class definition """

    # @unittest.skip("Not applicable")
    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skip("Not applicable")
    def test_state_id(self):
        """ Test state id of city """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skip("Not applicable")
    def test_name(self):
        """ Test city name """
        new = self.value()
        self.assertEqual(type(new.name), str)
