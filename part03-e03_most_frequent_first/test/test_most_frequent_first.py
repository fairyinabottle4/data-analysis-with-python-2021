#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from collections import defaultdict
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.most_frequent_first"
most_frequent_first = load(module_name, "most_frequent_first")

def sort_rows(a):
    """Sort rows in lexicographical order."""
    n,m = a.shape
    keys = np.arange(m-1,-1,-1)   # columns from last to first
    return a[np.lexsort(a.T[keys])]
    
@points('p03-03.1')
class MostFrequentFirst(unittest.TestCase):

    
    def test_same_rows(self):
        n, m = 10, 10
        a = np.random.randint(0,10, (n, m))
        for c in range(m):
            result = most_frequent_first(a, c)
            np.testing.assert_allclose(sort_rows(a), sort_rows(result),
                                       err_msg="The result does not contain the same rows as the input "
                                       "for column %i and array %s" % (c, a))

    def test_content(self):
        n, m = 10, 10
        for c in range(m):
            a = np.random.randint(0,10, (n, m))
            result = most_frequent_first(a, c)
            multiplicities=defaultdict(int)
            b=a[:, c]
            for x in b:
                multiplicities[x] += 1
            previous_multiplicity=np.inf
            for x in result[:,c]:
                self.assertGreaterEqual(previous_multiplicity, multiplicities[x],
                                        msg="Result\n%s not correctly sorted according to column %i!" % (result,c))
                previous_multiplicity = multiplicities[x]
            

if __name__ == '__main__':
    unittest.main()
    
