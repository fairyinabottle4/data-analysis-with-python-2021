#!/usr/bin/env python3

import unittest
from unittest.mock import patch, call, MagicMock
import numpy as np
import pandas as pd
import sklearn
from tmc import points
import re

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.cycling_weather_continues"
cycling_weather_continues = load(module_name, "cycling_weather_continues")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-13.1')
class CyclingWeatherContinues(unittest.TestCase):

    def test_return_type(self):
        self.coef, self.score = cycling_weather_continues("Merikannontie")
        self.assertIsInstance(self.coef, (list, tuple, np.ndarray),
                              msg="Expected coeeffients to be a list, tuple or an array!")
        self.assertIsInstance(self.score, float, msg="Expected the score to be a float!")

        self.assertAlmostEqual(self.score, 0.66, places=2, msg="Incorrect score for station 'Merikannontie'!")
        self.assertAlmostEqual(self.coef[0], -58.2, places=1,
                               msg="Incorrect regression coefficient for precipitation!")
        self.assertAlmostEqual(self.coef[1], -15.8, places=1,
                               msg="Incorrect regression coefficient for precipitation!")
        self.assertAlmostEqual(self.coef[2], 145.6, places=1,
                               msg="Incorrect regression coefficient for precipitation!")

        
    def test_output(self):
        main()
        output = get_stdout()
        #m = re.match(r"Measuring station: *(.*)", output)
        self.assertRegex(output, r"(?m)Measuring station: *(.+)$",
                         msg="No information about the measuring station in output!")
        self.assertRegex(output, r"(?m)Regression coefficient for variable 'precipitation': [-+]?\d+\.\d$",
                         msg="Incorrect output for variable precipitation!")
        self.assertRegex(output, r"(?m)Regression coefficient for variable 'snow depth': [-+]?\d+\.\d$",
                         msg="Incorrect output for variable snowdepth!")
        self.assertRegex(output, r"(?m)Regression coefficient for variable 'temperature': [-+]?\d+\.\d$",
                         msg="Incorrect output temperature!")

        self.assertRegex(output, r"(?m)Score: [-+]?\d+\.\d\d$",
                         msg="Incorrect output about score!")

    def test_calls(self):
        merge_method = spy_decorator(pd.core.frame.DataFrame.merge, "merge")
        with patch(ph("cycling_weather_continues"), wraps=cycling_weather_continues) as pcw,\
             patch(ph("sklearn.linear_model.LinearRegression"), wraps=sklearn.linear_model.LinearRegression) as lr, \
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
             patch.object(pd.core.frame.DataFrame, "merge", new=merge_method),\
             patch(ph("pd.merge"), wraps=pd.merge) as pmerge:
            main()
            pcw.assert_called_once()
            lr.assert_called_once()
            print(type(lr))
            if "fit_intercept" in lr.call_args[1]:
                self.assertTrue(lr.call_args[1]["fit_intercept"], msg="You did not fit the intercept!")
            elif len(lr.call_args[0]) > 0:
                self.assertTrue(lr.call_args[0][0], msg="You did not fit the intercept!")
            merge_method_called = merge_method.mock.call_count >= 1
            merge_func_called = pmerge.call_count >= 1
            self.assertTrue(merge_method_called or merge_func_called, msg="You did not call merge method or function!")
            self.assertEqual(prc.call_count, 2, msg="You should have called pd.read_csv exactly twice")

    
if __name__ == '__main__':
    unittest.main()
    
