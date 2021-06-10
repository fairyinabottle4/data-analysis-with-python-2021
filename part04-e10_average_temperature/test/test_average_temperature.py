#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd
import re
import os

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.average_temperature"
average_temperature = load(module_name, "average_temperature")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-10.1')
class Average_temperature(unittest.TestCase):

    
    def test_value(self):
        ret_val = average_temperature()
        self.assertAlmostEqual(ret_val, 16.035483870967745, places=4,
                               msg="Incorrect average temperature")

    def test_output(self):
        main()
        out = get_stdout()
        pattern = r"Average temperature in July:\s+\d+.\d"
        self.assertRegex(out, pattern, msg="Output is not in correct form!")
                     
    def test_called(self):
        with patch(ph("average_temperature"), wraps=average_temperature) as pat,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            pat.assert_called_once()
            prc.assert_called_once()
            args, kwargs = prc.call_args
            self.assertEqual(os.path.basename(args[0]),
                             "kumpula-weather-2017.csv", msg="Wrong filename given to read_csv!")
            if "sep" in kwargs:
                self.assertEqual(kwargs["sep"], ",", msg="Incorrect separator in call to read_csv!")

if __name__ == '__main__':
    unittest.main()
    
