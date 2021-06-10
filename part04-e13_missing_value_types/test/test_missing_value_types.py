#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.missing_value_types"
missing_value_types = load(module_name, "missing_value_types")
ph = patch_helper(module_name)

@points('p04-13.1')
class MissingValueTypes(unittest.TestCase):

    
    def test_shape(self):
        df = missing_value_types()
        self.assertEqual(df.shape, (6,2), msg="Incorrect shape!")

    def test_index(self):
        df = missing_value_types()
        np.testing.assert_array_equal(df.index, ["United Kingdom","Finland", "USA","Sweden","Germany","Russia"],
                                      err_msg="Incorrect index!")

    def test_columns(self):
        df = missing_value_types()
        np.testing.assert_array_equal(df.columns, ["Year of independence", "President"],
        err_msg="Incorrect column names!")

    def test_dtypes(self):
        df = missing_value_types()
        self.assertEqual(df.dtypes[0], np.float64, msg="Incorrect type in column 0!")
        self.assertEqual(df.dtypes[1], object, msg="Incorrect type in column 1!")

    def test_nan(self):
        df = missing_value_types()
        m = df.isnull().values
        self.assertTrue(m[0,0], msg="Expected a null value in position 0, 0!")
        self.assertTrue(m[0,1], msg="Expected a null value in position 0, 1!")
        self.assertTrue(m[3,1], msg="Expected a null value in position 3, 1!")
        self.assertTrue(m[4,0], msg="Expected a null value in position 4, 0!")
        s=m.sum()
        self.assertEqual(s, 4, msg="Wrong number of missing values!")
        
if __name__ == '__main__':
    unittest.main()
    
