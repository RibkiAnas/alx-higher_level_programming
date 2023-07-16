#!/usr/bin/python3
"""
Defines a unittest for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def setUp(self):
        """
        Reset the __nb_objects class attribute before each test case.
        """
        Base._Base__nb_objects = 0

    def test_init(self):
        """
        Test for __init__ method.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 1, 2, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 12)

    def test_width(self):
        """
        Test for width attribute.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        with self.assertRaises(TypeError):
            r1.width = "10"

        with self.assertRaises(ValueError):
            r1.width = -10

    def test_height(self):
        """
        Test for height attribute.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        with self.assertRaises(TypeError):
            r1.height = "10"

        with self.assertRaises(ValueError):
            r1.height = -10

    def test_x(self):
        """
        Test for x attribute.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        with self.assertRaises(TypeError):
            r1.x = "10"

        with self.assertRaises(ValueError):
            r1.x = -10

    def test_y(self):
        """
        Test for y attribute.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        with self.assertRaises(TypeError):
            r1.y = "10"

        with self.assertRaises(ValueError):
            r1.y = -10

    def test_area(self):
        """
        Test for area method.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_str(self):
        """
        Test for __str__ method.
        """
        r1 = Rectangle(4, 6, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 4/6")

    def test_update(self):
        """
        Test for update method.
        """
        r1 = Rectangle(10, 20)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        """
        Test for to_dictionary method.
        """
        r1 = Rectangle(10, 20, 3, 4)
        d = {'id': 1, 'width': 10, 'height': 20, 'x': 3, 'y': 4}
        self.assertDictEqual(r1.to_dictionary(), d)


if __name__ == '__main__':
    unittest.main()
