#!/usr/bin/python3
"""Unittests for User class."""

import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_user_inheritance(self):
        """Test if User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """Test if User has the correct attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(hasattr(user, "id"))
        self.assertIsInstance(user.id, str)
        self.assertTrue(hasattr(user, "created_at"))
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertIsInstance(user.updated_at, datetime.datetime)

    def test_user_creation(self):
        """Test User object creation."""
        user = User()
        self.assertIsNotNone(user)

    def test_user_email_setter(self):
        """Test setting the email attribute."""
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_user_password_setter(self):
        """Test setting the password attribute."""
        user = User()
        user.password = "P@$$wOrd"
        self.assertEqual(user.password, "P@$$wOrd")

    def test_user_first_name_setter(self):
        """Test setting the first_name attribute."""
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_user_last_name_setter(self):
        """Test setting the last_name attribute."""
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """Test to_dict method."""
        user = User()
        user.email = "test@example.com"
        user.password = "P@$$wOrd"
        user.first_name = "Jane"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "P@$$wOrd")
        self.assertEqual(user_dict["first_name"], "Jane")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_user_str_representation(self):
        """Test __str__ method."""
        user = User()
        user.email = "test@example.com"
        user.password = "P@$$wOrd"
        user.first_name = "Peter"
        user.last_name = "Pan"
        user_str = str(user)
        self.assertIn("[User]", user_str)
        self.assertIn(user.id, user_str)
        self.assertIn("'email': 'test@example.com'", user_str)
        self.assertIn("'password': 'P@$$wOrd'", user_str)
        self.assertIn("'first_name': 'Peter'", user_str)
        self.assertIn("'last_name': 'Pan'", user_str)

    def test_user_save_method(self):
        """Test save method."""
        user = User()
        initial_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, initial_updated_at)

    def test_user_create_from_dict(self):
        """Test creating User from dictionary."""
        user_dict = {
            '__class__': 'User',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'email': 'user@example.com',
            'password': 'secret',
            'first_name': 'Alice',
            'last_name': 'Wonderland'
        }
        user = User(**user_dict)
        self.assertEqual(user.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.password, 'secret')
        self.assertEqual(user.first_name, 'Alice')
        self.assertEqual(user.last_name, 'Wonderland')
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)
