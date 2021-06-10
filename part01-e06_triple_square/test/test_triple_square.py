#!/usr/bin/env python3

import re
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.triple_square"
main = load(module_name, "main")
triple = load(module_name, "triple")
square = load(module_name, "square")

class TripleSquare(unittest.TestCase):

    
    def content_helper(self, countlist):
        main()
        result=get_stdout().split('\n')
        l=len(result)
        self.assertIn(l, countlist, msg="Wrong number of printed lines: %i!" % l)
        for i, line in zip(range(l), result):
            j = i + 1
            pattern = r"triple\((\d+)\)==(\d+) square\((\d+)\)==(\d+)"
            self.assertRegex(line, pattern, msg="The output line was not in correct format!")
            m = re.match(pattern, line)
            p1=int(m.group(1))
            t=int(m.group(2))
            p2=int(m.group(3))
            s=int(m.group(4))
            self.assertEqual(p1, j, msg="Wrong argument for 'triple' on line %s!" % line)
            self.assertEqual(p2, j, msg="Wrong argument for 'square' on line %s!" % line)
            self.assertEqual(t, 3*j, msg="Wrong result from 'triple' on line %s!" % line)
            self.assertEqual(s, j**2, msg="Wrong result from 'triple' on line %s!" % line)

    def call_helper(self, countlist):
        with patch(module_name+'.triple', side_effect=triple) as tr:
            with patch(module_name+'.square', side_effect=square) as sq:
                main()
                self.assertIn(len(tr.mock_calls), countlist,
                              msg="Are you sure you called 'triple' the right number of times?")
                self.assertIn(len(sq.mock_calls), countlist,
                              msg="Are you sure you called 'square' the right number of times?")
        

    @points('p01-06.1')
    def test_tiple_output_and_type(self):
        o = triple(6)
        self.assertIsInstance(o, int, f"Return type of triple should be int when tripling ints. Got {type(o)}")
        self.assertEqual(o, 18, f"triple(6) should be 18. Got {o}")

    @points('p01-06.1')
    def test_square_output_and_type(self):
        o = square(3)
        self.assertIsInstance(o, int, f"Return type of square should be int when squaring ints. Got {type(o)}")
        self.assertEqual(o, 9, f"square(3) should be 9. Got {o}")

    @points('p01-06.1')
    def test_calls(self):
        self.content_helper([3, 10])
        self.call_helper([4, 10])

    @points('p01-06.2')
    def test_calls2(self):
        self.content_helper([3])
        self.call_helper([4])

        
if __name__ == '__main__':
    unittest.main()
    
