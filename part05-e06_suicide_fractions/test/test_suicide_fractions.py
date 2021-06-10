#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.suicide_fractions"
suicide_fractions = load(module_name, "suicide_fractions")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-06.1')
class SuicideFractions(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.s = suicide_fractions()
        
    def setUp(self):
        self.s = suicide_fractions()
        
    def test_shape(self):
        self.assertEqual(self.s.shape, (141,), msg="The return Series has incorrect shape!")

    def test_type(self):
        self.assertIsInstance(self.s, pd.Series, msg="You should return a Series object!")
        self.assertEqual(self.s.dtype, float, msg="The dtype of Series should be float!")

    def test_index(self):
        ind = ["Albania", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia"]
        self.assertCountEqual(self.s.index[:5], ind, msg="First five indices were incorrect!")

    def test_nulls(self):
        nulls = self.s.isnull().sum()
        self.assertEqual(nulls, 23, msg="Wrong number of missing values in the Series!")

    def test_content(self):
        self.assertAlmostEqual(self.s["Albania"], 0.000035, places=6, msg="Incorrect mean suicide fraction for Albania!")
        self.assertAlmostEqual(self.s["Belgium"], 0.000222, places=6, msg="Incorrect mean suicide fraction for Belgium!")
        self.assertAlmostEqual(self.s["Finland"], 0.000228, places=6, msg="Incorrect mean suicide fraction for Finland!")
            
    def test_calls(self):
        method = spy_decorator(pd.core.frame.DataFrame.groupby, "groupby") 
        with patch(ph("suicide_fractions"), wraps=suicide_fractions) as psf,\
             patch.object(pd.core.frame.DataFrame, "groupby", new=method) as pgroupby,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            psf.assert_called_once()
            prc.assert_called_once()
            method.mock.assert_called_once()
            args, kwargs = method.mock.call_args
            correct = ((len(args) > 0 and args[0]== "country") or
                       ("by" in kwargs and kwargs["by"] == "country"))
            self.assertTrue(correct, msg="Wrong or missing argument to groupby method!")
            #self.assertEqual(args[0], "country", msg="Wrong argument to groupby method!")

 
if __name__ == '__main__':
    unittest.main()
    
