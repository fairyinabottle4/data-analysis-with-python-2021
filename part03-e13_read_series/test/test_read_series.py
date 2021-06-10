#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.read_series"
read_series = load(module_name, "read_series")
ph = patch_helper(module_name)

@points('p03-13.1')
class ReadSeries(unittest.TestCase):

    
    def test_first(self):
        with patch("builtins.input", side_effect=["a  12", "b	 3", "c	50", ""]) as i:
            s = read_series()
        self.assertIsInstance(s, pandas.core.series.Series, msg="You did not return a Series object!")
        self.assertIsInstance(s.dtype, object, msg="Expected dtype object!")
        np.testing.assert_array_equal(s.values, ["12","3","50"], err_msg="Incorrect values in Series!")
        np.testing.assert_array_equal(s.index, ["a", "b", "c"], err_msg="Incorrect index!")

    def test_empty(self):
        with patch("builtins.input", side_effect=[""]) as i:
            s = read_series()
        self.assertIsInstance(s, pandas.core.series.Series, msg="You did not return a Series object!")
        self.assertIsInstance(s.dtype, object)
        self.assertEqual(len(s), 0, msg="Expected a Series of length 0!")

    def test_error(self):
        with patch("builtins.input", side_effect=["0 a", "xxxxx"]) as i:
            with self.assertRaises(Exception, msg="For malformed input an exception should occur!"):
                read_series()
            
if __name__ == '__main__':
    unittest.main()
    
