#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.split_date"
split_date = load(module_name, "split_date")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-16.1')
class SplitDate(unittest.TestCase):

#    @classmethod
#    def setUpClass(cls):
#        cls.df = split_date()
        
    def setUp(self):
        self.df = split_date()
        
    def test_shape(self):
        self.assertEqual(self.df.shape, (37128, 5),
                         msg="The DataFrame has incorrect shape!")

    def test_columns(self):
        np.testing.assert_array_equal(self.df.columns,
                                      ["Weekday", "Day", "Month", "Year", "Hour"],
                                      err_msg="Incorrect column names!")

    def test_dtypes(self):
        correct_types = [object, np.integer, np.integer, np.integer, np.integer]
        for i, (result, correct) in enumerate(zip(self.df.dtypes, correct_types)):
            self.assertTrue(np.issubdtype(result, correct),
                            msg="Types don't match on column %i! Expected %s got %s." % (i, correct, result))
        # np.testing.assert_array_equal(self.df.dtypes,
        #                               [object, int, np.integer, int, int], err_msg="Incorrect column types")
        
    def test_called(self):
        with patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
             patch(ph("split_date"), wraps=split_date) as psd:
            main()
            psd.assert_called()

    def test_content(self):
        weekdays = "Mon Tue Wed Thu Fri Sat Sun".split()
        for elem in self.df["Weekday"]:
            self.assertIn(elem, weekdays, msg="Incorrect value '%s' in column Weekday!" % elem)

        for index in self.df.index:
            weekday, day, month, year, hour = self.df.loc[index]
            self.assertIn(weekday, weekdays, msg="Incorrect value '%s' in column Weekday!" % weekday)
            self.assertIn(day, range(1,32), msg="Incorrect value '%s' in column Day!" % day)
            self.assertIn(month, range(1,13), msg="Incorrect value '%s' in column Month!" % month)
            self.assertIn(year, range(2014,2019), msg="Incorrect value '%s' in column Year!" % year)
            self.assertIn(hour, range(0,24), msg="Incorrect value '%s' in column Hour!" % hour)

if __name__ == '__main__':
    unittest.main()
    
