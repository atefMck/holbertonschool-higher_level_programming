#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ tests for Base class """
    def test_base(self):
        """
        Tests when d is given or not
        """
        b = Base()
        self.assertEqual(b.id, 1)
