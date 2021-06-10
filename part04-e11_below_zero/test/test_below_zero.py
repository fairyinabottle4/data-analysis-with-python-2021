#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd
import re
import os

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.below_zero"
below_zero = load(module_name, "below_zero")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-11.1')
class BelowZero(unittest.TestCase):

    def test_value(self):
        ret_val = below_zero()
        self.assertEqual(ret_val, 49, msg="Incorrect return value!")

    def test_output(self):
        main()
        out = get_stdout()
        pattern = r"Number of days below zero:\s+\d+"
        self.assertRegex(out, pattern, msg="Output is not in correct form!")

    def test_called(self):
        with patch(ph("below_zero"), wraps=below_zero) as pbz,\
            patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            pbz.assert_called_once()
            prc.assert_called_once()
            args, kwargs = prc.call_args
            self.assertEqual(os.path.basename(args[0]),
                             "kumpula-weather-2017.csv", msg="Wrong filename given to read_csv!")
            if "sep" in kwargs:
                self.assertEqual(kwargs["sep"], ",", msg="Incorrect separator in call to read_csv!")


if __name__ == '__main__':
    unittest.main()
    
