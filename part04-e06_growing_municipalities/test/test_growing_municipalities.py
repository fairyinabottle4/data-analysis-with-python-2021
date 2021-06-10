#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd
import re

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.growing_municipalities"
growing_municipalities = load(module_name, "growing_municipalities")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p04-06.1')
class GrowingMunicipalities(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = pd.read_csv(get_path("municipal.tsv"),
    #                           index_col=0, sep="\t")
    #     cls.df = cls.df["Akaa":"Äänekoski"]
    #     cls.c = "Population change from the previous year, %"

    def setUp(self):
        self.df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
        self.df = self.df["Akaa":"Äänekoski"]
        self.c = "Population change from the previous year, %"

    def test_all(self):
        result = growing_municipalities(self.df)
        self.assertAlmostEqual(result, 0.228296, places=4,
                               msg="Incorrect proportion for full data set!")
        
    def test_growing(self):
        m=self.df[self.c] > 0.0
        result = growing_municipalities(self.df[m])
        self.assertAlmostEqual(result, 1.0, places=4,
                               msg="Incorrect proportion for growing municipalities data set!")

    def test_not_growing(self):
        m=self.df[self.c] <= 0.0
        result = growing_municipalities(self.df[m])
        self.assertAlmostEqual(result, 0.0, places=4,
                               msg="Incorrect proportion for non-growing municipalities data set!")

    def test_call(self):
        with patch(ph("growing_municipalities"), wraps=growing_municipalities) as pgm:
            main()
            pgm.assert_called()
            
    def test_output(self):
        main()
        out = get_stdout()
        pattern = r"Proportion of growing municipalities: \d+\.\d%"
        self.assertRegex(out, pattern, msg="Output '%s' was not in correct form!" % out)

            
if __name__ == '__main__':
    unittest.main()
    
