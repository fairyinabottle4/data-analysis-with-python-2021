#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.positive_list"
positive_list = load(module_name, "positive_list")

@points('p01-17.1')
class PositiveList(unittest.TestCase):

    
    def test_first(self):
        L=[2,-2,0,1,-7]
        result = positive_list(L)
        self.assertIsInstance(result, list, f"positive_list should return a list. Got {type(result)}")
        self.assertEqual(result, [2,1], msg="Wrong result for list %s!" % L)

    def test_random(self):
        for i in range(4):
            L = np.random.randint(-100, 100, 50)
            result = positive_list(L)
            self.assertIsInstance(result, list, f"positive_list should return a list. Got {type(result)}")
            correct = [ x  for x in L if x > 0]
            self.assertEqual(result, correct, msg="Wrong result for list %s!" % L)

    def test_calls(self):
        with patch('builtins.filter') as f:
            result = positive_list([2,-2,0,1,-7])
            f.assert_called()

if __name__ == '__main__':
    unittest.main()
    
