#!/usr/bin/python3
"""
Defines a unittest for Square class.
"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def setUp(self):
        """
        Reset the __nb_objects class attribute
        before each test case.
        """
        Base._Base__nb_objects = 0

    def test_init(self):
        """
        Test for __init__ method.
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(10, 1, 2, 12)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 12)

    def test_size(self):
        """
        Test for size attribute.
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError):
            s1.size = "10"

        with self.assertRaises(ValueError):
            s1.size = -10

    def test_x(self):
        """
        Test for x attribute.
        """
        s1 = Square(10)
        self.assertEqual(s1.x, 0)

        with self.assertRaises(TypeError):
            s1.x = "10"

        with self.assertRaises(ValueError):
            s1.x = -10

    def test_y(self):
        """
        Test for y attribute.
        """
        s1 = Square(10)
        self.assertEqual(s1.y, 0)

        with self.assertRaises(TypeError):
            s1.y = "10"

        with self.assertRaises(ValueError):
            s1.y = -10

    def test_area(self):
        """
        Test for area method.
        """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_str(self):
        """
        Test for __str__ method.
        """
        s1 = Square(5, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 5")

    def test_update(self):
        """
        Test for update method.
        """
        s1 = Square(10)
        s1.update(89)
        self.assertEqual(s1.id, 89)

        s1.update(89, 2)
        self.assertEqual(s1.size, 2)

        s1.update(89, 2, 3)
        self.assertEqual(s1.x, 3)

        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        """
        Test for to_dictionary method.
        """
        s1 = Square(10, 2, 3)
        d = {'id': 1, 'size': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(s1.to_dictionary(), d)


if __name__ == '__main__':
    unittest.main()
