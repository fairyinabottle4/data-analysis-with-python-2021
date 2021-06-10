#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.swedish_and_foreigners"
swedish_and_foreigners = load(module_name, "swedish_and_foreigners")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-05.1')
class SwedishAndForeigners(unittest.TestCase):

    
    def test_shape(self):
        df = swedish_and_foreigners()
        self.assertEqual(df.shape, (28,3), msg="Incorrect shape!")

    def test_columns(self):
        df = swedish_and_foreigners()
        np.testing.assert_array_equal(df.columns,
                                      ["Population","Share of Swedish-speakers of the population, %",
                                       "Share of foreign citizens of the population, %"],
                         err_msg="Incorrect column names!")
    
    def test_index(self):
        df = swedish_and_foreigners()
        self.assertEqual(df.index[0], "Brändö", msg="Incorrect first index!")
        self.assertEqual(df.index[-1], "Vöyri", msg="Incorrect last index!")

    def test_content(self):
        df = swedish_and_foreigners()
        values=[452, 89.7, 10.5]
        for i in range(3):
            self.assertEqual(df.iloc[i,i], values[i],
                             msg="Value on row '%s' column '%s' is not correct!" % (
                                 df.index[i], df.columns[i]))

    def test_called(self):
        with patch(ph("swedish_and_foreigners"), wraps=swedish_and_foreigners) as psaf:
            main()
            psaf.assert_called()

if __name__ == '__main__':
    unittest.main()
    
