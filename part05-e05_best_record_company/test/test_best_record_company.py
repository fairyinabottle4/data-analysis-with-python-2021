#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.best_record_company"
best_record_company = load(module_name, "best_record_company")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-05.1')
class BestRecordCompany(unittest.TestCase):

    
    def test_shape(self):
        df = best_record_company()
        self.assertEqual(df.shape, (7,7), msg="Incorrect shape!")

    
    def test_column_names(self):
        cols = ['Pos', 'LW', 'Title', 'Artist', 'Publisher', 'Peak Pos', 'WoC']
        df = best_record_company()
        self.assertCountEqual(df.columns, cols, msg="Incorrect column names!") 

    def test_publisher(self):
        df = best_record_company()
        self.assertEqual(1, len(df["Publisher"].unique()), msg="The publisher should always be the same in the result!")


    def test_calls(self):
        method = spy_decorator(pd.core.frame.DataFrame.groupby, "groupby") 
        with patch(ph("best_record_company"), wraps=best_record_company) as pbrc,\
             patch.object(pd.core.frame.DataFrame, "groupby", new=method) as pgroupby,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            pbrc.assert_called_once()
            prc.assert_called_once()
            method.mock.assert_called_once()
            args, kwargs = method.mock.call_args
            correct = ((len(args) > 0 and args[0]== "Publisher") or
                       ("by" in kwargs and kwargs["by"] == "Publisher"))
            self.assertTrue(correct, msg="Wrong or missing argument to groupby method!")
        
if __name__ == '__main__':
    unittest.main()
    
