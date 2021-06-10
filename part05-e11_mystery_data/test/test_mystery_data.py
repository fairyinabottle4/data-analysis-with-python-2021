#!/usr/bin/python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name='src.mystery_data'
mystery_data = load(module_name, 'mystery_data')
ph = patch_helper(module_name)

@points('p05-11.1')
class MysteryData(unittest.TestCase):

    
    def test_result(self):
        coefficients = mystery_data()
        self.assertAlmostEqual(-11, sum(coefficients), msg="Incorrect sum of coefficients!")

    def test_calls(self):
        with patch(ph("sklearn.linear_model.LinearRegression")) as linreg:
            coefficients = mystery_data()
            if len(linreg.call_args[0]) > 0:
                self.assertFalse(linreg.call_args[0][0], msg="Do not fit the intercept")
            else:
                linreg.assert_called_once_with(fit_intercept=False)
            a, b = linreg().fit.call_args[0]
            shape = (1000, 5)
            self.assertEqual(a.shape, shape,
                             msg="Incorrect parameters to LinearRegression, wrong shape!")
            self.assertEqual(len(b), 1000,
                             msg="Incorrect parameters to LinearRegression, wrong shape!")


if __name__ == '__main__':
    unittest.main()
    
