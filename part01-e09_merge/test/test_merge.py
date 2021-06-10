#!/usr/bin/env python3

import numpy as np
import unittest
import timeit
from unittest.mock import patch
import copy

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.merge"
merge = load(module_name, "merge")

@points('p01-09.1')
class Merge(unittest.TestCase):

    def test_non_mutating(self):
        L1_orig = [1,5,9,12]
        L2_orig = [2,6,10]
        L1 = copy.copy(L1_orig)
        L2 = copy.copy(L2_orig)
        result = merge(L1, L2)
        self.assertEqual(L1, L1_orig, msg="You are not allowed to modify the input lists!")
        self.assertEqual(L2, L2_orig, msg="You are not allowed to modify the input lists!")

    def test_first(self):
        L1 = [1,5,9,12]
        L2 = [2,6,10]
        result = merge(L1, L2)
        self.assertIsInstance(result, list, f"merge should return a list. Got {type(result)}")
        self.assertEqual(result, sorted(L1+L2), msg="Not correct result for input lists %s and %s!" % (L1,L2))

    def test_random(self):
        L = sorted(np.random.randint(-100, 100, 30))
        # Choose randomly 20 elements out of 30 to be in list L1, rest in L2
        indices = set(np.random.choice(30, 20, replace=False))
        L1=[]
        L2=[]
        for i,x in enumerate(L):
            if i in indices:
                L1.append(x)
            else:
                L2.append(x)
        result = merge(L1,L2)
        self.assertEqual(len(result), len(L), msg="Incorrect length of result list for input lists %s and %s!" % (L1, L2))
        self.assertEqual(result, L, msg="Incorrect result for input lists %s and %s!" % (L1, L2))

    def test_calls(self):
        with patch('builtins.sorted') as s:
            merge([1,5,9,12], [2,6,10])
            self.assertEqual(sorted.call_count, 0, msg="You weren't allowed to use function 'sorted'!")
        # The below does not work, because list is defined in C
        #with patch.object(list, 'sort') as sort_method:
        with open("src/merge.py") as in_file:
            for line in in_file:
                self.assertFalse(".sort" in line, "You weren't allowed to use the 'sort' method")


if __name__ == '__main__':
    unittest.main()

