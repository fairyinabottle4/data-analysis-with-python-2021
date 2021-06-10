#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import re
import pandas as pd
import os

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.snow_depth"
snow_depth = load(module_name, "snow_depth")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-09.1')
class SnowDepth(unittest.TestCase):

    
    def test_value(self):
        ret_val = snow_depth()
        self.assertEqual(ret_val, 15.0, msg="Incorrect return value!")

    def test_output(self):
        main()
        out = get_stdout()
        pattern = r"Max snow depth:\s+\d+.\d"
        self.assertRegex(out, pattern, msg="Output is not in correct form!")

    def test_called(self):
        with patch(ph("snow_depth"), wraps=snow_depth) as psd,\
            patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            main()
            psd.assert_called_once()
            prc.assert_called_once()
            args, kwargs = prc.call_args
            self.assertEqual(os.path.basename(args[0]),
                             "kumpula-weather-2017.csv", msg="Wrong filename was given to read_csv!")
            if "sep" in kwargs:
                self.assertEqual(kwargs["sep"], ",", msg="Incorrect separator in call to read_csv!")
            
if __name__ == '__main__':
    unittest.main()
    
