#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.detect_ranges"
detect_ranges = load(module_name, "detect_ranges")

@points('p01-10.1')
class DetectRanges(unittest.TestCase):


    def test_first(self):
        L = [2,5,4,8,12,6,7,10,13]
        Lc = L.copy()
        result = detect_ranges(L)
        self.assertIsInstance(result, list, f"detect_ranges should return a list. Got {type(result)}")
        self.assertEqual(L, Lc, msg="Do not modify the input list %s!" % Lc)
        self.assertEqual(result, [2, (4, 9), 10, (12, 14)], msg="Incorrect result for the input list %s!" % L)

    def test_second(self):
        L = [1, 2, 4]
        res = detect_ranges(L)
        self.assertEqual(res, [(1, 3), 4], msg=f"Incorrect result for the input list {L}!")

    def test_third(self):
        L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
        res = detect_ranges(L)
        self.assertEqual(res, [(88, 91), (92, 98)], msg=f"Incorrect result for the input list {L}!")

    def test_fourth(self):
        L = [-2, 0, 1, 2, 3]
        res = detect_ranges(L)
        self.assertEqual(res, [-2, (0, 4)], msg=f"Incorrect result for the input list {L}!")

    def test_fifth(self):
        L = [4, 2, 0, -2, -4]
        self.assertEqual(detect_ranges(L), list(reversed(L)), msg=f"Incorrect result for the input list {L}!")

    def test_random(self):
        for i in range(10):
            L = [int(i) for i in set(np.random.randint(-100, 100, 10))]
            mi = min(L)
            ma = max(L)
            complement = list(set(range(mi, ma+1)) - set(L))
            result = detect_ranges(L)
            complement_result = detect_ranges(complement)
            catenation = []   # Expand the ranges into this catenation, contains all the elements in the ranges
            for x in result:
                try:
                    a, b = x
                    catenation.extend(range(a,b))
                except TypeError:
                    catenation.append(x)
            self.assertEqual(sorted(L), catenation, msg="Wrong result for input list %s!" % L)
            catenation = []   # Expand the complement ranges into this catenation, contains all the elements in the complement
            for x in complement_result:
                try:
                    a, b = x
                    catenation.extend(range(a,b))
                except TypeError:
                    catenation.append(x)
            self.assertEqual(sorted(complement), catenation, msg=f"Wrong result for input list {catenation}!")
            self.assertEqual(len(result), len(complement_result)+1, msg=f"Wrong number of ranges for one of input lists:\n{L}\n=>\n{result}\nand\n{catenation}\n=>\n{complement_result}!")


if __name__ == '__main__':
    unittest.main()

