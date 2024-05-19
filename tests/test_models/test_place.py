#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.place import Place
from models.base_model import BaseModel
import datetime


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_place_inheritance(self):
        """Test if Place inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        """Test if Place has the correct attributes."""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(hasattr(place, "id"))
        self.assertIsInstance(place.id, str)
        self.assertTrue(hasattr(place, "created_at"))
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertIsInstance(place.updated_at, datetime.datetime)

    def test_place_creation(self):
        """Test Place object creation."""
        place = Place()
        self.assertIsNotNone(place)

    def test_place_city_id_setter(self):
        """Test setting the city_id attribute."""
        place = Place()
        place.city_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        self.assertEqual(place.city_id, "12345678-90ab-cdef-ghij-klmnopqrst")

    def test_place_user_id_setter(self):
        """Test setting the user_id attribute."""
        place = Place()
        place.user_id = "98765432-10fe-dcba-9876-543210fedcba"
        self.assertEqual(place.user_id, "98765432-10fe-dcba-9876-543210fedcba")

    def test_place_name_setter(self):
        """Test setting the name attribute."""
        place = Place()
        place.name = "Cozy Apartment"
        self.assertEqual(place.name, "Cozy Apartment")

    def test_place_number_rooms_setter(self):
        place = Place()
        place.number_rooms = 2
        self.assertEqual(place.number_rooms, 2)

    def test_place_number_bathrooms_setter(self):
        place = Place()
        place.number_bathrooms = 1
        self.assertEqual(place.number_bathrooms, 1)

    def test_place_max_guest_setter(self):
        """Test setting the max_guest attribute."""
        place = Place()
        place.max_guest = 4
        self.assertEqual(place.max_guest, 4)

    def test_place_price_by_night_setter(self):
        """Test setting the price_by_night attribute."""
        place = Place()
        place.price_by_night = 100
        self.assertEqual(place.price_by_night, 100)

    def test_place_latitude_setter(self):
        """Test setting the latitude attribute."""
        place = Place()
        place.latitude = 37.7749
        self.assertEqual(place.latitude, 37.7749)

    def test_place_longitude_setter(self):
        """Test setting the longitude attribute."""
        place = Place()
        place.longitude = -122.4194
        self.assertEqual(place.longitude, -122.4194)

    def test_place_amenity_ids_setter(self):
        """Test setting the amenity_ids attribute."""
        place = Place()
        place.amenity_ids = ["12345", "98765"]
        self.assertEqual(place.amenity_ids, ["12345", "98765"])

    def test_place_str_representation(self):
        """Test __str__ method."""
        place = Place()
        place.city_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        place.user_id = "98765432-10fe-dcba-9876-543210fedcba"
        place.name = "Mohamed Maher"
        place_str = str(place)
        self.assertIn("[Place]", place_str)
        self.assertIn(place.id, place_str)
        self.assertIn(
                "'city_id': '12345678-90ab-cdef-ghij-klmnopqrst'", place_str)
        self.assertIn(
                "'user_id': '98765432-10fe-dcba-9876-543210fedcba'", place_str)
        self.assertIn("'name': 'Mohamed Maher'", place_str)

    def test_place_save_method(self):
        """Test save method."""
        place = Place()
        initial_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, initial_updated_at)

    def test_place_create_from_dict(self):
        """Test creating Place from dictionary."""
        place_dict = {
            '__class__': 'Place',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'city_id': '98765432-10fe-dcba-9876-543210fedcba',
            'user_id': 'abcdef12-3456-7890-1234-567890abcdef',
            'name': 'Luxury Villa',
            'description': 'villa with a private pool.',
            'number_rooms': 4,
            'number_bathrooms': 3,
            'max_guest': 8,
            'price_by_night': 500,
            'latitude': 40.7128,
            'longitude': -74.0060
        }
        place = Place(**place_dict)
        self.assertEqual(place.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(place.city_id, '98765432-10fe-dcba-9876-543210fedcba')
        self.assertEqual(place.user_id, 'abcdef12-3456-7890-1234-567890abcdef')
        self.assertEqual(place.name, 'Luxury Villa')
        self.assertEqual(place.description, 'villa with a private pool.')
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 500)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertIsInstance(place.updated_at, datetime.datetime)
