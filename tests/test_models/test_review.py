#!/usr/bin/python3
"""Unittests for Review class."""

import unittest
from models.review import Review
from models.base_model import BaseModel
import datetime


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_review_inheritance(self):
        """Test if Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        """Test if Review has the correct attributes."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertIsInstance(review.id, str)
        self.assertTrue(hasattr(review, "created_at"))
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertIsInstance(review.updated_at, datetime.datetime)

    def test_review_creation(self):
        """Test Review object creation."""
        review = Review()
        self.assertIsNotNone(review)

    def test_review_place_id_setter(self):
        """Test setting the place_id attribute."""
        review = Review()
        review.place_id = "12345678-90ab-cdef-ghij-klmnopqrst"
        self.assertEqual(review.place_id, "12345678-90ab-cdef-ghij-klmnopqrst")

    def test_review_user_id_setter(self):
        """Test setting the user_id attribute."""
        review = Review()
        review.user_id = "98765432-10fe-dcba-9876"
        self.assertEqual(review.user_id, "98765432-10fe-dcba-9876")

    def test_review_text_setter(self):
        """Test setting the text attribute."""
        review = Review()
        review.text = "This is a great place to stay!"
        self.assertEqual(review.text, "This is a great place to stay!")

    def test_review_to_dict(self):
        """Test to_dict method."""
        review = Review()
        review.place_id = "12345678-90ab-cdef-ghij"
        review.user_id = "98765432-10fe-dcba-9876"
        review.text = "I had a wonderful time here."
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "12345678-90ab-cdef-ghij")
        self.assertEqual(review_dict["user_id"], "98765432-10fe-dcba-9876")
        self.assertEqual(review_dict["text"], "I had a wonderful time here.")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

    def test_review_str_representation(self):
        """Test __str__ method."""
        review = Review()
        review.place_id = "12345678-90ab-cdef-ghij"
        review.user_id = "98765432-10fe-dcba-9876"
        review.text = "The staff was very friendly."
        review_str = str(review)
        self.assertIn("[Review]", review_str)
        self.assertIn(review.id, review_str)
        self.assertIn("'place_id': '12345678-90ab-cdef-ghij'", review_str)
        self.assertIn("'user_id': '98765432-10fe-dcba-9876'", review_str)
        self.assertIn("'text': 'The staff was very friendly.'", review_str)

    def test_review_save_method(self):
        """Test save method."""
        review = Review()
        initial_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, initial_updated_at)

    def test_review_create_from_dict(self):
        """Test creating Review from dictionary."""
        review_dict = {
            '__class__': 'Review',
            'id': '12345678-90ab-cdef-ghij-klmnopqrst',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000',
            'place_id': '98765432-10fe-dcba-9876',
            'user_id': 'abcdef12-3456-7890-1234',
            'text': 'I would recommend this place'
        }
        review = Review(**review_dict)
        self.assertEqual(review.id, '12345678-90ab-cdef-ghij-klmnopqrst')
        self.assertEqual(review.place_id, '98765432-10fe-dcba-9876')
        self.assertEqual(review.user_id, 'abcdef12-3456-7890-1234')
        self.assertEqual(review.text, 'I would recommend this place')
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)
