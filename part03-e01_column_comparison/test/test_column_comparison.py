#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.column_comparison"
column_comparison = load(module_name, "column_comparison")

@points('p03-01.1')
class ColumnComparison(unittest.TestCase):

    
    def test_greater(self):
        n=10
        for m in range(2, 10):
            a=np.random.randn(n, m)
            result=column_comparison(a)
            for row in result:
                self.assertGreater(row[1], row[-2], msg="The row %s should not be in the result!" % row)

    def test_shape(self):
        n=10
        for m in range(2, 10):
            a=np.random.randn(n, m)
            result=column_comparison(a)
            self.assertEqual(result.shape[1], m, msg="The result should have as many columns as the input!")
            self.assertLessEqual(result.shape[0], n,
                                 msg="The result should have less or equal number of rows than the input!")

    def test_content(self):
        n=10
        for m in range(2, 10):
            a=np.random.randn(n, m)
            result=column_comparison(a)
            ri=0
            for row in a:
                if row[1] > row[-2]:
                    np.testing.assert_allclose(row, result[ri], err_msg="Incorrect result for array\n%s"%a)
                    ri += 1
            self.assertEqual(ri, result.shape[0], msg="Wrong number of rows for array\n%s" % a)
                
if __name__ == '__main__':
    unittest.main()
    
