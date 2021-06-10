#!/usr/bin/env python3

import numpy as np
import re
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.sum_equation"
sum_equation = load(module_name, "sum_equation")

@points('p01-19.1')
class SumEquation(unittest.TestCase):

    
    def test_first(self):
        L = [1,5,7]
        result = sum_equation(L)
        self.assertIsInstance(result, str, f"sum_equation should return a string. Got {type(result)}")
        self.assertEqual(result, "1 + 5 + 7 = 13", msg="Incorrect result for input list %s!" % L)

    def test_random(self):
        L = list(np.random.randint(1, 100, 50))
        result = sum_equation(L)
        self.assertIsInstance(result, str, f"sum_equation should return a string. Got {type(result)}")
        m = re.match("(.*) = (\d+)", result)
        self.assertTrue(m)
        s = int(m.group(2))
        self.assertEqual(s, sum(L))
        a = m.group(1)
        L2 = list(map(int, a.split('+')))
        self.assertEqual(L, L2)
        
    def test_empty(self):
        result = sum_equation([])
        self.assertIsInstance(result, str, f"sum_equation should return a string. Got {type(result)}")
        self.assertEqual(result, "0 = 0", msg="Incorrect result for an empty input list!")
        
if __name__ == '__main__':
    unittest.main()
    
