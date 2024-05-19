#!/usr/bin/python3
"""Unittests for console.py."""

import unittest
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from models import storage
import os
import json


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand."""

    @classmethod
    def setUpClass(cls):
        """Setup for test methods."""
        cls.storage = FileStorage()
        cls.storage.all().clear()
        cls.storage.save()  # Save an empty file.json
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Cleanup after test methods."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_do_quit(self):
        """Test do_quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('quit'))
            self.assertEqual(f.getvalue(), '')

    def test_do_EOF(self):
        """Test do_EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
            self.assertEqual(f.getvalue(), '\n')

    def test_do_create(self):
        """Test do_create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb_command = HBNBCommand()
            hbnb_command.onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()
            self.assertIsNotNone(base_model_id)
            # Access the FileStorage instance from HBNBCommand
            # Reload to update the storage from file.json
            storage.save()
            self.assertIn(
                "{}.{}".format(BaseModel.__name__, base_model_id),
                storage.all()
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            user_id = f.getvalue().strip()
            self.assertIsNotNone(user_id)
            storage.save()
            self.assertIn(
                "{}.{}".format(User.__name__, user_id),
                storage.all()
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create NonExistentClass')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_do_show(self):
        """Test do_show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {base_model_id}')
            self.assertIn(
                f"[{BaseModel.__name__}] ({base_model_id})",
                f.getvalue()
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'show BaseModel 12345678-90ab-cdef-ghij-klmnopqrst')
            self.assertEqual(
                f.getvalue().strip(),
                "** no instance found **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'show NonExistentClass 12345678-90ab-cdef-ghij-klmnopqrst')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel')
            self.assertEqual(
                f.getvalue().strip(),
                "** instance id missing **"
            )

    def test_do_destroy(self):
        """Test do_destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy BaseModel {base_model_id}')
            self.assertEqual(f.getvalue().strip(), '')  # No output expected

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy BaseModel {base_model_id}')
            self.assertEqual(
                f.getvalue().strip(),
                "** no instance found **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'destroy NonExistentClass 12345678-90ab-cdef-ghij')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertEqual(
                f.getvalue().strip(),
                "** instance id missing **"
            )

    def test_do_all(self):
        """Test do_all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            self.assertTrue(
                f"[{BaseModel.__name__}]" in output
                and f"[{User.__name__}]" in output
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            output = f.getvalue().strip()
            self.assertTrue(f"[{BaseModel.__name__}]" in output)
            self.assertFalse(f"[{User.__name__}]" in output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all NonExistentClass')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_do_update(self):
        """Test do_update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} name "My BaseModel"'
            )
            self.assertEqual(f.getvalue().strip(), '')  # No output expected

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} name "My BaseModel"'
            )
            self.assertEqual(f.getvalue().strip(), '')  # No output expected

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f'update BaseModel {base_model_id} number 123')
            self.assertEqual(f.getvalue().strip(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} "first_name" "John"'
            )
            self.assertEqual(f.getvalue().strip(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} first_name "John"'
            )
            self.assertEqual(f.getvalue().strip(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} first_name\
                        "John" last_name "Doe"'
            )
            self.assertEqual(f.getvalue().strip(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {base_model_id} first_name\
                        "John" last_name "Doe" age 30'
            )
            self.assertEqual(f.getvalue().strip(), '')

        # Test updating with a dictionary
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'BaseModel.update({base_model_id}, {{ "first_name": "Jane",\
                        "last_name": "Doe", "age": 25 }})'
            )
            self.assertEqual(f.getvalue().strip(), '')

        # Check if attribute values were updated correctly
        objects = storage.all()
        base_model = objects[f"{BaseModel.__name__}.{base_model_id}"]
        self.assertEqual(base_model.first_name, "Jane")
        self.assertEqual(base_model.last_name, "Doe")
        self.assertEqual(base_model.age, 25)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'update NonExistentClass 12345678-90ab-cdef-ghij-\
                            klmnopqrst name "My Class"')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'update BaseModel 12345678-90ab-cdef-ghij-klmnopqrst\
                            name "My Class"')
            self.assertEqual(
                f.getvalue().strip(),
                "** no instance found **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel')
            self.assertEqual(
                f.getvalue().strip(),
                "** instance id missing **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'update BaseModel 12345678-90ab-cdef-ghij-klmnopqrst')
            self.assertEqual(
                f.getvalue().strip(),
                "** attribute name missing **"
            )

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'update BaseModel 12345678-90ab-cdef-ghij-klmnopqrst\
                            name')
            self.assertEqual(
                f.getvalue().strip(),
                "** value missing **"
            )

    def test_do_count(self):
        """Test do_count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('BaseModel.count()')
            output = f.getvalue().strip().splitlines()
            self.assertEqual(output[2], '6')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('count NonExistentClass')
            self.assertEqual(
                f.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_evaluate_value(self):
        """Test evaluate_value static method."""
        self.assertEqual(HBNBCommand.evaluate_value('"Hello"'), "Hello")
        self.assertEqual(HBNBCommand.evaluate_value("'World'"), "World")
        self.assertEqual(HBNBCommand.evaluate_value("123"), 123)
        self.assertEqual(HBNBCommand.evaluate_value("3.14"), 3.14)
        self.assertEqual(HBNBCommand.evaluate_value("[1, 2, 3]"), [1, 2, 3])
        self.assertIsNotNone(HBNBCommand.evaluate_value('"1, 2, 3"'))

    def test_default_command_missing_class(self):
        """Test default command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('.all()')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('.count()')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('.show()')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('.destroy()')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('.update()')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_default_command_invalid_class(self):
        """Test default command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('InvalidClassName.all()')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('InvalidClassName.count()')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'InvalidClassName.show("12345678-90ab-cdef-ghij-\
                            klmnopqrst")')
            self.assertEqual(
                    f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'InvalidClassName.destroy\
                            ("12345678-90ab-cdef-ghij-klmnopqrst")')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'InvalidClassName.update("12345678-90ab-cdef-ghij\
                            -klmnopqrst", {"name": "My Class"})')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_default_command_all(self):
        """Test default command with all()."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('BaseModel.all()')
            self.assertIn("[BaseModel]", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('User.all()')
            self.assertIn(f"[{User.__name__}]", f.getvalue())

    def test_default_command_count(self):
        """Test default command with count()."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertIn('1', f.getvalue().strip('\n'))

    def test_default_command_show(self):
        """Test default command with show()."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.show("{base_model_id}")')
            self.assertIn(
                    f"[{BaseModel.__name__}] ({base_model_id})", f.getvalue())

    def test_default_command_destroy(self):
        """Test default command with destroy()."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.destroy("{base_model_id}")')
            self.assertEqual(f.getvalue().strip(), '')

    def test_default_command_update(self):
        """Test default command with update()."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update("{base_model_id}",\
                    "name", "New Name")')
            self.assertEqual(f.getvalue().strip(), '')

    def test_default_command_update_with_invalid_id(self):
        """Test default command with update() with invalid id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'BaseModel.update("invalid_id", {"name":\
                            "My BaseModel"})')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_default_command_update_with_missing_attribute_name(self):
        """Test default command with update() with missing attribute name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("12345678-90ab-cdef-ghij-\
                    klmnopqrst")')
            self.assertEqual(
                    f.getvalue().strip(), "** attribute name missing **")

    def test_default_command_update_with_missing_value(self):
        """Test default command with update() with missing value."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    'BaseModel.update("12345678-90ab-cdef-ghij-klmnopqrst",\
                            "name")')
            self.assertEqual(f.getvalue().strip(), "** value missing **")
