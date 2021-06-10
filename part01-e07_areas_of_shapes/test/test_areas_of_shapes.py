#!/usr/bin/env python3

import math
import re
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.areas_of_shapes"
main = load(module_name, "main")

@points('p01-07.1')
class AreasOfShapes(unittest.TestCase):


        
    def test_empty(self):
        with patch('builtins.input', side_effect=[""]) as p:
            main()
            result=get_stdout().split('\n')
            self.assertEqual(len(result), 1, msg="Program should quit immediately, when empty string is given!")


    def test_one_query(self):
        with patch('builtins.input', side_effect=["triangle", "20", "5", ""]) as p:
            main()
            result=get_stdout().split('\n')
            self.assertEqual(len(result), 1, msg="Expected exactly one result line!")
            pattern = r"^The area is (.*)"
            self.assertRegex(result[0], pattern, msg="Expected output about the resulting area!")
            m = re.match(pattern, result[0])
            self.assertEqual(float(m.group(1)), 20*5/2, msg="Wrong area for a triangle with dimensions 20 and 5!")

    def test_many_queries(self):
        input_sequence = ["triangle", "20", "5", "rectangel",
                          "rectangle", "20", "4", "circle", "10", ""]
        with patch('builtins.input', side_effect=input_sequence) as p:
            main()
            result=get_stdout().split('\n')
            self.assertEqual(len(result), 4, msg="Expected four lines of output for input sequence %s!" % input_sequence)
            pattern = r"^The area is (.*)"
            self.assertRegex(result[0], pattern, msg="Expected output about the resulting area!")
            m = re.match(pattern, result[0])
            self.assertEqual(float(m.group(1)), 20*5/2, msg="Wrong area for a triangle with dimensions 20 and 5!")

            self.assertEqual(result[1], "Unknown shape!", msg="Incorrect error message for shape 'rectangel'!")

            self.assertRegex(result[2], pattern, msg="Expected output about the resulting area!")
            m = re.match(pattern, result[2])
            self.assertEqual(float(m.group(1)), 20*4, msg="Wrong area for a rectangle with dimensions 20 and 4!")

            self.assertRegex(result[3], pattern, msg="Expected output about the resulting area!")
            m = re.match(pattern, result[3])
            self.assertAlmostEqual(float(m.group(1)), math.pi*10**2, places=4, msg="Wrong area for circle with radius 10!")


if __name__ == '__main__':
    unittest.main()
    
