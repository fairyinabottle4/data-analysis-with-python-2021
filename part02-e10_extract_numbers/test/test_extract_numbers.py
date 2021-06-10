#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.extract_numbers"
extract_numbers = load(module_name, "extract_numbers")

@points('p02-10.1')
class ExtractNumbers(unittest.TestCase):

    
    def test_first(self):
        s="abd 123 1.2 test 13.2 -1"
        L=extract_numbers(s)
        self.assertEqual(L, [123, 1.2, 13.2, -1], msg="Incorrect result for string %s!" % s)

    def test_calls(self):
        with patch('builtins.float', wraps=float) as fl:
            extract_numbers("abd 123 1.2 test 13.2 -1")
            self.assertEqual(fl.call_count, 4, msg="Expected 4 calls of 'float'!")

    def test_random(self):
        L=list(np.random.randint(-100,100, 50))
        s=" ".join(map(str, L))
        result = extract_numbers(s)
        self.assertEqual(L, result, msg="Incorrect result for string %s!" % s)

if __name__ == '__main__':
    unittest.main()
    
