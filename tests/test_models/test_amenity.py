#!/usr/bin/python3
""" document document """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ document document """

    def __init__(self, *args, **kwargs):
        """ document document """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.name), str)
