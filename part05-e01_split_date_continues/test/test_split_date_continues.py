#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.split_date_continues"
split_date_continues = load(module_name, "split_date_continues")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p05-01.1')
class SplitDateContinues(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = split_date_continues()

    def setUp(self):
        self.df = split_date_continues()
    
    def test_shape(self):
        self.assertEqual(self.df.shape, (37128, 25), msg="Incorrect shape!")

    def test_columns(self):
        np.testing.assert_array_equal(self.df.columns[:6],
                                      ['Weekday', 'Day', 'Month', 'Year', 'Hour', 'Auroransilta'],
                                      err_msg="First six column names were incorrect!")

    def test_dtypes(self):
        np.testing.assert_array_equal(self.df.dtypes[:6],
                                      [object, int, int, int, int, float],
                                      err_msg="Incorrect column types in first six columns!")

    def test_content(self):
        value = self.df.loc[0, "Auroransilta"]
        self.assertTrue(np.isnan(value),
                         msg="Incorrect value on row 0 column Auroransilta, expected NaN got %f!" % value)
        self.assertEqual(self.df.loc[0, "Baana"], 8.0,
                         msg="Incorrect value on row 0 column Baana!")
        
    def test_calls(self):
        with patch(ph("split_date_continues"), wraps=split_date_continues) as psplit,\
            patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
            patch(ph("pd.concat"), wraps=pd.concat) as pconcat:
            main()
            psplit.assert_called_once()
            prc.assert_called_once()
            pconcat.assert_called()

if __name__ == '__main__':
    unittest.main()
    
