#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.rows_and_columns"
get_rows = load(module_name, "get_rows")
get_columns = load(module_name, "get_columns")

@points('p02-11.1')
class RowsAndColumns(unittest.TestCase):

    
    def test_row_types(self):
        a=np.random.randint(0,10, (4,5))
        rows=get_rows(a)
        self.assertIsInstance(rows, list, msg="The function get_rows should return a list!")
        self.assertEqual(len(rows), 4, msg="Incorrect number of elements in list")
        for row in rows:
            self.assertIsInstance(row, np.ndarray, msg="The list elements should be arrays!")

    def test_columns_types(self):
        a=np.random.randint(0,10, (4,5))
        columns=get_columns(a)
        self.assertIsInstance(columns, list, msg="The function get_columnss should return a list!")
        self.assertEqual(len(columns), 5, msg="Incorrect number of elements in list")
        for column in columns:
            self.assertIsInstance(column, np.ndarray, msg="The list elements should be arrays!")

    def test_row_content(self):
        n=4
        m=5
        a=np.random.randint(0,10, (n,m))
        rows=get_rows(a)
        self.assertEqual(len(rows), n, msg="Incorrect number of elements in list")
        for ri, row in enumerate(rows):
            self.assertEqual(row.shape, (m,), msg="Incorrect shape!")
            for ci in range(m):
                self.assertEqual(a[ri, ci], row[ci], msg="Incorrect value at (%i,%i)!" % (ri,ci))

    def test_column_content(self):
        n=4
        m=5
        a=np.random.randint(0,10, (n,m))
        columns=get_columns(a)
        self.assertEqual(len(columns), m, msg="Incorrect number of elements in list")
        for ci, column in enumerate(columns):
            self.assertEqual(column.shape, (n,), msg="Incorrect shape!")
            for ri in range(n):
                self.assertEqual(a[ri, ci], column[ri], msg="Incorrect value at (%i,%i)!" % (ri,ci))

                
if __name__ == '__main__':
    unittest.main()
    
