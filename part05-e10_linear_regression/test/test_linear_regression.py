#!/usr/bin/python3

import unittest
from unittest.mock import patch


import numpy as np
import sys
import sklearn
import sklearn.linear_model
from tmc import points

from tmc.utils import load, get_stdout, patch_helper
module_name='src.linear_regression'
fit_line = load(module_name, 'fit_line')
main = load(module_name, 'main')
ph = patch_helper(module_name)

class LinearRegression(unittest.TestCase):

    
    @points('p05-10.1')
    def test_first(self):
        x=np.array([1,2,3])
        y=np.array([1,2.5,3])+1
        slope, intercept = fit_line(x, y)
        self.assertIsInstance(slope, float, msg="Expected slope to have type float!")
        self.assertAlmostEqual(slope, 1.0, places=4, msg="Incorrect slope!")
        self.assertAlmostEqual(intercept, 1.16666666667, places=4, msg="Incorrect intercept!")

    @points('p05-10.1')
    def test_output(self):
        with patch(ph("plt.show")) as pshow:
            main()
            output = get_stdout()
            pattern1 = r"Slope:\s+(.*)"
            self.assertRegex(output, pattern1, msg="Slope was not printed!")
            pattern2 = r"Intercept:\s+(.*)"
            self.assertRegex(output, pattern2, msg="Intercept was not printed!")
        
    @points('p05-10.2')
    def test_plot(self):
        with patch(ph("plt.show")) as pshow,\
             patch(ph("plt.scatter")) as pscatter,\
             patch(ph("plt.plot")) as pplot:
            main()
            pshow.assert_called_once()
            self.assertEqual(pplot.call_count + pscatter.call_count, 2,
                             msg="Expected exactly two calls to plotting functions (plot or scatter)!")
            #pplot.assert_called()
        
    @points('p05-10.1')
    def test_calls(self):
        x=np.array([1,2,3])
        y=np.array([1,2.5,3])+1
        with patch(ph('sklearn.linear_model.LinearRegression')) as linreg:
            slope, intercept = fit_line(x, y)
            linreg.assert_called_once()
            a, b = linreg().fit.call_args[0]
            shape = (len(x), 1)
            self.assertEqual(a.shape, shape, msg="Incorrect shape of parameter to fit method!")
            self.assertEqual(len(b), len(y), msg="Incorrect shape of parameter to fit method!")

            
if __name__ == '__main__':
    unittest.main()
    
