#!/usr/bin/python3
"""
Unittest defintion for Place class
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skip("Not applicable")
    def test_city_id(self):
        """ Test id type """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skip("Not applicable")
    def test_user_id(self):
        """ Test id type """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skip("Not applicable")
    def test_name(self):
        """ Test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skip("Not applicable")
    def test_description(self):
        """ Test description type """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skip("Not applicable")
    def test_number_rooms(self):
        """ test number_rooms type """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skip("Not applicable")
    def test_number_bathrooms(self):
        """ Test number_bathrooms type """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skip("Not applicable")
    def test_max_guest(self):
        """ Test max_guest type """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skip("Not applicable")
    def test_price_by_night(self):
        """ Test price_by_night type """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skip("Not applicable")
    def test_latitude(self):
        """ Test latitude type """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skip("Not applicable")
    def test_longitude(self):
        """ Test longitude type """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skip("Not applicable")
    def test_amenity_ids(self):
        """ Test amenity id type """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
