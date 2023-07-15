#!/usr/bin/python3
"""
Defines a unittest for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unittest for testing instantiation of
    the Rectangle class.
    """

    def test_attributes(self):
        """
        Test that attributes are assigned
        correctly.
        """
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 99)


if __name__ == '__main__':
    unittest.main()
