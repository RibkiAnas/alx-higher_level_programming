#!/usr/bin/python3
"""
Defines a unittest for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unittest for testing instantiation of
    the Base class.
    """
    def setUp(self):
        """
        Reset __nb_objects before each test
        """
        Base._Base__nb_objects = 0

    def test_id_none(self):
        """
        Test id when no id is passed to
        constructor.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_not_none(self):
        """
        Test id when id is passed to
        constructor
        """
        b1 = Base(12)
        b2 = Base(14)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 14)

    def test_id_mixed(self):
        """
        Test id with a mix of passed and not
        passed id
        """
        b1 = Base()
        b2 = Base(14)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 14)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
