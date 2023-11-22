#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os

#  import json
import console

# import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    # function to set up the test
    def setUp(self):
        """set up for test"""
        self.console = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """tears down at the end of the test"""
        del cls.consol

    # function to remove temporary JSON file
    # function to reset FileStorage objects
    def removeJSON(self):
        """remove temporary JSON file"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def resetStorage(self):
        """reset FileStorage objects"""
        FileStorage._FileStorage__objects = {}

    # function that test if the file is executable
    def test_is_executable(self):
        """test if the file is executable"""
        self.assertTrue(os.access("console.py", os.X_OK))

    # function that tests the console documentation
    def test_console_docstring(self):
        """test console documentation"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    # function that tests the pep8 style
    def test_pep8_console(self):
        """test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    # function that tests the base model documentation
    def test_base_model_docstring(self):
        """test base model documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    # function that tests the user documentation
    def test_user_docstring(self):
        """test user documentation"""
        self.assertIsNotNone(User.__doc__)

    # function that tests the state documentation
    def test_state_docstring(self):
        """test state documentation"""
        self.assertIsNotNone(State.__doc__)

    # function that tests the city documentation
    def test_city_docstring(self):
        """test city documentation"""
        self.assertIsNotNone(City.__doc__)

    # function that tests the amenity documentation
    def test_amenity_docstring(self):
        """test amenity documentation"""
        self.assertIsNotNone(Amenity.__doc__)

    # function that tests the place documentation
    def test_place_docstring(self):
        """test place documentation"""
        self.assertIsNotNone(Place.__doc__)

    # function that tests the review documentation
    def test_review_docstring(self):
        """test review documentation"""
        self.assertIsNotNone(Review.__doc__)

    # function that tests the FileStorage documentation
    def test_file_storage_docstring(self):
        """test file storage documentation"""
        self.assertIsNotNone(FileStorage.__doc__)

    # function that tests the all function
    def test_all(self):
        """test all function"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")

    # function that tests the create function
    def test_create(self):
        """test create function"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create State")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create City")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create User")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create Place")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create Amenity")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create Review")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.assertTrue(len(f.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd(
                'create Place city_id="0001" \
                user_id="0001" name="My_little_house"\
                number_rooms=4 number_bathrooms=2 max_guest=10\
                price_by_night=300 latitude=37.773972 longitude=-122.431297'
            )
            self.assertTrue(len(f.getvalue()) > 0)
