#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.cleaning_data"
cleaning_data = load(module_name, "cleaning_data")
main = load(module_name, "main")
ph = patch_helper(module_name)


class CleaningData(unittest.TestCase):

    @points('p04-17.1')
    def test_shape(self):
        df = cleaning_data()
        self.assertEqual(df.shape, (4,5), "Incorrect shape!")
        
    @points('p04-17.1')
    def test_columns(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df.columns, ["President", "Start", "Last",
                                                   "Seasons", "Vice-president"],
                                      err_msg="Incorrect column names!")
        
    @points('p04-17.1')
    def test_dtypes(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df.dtypes, [object, int,  float,  int, object],
                                      err_msg="Incorrect column types!")
        
    @points('p04-17.1')
    def test_start(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df["Start"], [2017, 2009, 2001, 1993],
                                      err_msg="Incorrect values in Start column!")
        
    @points('p04-17.1')   
    def test_last(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df["Last"], [np.nan, 2017, 2009, 2001],
                                      err_msg="Incorrect values in Last column!")

    @points('p04-17.1')
    def test_seasons(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df["Seasons"], [1, 2, 2, 2],
                                      err_msg="Incorrect values in Seasons column!")

    @points('p04-17.2')
    def test_president(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df["President"],
                                      ["Donald Trump", "Barack Obama", "George Bush", "Bill Clinton"],
                                      err_msg="Incorrect values in President column!")

    @points('p04-17.2')
    def test_vice_president(self):
        df = cleaning_data()
        np.testing.assert_array_equal(df["Vice-president"],
                                      ["Mike Pence", "Joe Biden", "Dick Cheney", "Al Gore"],
                                      err_msg="Incorrect values in Vice-president column!")

if __name__ == '__main__':
    unittest.main()
    
