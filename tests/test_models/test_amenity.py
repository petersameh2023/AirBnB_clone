#!/usr/bin/python3
"""Unittests for Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_amenity_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test if Amenity has the correct attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertIsInstance(amenity.id, str)
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

    def test_amenity_creation(self):
        """Test Amenity object creation."""
        amenity = Amenity()
        self.assertIsNotNone(amenity)

    def test_amenity_name_setter(self):
        """Test setting the name attribute."""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_amenity_to_dict(self):
        """Test to_dict method."""
        amenity = Amenity()
        amenity.name = "Maher"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Maher")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_amenity_str_representation(self):
        """Test __str__ method."""
        amenity = Amenity()
        amenity.name = "Mohamed"
        amenity_str = str(amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(amenity.id, amenity_str)
        self.assertIn("'name': 'Mohamed'", amenity_str)

    def test_amenity_save_method(self):
        """Test save method."""
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, initial_updated_at)

    def test_amenity_create_from_dict(self):
        """Test creating Amenity from dictionary."""
        amenity_dict = {
            '__class__': 'Amenity',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'name': 'Peter'
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(amenity.name, 'Peter')
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
