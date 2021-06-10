#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.cities"
cities = load(module_name, "cities")
ph = patch_helper(module_name)

@points('p04-01.1')
class Cities(unittest.TestCase):

    
    def test_first(self):
        df = cities()
        cols=df.columns
        ind=df.index
        self.assertEqual(cols[0], "Population", msg="Incorrect first column name!")
        self.assertEqual(cols[1], "Total area", msg="Incorrect second column name!")

        np.testing.assert_array_equal(ind, ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"],
                                      err_msg="Index was incorrect!")

        self.assertEqual(df.iloc[0,0], 643272, msg="Incorrect content in df.iloc[0,0]!")
        self.assertEqual(df.iloc[1,1], 528.03, msg="Incorrect content in df.iloc[1,1]!")
        self.assertEqual(df.iloc[2,0], 231853, msg="Incorrect content in df.iloc[2,0]!")
        self.assertEqual(df.iloc[3,1], 240.35, msg="Incorrect content in df.iloc[3,1]!")
        
if __name__ == '__main__':
    unittest.main()
    
