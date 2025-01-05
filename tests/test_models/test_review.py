#!/usr/bin/python3
"""
Unittest for Review class
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test for place_id type """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test for user_id type """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test for text type """
        new = self.value()
        self.assertEqual(type(new.text), str)
