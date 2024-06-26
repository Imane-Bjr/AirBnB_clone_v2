#!/usr/bin/python3
""" document document """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ document document """

    def __init__(self, *args, **kwargs):
        """ document document """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ document document """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
