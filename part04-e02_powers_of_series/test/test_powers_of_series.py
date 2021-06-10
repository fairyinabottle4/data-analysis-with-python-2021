#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.powers_of_series"
powers_of_series = load(module_name, "powers_of_series")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p04-02.1')
class PowersOfSeries(unittest.TestCase):

    def test_type(self):
        s = pd.Series([1,2,3,4], index=list("abcd"))
        k = 2
        df = powers_of_series(s, k)
        self.assertIsInstance(df, pd.DataFrame, msg="powers_of_series should return a DataFrame!")
    
    def test_dimensions(self):
        ind=list("abcdefghijklmnopqrstuvwxyz")
        k=3
        for n in range(4):
            L=np.random.randint(-10, 10, n)
            s = pd.Series(L, index=ind[:n])
            df = powers_of_series(s, k)
            self.assertEqual(df.shape, (n, k),
                             msg="The DataFrame had wrong shape for call powers_of_series(%s, %i)!" % (s,k))
 
    def test_content(self):
        ind=list("abcdefghijklmnopqrstuvwxyz")
        k=3
        for n in range(4, 0, -1):
            L=np.random.randint(-10, 10, n)
            s = pd.Series(L, index=ind[:n])
            df = powers_of_series(s, k)
            self.assertTrue(np.issubdtype(df.columns.dtype, np.integer),
                            msg="Expected column indices to have integer type!")
            for i in range(1,k+1):
                np.testing.assert_array_equal(df[i], s**i, err_msg="Incorrect values in column %i for Series\n%s!" % ( i, s))

    def test_called(self):
        with patch(ph("powers_of_series"), wraps=powers_of_series) as ppos:
            main()
            ppos.assert_called()

if __name__ == '__main__':
    unittest.main()
    
