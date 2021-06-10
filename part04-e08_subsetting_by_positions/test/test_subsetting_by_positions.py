#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.subsetting_by_positions"
subsetting_by_positions = load(module_name, "subsetting_by_positions")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-08.1')
class SubsettingByPositions(unittest.TestCase):

    
    def test_shape_and_columns(self):
        df = subsetting_by_positions()
        self.assertEqual(df.shape, (10,2), msg="The returned DataFrame had wrong shape!")
        #np.testing.assert_array_equal(df.index, range(10), err_msg="Incorrect index")
        np.testing.assert_array_equal(df.columns, ["Title", "Artist"],
                                      err_msg="Incorrect column names")

    def test_called(self):
        with patch(ph("subsetting_by_positions"), wraps=subsetting_by_positions) as psbp,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            psbp.assert_called()
            prc.assert_called()
            
if __name__ == '__main__':
    unittest.main()
    
