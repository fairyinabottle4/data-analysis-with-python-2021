#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.special_missing_values"
special_missing_values = load(module_name, "special_missing_values")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-14.1')
class SpecialMissingValues(unittest.TestCase):

    
    def test_shape(self):
        df = special_missing_values()
        self.assertEqual(df.shape, (17,7), msg="Incorrect shape!")

    def test_columns(self):
        df = special_missing_values()
        np.testing.assert_array_equal(df.columns,
                                      ["Pos", "LW", "Title", "Artist", "Publisher", "Peak Pos", "WoC"],
                                      err_msg="Incorrect column names!")

    def test_called(self):
        with patch(ph("special_missing_values"), wraps=special_missing_values) as psmv,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            psmv.assert_called()
            prc.assert_called()
            
    def test_content(self):
        df = special_missing_values()
        np.testing.assert_array_equal(df["Pos"], [3,4,6,9,10,12,15,16,21,22,24,30,31,34,35,38,39],
                                   err_msg="The values in position column were incorrect!")
        
if __name__ == '__main__':
    unittest.main()
    
