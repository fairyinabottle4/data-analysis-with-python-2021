#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.usemodule"
main = load(module_name, "main")
from src import triangle
from src import usemodule


@points('p01-20.1')
class Usemodule(unittest.TestCase):

    def check_attr(self, attr):
        self.assertTrue(hasattr(triangle, attr),
                        "The module triangle is missing the attribute %s!" % attr)
        
    
    def test_module(self):
        self.check_attr("__author__")
        self.assertGreaterEqual(len(triangle.__author__), 5,
                                msg="The __author__ attribute must have length at least five!")
        self.check_attr("__version__")
        self.assertEqual(type(triangle.__version__), str, "The version attribute should be a string.")
        self.assertGreater(len(triangle.__version__), 0, msg="The __version__ attribute must have positive length!")
        self.check_attr("__doc__")
        self.assertIsNotNone(triangle.__doc__, msg = "The module triangle has no docstring!")
        self.assertGreater(len(triangle.__doc__), 10,
                           "The docstring for module triangle is too short!")
        
        self.assertTrue(hasattr(triangle.hypothenuse, "__doc__"),
                         msg="The function triangle.hypothenuse has no docstring!")
        self.assertIsNotNone(triangle.hypothenuse.__doc__,
                            msg="The function triangle.hypothenuse has no docstring!")
        self.assertGreater(len(triangle.hypothenuse.__doc__), 10,
                           msg="The doctstring for function triangle.hypothenuse is too short!")

        self.assertTrue(hasattr(triangle.area, "__doc__"),
                         msg="The function triangle.area has no docstring!")
        self.assertIsNotNone(triangle.area.__doc__,
                            msg="The function triangle.area has no docstring!")
        self.assertGreater(len(triangle.area.__doc__), 10,
                           msg="The doctstring for function triangle.area is too short!")

    def test_hypotenuse(self):
        res = triangle.hypothenuse(1, 1)
        self.assertIsInstance(res, float, f"hypotenuse should return a floating point number when called with 1, 1. Got {type(res)}.")
        self.assertAlmostEqual(res, 1.414, 3, f"hypotenuse with sides 1, 1 should be ~1.414. Got {res}.")

    def test_area(self):
        res = triangle.area(1, 1)
        self.assertIsInstance(res, float, f"area should return a floating point number when called with 1, 1. Got {type(res)}.")
        self.assertAlmostEqual(res, 0.5, 3, f"area of triangle with sides 1, 1 should be 0.5. Got {res}.")
        
    def test_main(self):
        with patch('src.triangle.hypothenuse') as h:
            with patch('src.triangle.area') as a:
                usemodule.main()
                self.assertGreaterEqual(h.call_count, 1,
                                        msg="Expected 'triangle.hypothenuse' to have been called!")
                self.assertGreaterEqual(a.call_count, 1,
                                        msg="Expected 'triangle.area' to have been called!")
        
if __name__ == '__main__':
    unittest.main()
    
