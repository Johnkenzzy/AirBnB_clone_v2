#!/usr/bin/python3
"""
Unittest module for User class
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test class definition """

    def __init__(self, *args, **kwargs):
        """ Initializatiion """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test for first_name type """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test for last_name type """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test for email type """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test for password type """
        new = self.value()
        self.assertEqual(type(new.password), str)
