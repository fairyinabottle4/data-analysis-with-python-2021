#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.distinct_characters"
distinct_characters = load(module_name, "distinct_characters")


def random_string(l):
    a=np.random.randint(ord('A'), ord('Z')+1, l)   # From 'A' to 'Z' 
    L = list(map(chr, a))
    indices = np.random.choice(l, int(l/4), replace=False) # places for l/4 spaces
    for i in indices:
        L[i] = ' '
    return "".join(L)

def compress(s):
    result=[]
    for c in s:
        if not result or result[-1] != c:
            result.append(c)
    return "".join(result)

@points('p01-12.1')
class DistinctCharacters(unittest.TestCase):

    
    def test_first(self):
        L = ["check", "look", "try", "pop"]
        d = distinct_characters(L)
        self.assertIsInstance(d, dict, f"distinct_characters should return a dictionary. Got {type(d)}")
        self.assertEqual(d["check"], 4, msg="Number of distinct characters of word 'check' was incorrect!")
        self.assertEqual(d["look"], 3, msg="Number of distinct characters of word 'look' was incorrect!")
        self.assertEqual(d["try"], 3, msg="Number of distinct characters of word 'try' was incorrect!")
        self.assertEqual(d["pop"], 2, msg="Number of distinct characters of word 'pop' was incorrect!")

    def test_empty(self):
        d = distinct_characters([])
        self.assertEqual(len(d), 0, msg="Empty list should result in an empty dictionary!")

    def test_random(self):
        for n in range(10):
            L=random_string(100).split()
            d = distinct_characters(L)
            self.assertEqual(len(d), len(set(L)))
            for s in L:
                self.assertEqual(len(compress(sorted(s))), d[s], msg="Number of distinct characters of word '%s' was incorrect!" % s)
            
if __name__ == '__main__':
    unittest.main()
    
