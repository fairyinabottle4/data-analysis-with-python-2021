#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.municipalities_of_finland"
municipalities_of_finland = load(module_name, "municipalities_of_finland")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-04.1')
class MunicipalitiesOfFinland(unittest.TestCase):

    
    def test_shape(self):
        df = municipalities_of_finland()
        self.assertEqual(df.shape, (311,6), msg="The DataFrame had incorrect shape!")

    def test_called(self):
        with patch(ph("municipalities_of_finland"),
                   wraps=municipalities_of_finland) as pm:
            main()
            pm.assert_called()
        with patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc:
            df = municipalities_of_finland()
            prc.assert_called()

    def test_content(self):
        df = municipalities_of_finland()
        self.assertEqual(df.index[0], "Akaa", msg="Incorrect first index!")
        self.assertEqual(df.index[-1], "Äänekoski", msg="Incorrect last index!")
        self.assertEqual(df.iloc[0,0], 16769, msg="Element in the top left corner was incorrect!")
        self.assertEqual(df.iloc[-1,-1], 30.5, msg="Element in the bottom right corner was incorrect!")

if __name__ == '__main__':
    unittest.main()
    
