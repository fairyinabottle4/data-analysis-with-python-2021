#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.row_and_column_vectors"
get_row_vectors = load(module_name, "get_row_vectors")
get_column_vectors = load(module_name, "get_column_vectors")

@points('p02-12.1')
class RowsAndColumns(unittest.TestCase):

    
    def test_row_types(self):
        a=np.random.randint(0,10, (4,5))
        rows=get_row_vectors(a)
        self.assertIsInstance(rows, list, msg="The function get_row_vectors should return a list!")
        for row in rows:
            self.assertIsInstance(row, np.ndarray, msg="The list elements should be arrays!")

    def test_columns_types(self):
        a=np.random.randint(0,10, (4,5))
        columns=get_column_vectors(a)
        self.assertIsInstance(columns, list,
                              msg="The function get_column_vectors should return a list!")
        for column in columns:
            self.assertIsInstance(column, np.ndarray, msg="The list elements should be arrays!")
    
    def test_row_count(self):
        a = np.random.randint(0, 100, (3, 5))
        self.assertEqual(len(get_row_vectors(a)), 3, msg="Wrong number of rows")
    
    def test_column_count(self):
        a = np.random.randint(0, 100, (3, 5))
        self.assertEqual(len(get_column_vectors(a)), 5, msg="Wrong number of columns")

    def test_row_content(self):
        n=4
        m=5
        a=np.random.randint(0,10, (n,m))
        rows=get_row_vectors(a)
        for ri, row in enumerate(rows):
            self.assertEqual(row.shape, (1,m), msg="Incorrect shape!")
            for ci in range(m):
                self.assertEqual(a[ri, ci], row[0,ci], msg="Incorrect value at (%i,%i)!" % (ri,ci))

    def test_column_content(self):
        n=4
        m=5
        a=np.random.randint(0,10, (n,m))
        columns=get_column_vectors(a)
        for ci, column in enumerate(columns):
            self.assertEqual(column.shape, (n,1), msg="Incorrect shape!")
            for ri in range(n):
                self.assertEqual(a[ri, ci], column[ri,0], msg="Incorrect value at (%i,%i)!" % (ri,ci))

                
if __name__ == '__main__':
    unittest.main()
    
