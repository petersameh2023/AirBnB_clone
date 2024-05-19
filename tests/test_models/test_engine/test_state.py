#!/usr/bin/python3
"""Unittests for State class."""

import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_state_inheritance(self):
        """Test if State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        """Test if State has the correct attributes."""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertIsInstance(state.id, str)
        self.assertTrue(hasattr(state, "created_at"))
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertIsInstance(state.updated_at, datetime.datetime)

    def test_state_creation(self):
        """Test State object creation."""
        state = State()
        self.assertIsNotNone(state)

    def test_state_name_setter(self):
        """Test setting the name attribute."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        """Test to_dict method."""
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "New York")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_state_str_representation(self):
        """Test __str__ method."""
        state = State()
        state.name = "Texas"
        state_str = str(state)
        self.assertIn("[State]", state_str)
        self.assertIn(state.id, state_str)
        self.assertIn("'name': 'Texas'", state_str)

    def test_state_save_method(self):
        """Test save method."""
        state = State()
        initial_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, initial_updated_at)

    def test_state_create_from_dict(self):
        """Test creating State from dictionary."""
        state_dict = {
            '__class__': 'State',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'name': 'Florida'
        }
        state = State(**state_dict)
        self.assertEqual(state.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(state.name, 'Florida')
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
