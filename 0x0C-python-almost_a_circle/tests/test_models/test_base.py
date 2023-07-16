#!/usr/bin/python3
"""
Defines a unittest for Base class.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def setUp(self):
        """
        Reset the __nb_objects class attribute
        before each test case.
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        Test for id attribute.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_to_json_string(self):
        """
        Test for to_json_string method.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """
        Test for from_json_string method.
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])

    def test_save_to_file(self):
        """
        Test for save_to_file method.
        """
        filename = "Base.json"
        if os.path.exists(filename):
            os.remove(filename)

        Base.save_to_file(None)
        with open(filename, "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file(self):
        """
        Test for load_from_file method.
        """
        filename = "Base.json"
        if os.path.exists(filename):
            os.remove(filename)

        self.assertEqual(Base.load_from_file(), [])

    def test_save_to_file_csv(self):
        """
        Test saving a list of Rectangle and Square
        objects to a CSV file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(),
                             "1,10,7,2,8\n2,2,4,0,0\n")

        s1 = Square(5)
        s2 = Square(7, 9)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "3,5,5,0,0\n4,7,7,9,0\n")

    def test_load_from_file_csv(self):
        """
        Test loading a list of Rectangle and Square
        objects from a CSV file.
        """
        list_rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rects), 2)
        r1 = list_rects[0]
        self.assertEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                         [1, 10, 7, 2, 8])
        r2 = list_rects[1]
        self.assertEqual([r2.id, r2.width, r2.height, r2.x, r2.y],
                         [2, 2, 4, 0, 0])

        list_squares = Square.load_from_file_csv()
        self.assertEqual(len(list_squares), 2)
        s1 = list_squares[0]
        self.assertEqual([s1.id, s1.size, s1.x, s1.y], [3, 5, 5, 0])
        s2 = list_squares[1]
        self.assertEqual([s2.id, s2.size, s2.x, s2.y], [4, 7, 7, 9])


if __name__ == '__main__':
    unittest.main()
