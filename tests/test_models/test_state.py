#!/usr/bin/python3
"""
Unittest module for State class
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ State test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skip("Not applicable")
    def test_name3(self):
        """ Test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)
