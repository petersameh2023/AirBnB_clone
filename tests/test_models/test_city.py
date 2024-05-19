#!/usr/bin/python3
"""Unittests for City class."""

import unittest
from models.city import City
from models.base_model import BaseModel
import datetime


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_city_inheritance(self):
        """Test if City inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test if City has the correct attributes."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertIsInstance(city.id, str)
        self.assertTrue(hasattr(city, "created_at"))
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertIsInstance(city.updated_at, datetime.datetime)

    def test_city_creation(self):
        """Test City object creation."""
        city = City()
        self.assertIsNotNone(city)

    def test_city_state_id_setter(self):
        """Test setting the state_id attribute."""
        city = City()
        city.state_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        self.assertEqual(city.state_id, "12345678-90ab-cdef-ghij-klmnopqrst")

    def test_city_name_setter(self):
        """Test setting the name attribute."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict(self):
        """Test to_dict method."""
        city = City()
        city.state_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        city.name = "New York City"
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(
                city_dict["state_id"],
                "12345678-90ab-cdef-ghij-klmnopqrst")
        self.assertEqual(city_dict["name"], "New York City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_city_str_representation(self):
        """Test __str__ method."""
        city = City()
        city.state_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        city.name = "Cairo"
        city_str = str(city)
        self.assertIn("[City]", city_str)
        self.assertIn(city.id, city_str)
        self.assertIn(
                "'state_id': '12345678-90ab-cdef-ghij-klmnopqrst'",
                city_str)
        self.assertIn("'name': 'Cairo'", city_str)

    def test_city_save_method(self):
        """Test save method."""
        city = City()
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, initial_updated_at)

    def test_city_create_from_dict(self):
        """Test creating City from dictionary."""
        city_dict = {
            '__class__': 'City',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'state_id': '98765432-10fe-dcba-9876-543210fedcba',
            'name': 'London'
        }
        city = City(**city_dict)
        self.assertEqual(city.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(city.state_id, '98765432-10fe-dcba-9876-543210fedcba')
        self.assertEqual(city.name, 'London')
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)
