#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.transform"
transform = load(module_name, "transform")

@points('p01-16.1')
class Transform(unittest.TestCase):

    
    def test_first(self):
        s1 = "1 5 3"
        s2 = "2 6 -1"
        result = transform(s1, s2)
        self.assertIsInstance(result, list, f"transfrom should return a list. Got {type(result)}")
        self.assertEqual(result, [2, 30, -3], msg="Incorrect result for input strings %s and %s" % (s1, s2))

    def test_empty(self):
        result = transform("", "")
        self.assertIsInstance(result, list, f"transfrom should return a list. Got {type(result)}")
        self.assertEqual(result, [], msg="""Two empty strings should return an empty list!
Have you noted that s.split() and s.split(" ") work differently!""")

    def test_random(self):
        L1 = np.random.randint(-100, 100, 50)
        L2 = np.random.randint(-100, 100, 50)
        s1 = " ".join(map(str, L1))
        s2 = " ".join(map(str, L2))
        result = transform(s1, s2)
        self.assertIsInstance(result, list, f"transfrom should return a list. Got {type(result)}")
        for a, b, c in zip(L1, L2, result):
            self.assertEqual(a*b, c)

    def test_calls(self):
        s1 = "1 5 3"
        s2 = "2 6 -1"
        with patch('builtins.zip') as z:
            with patch('builtins.map') as m:
                result = transform(s1, s2)
                z.assert_called()
                self.assertGreaterEqual(len(m.mock_calls), 2)
            
if __name__ == '__main__':
    unittest.main()
    
