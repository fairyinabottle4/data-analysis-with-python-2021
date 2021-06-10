#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.correlation"
correlations = load(module_name, "correlations")
lengths = load(module_name, "lengths")

def patch_name(m, d):
    import importlib
    parts=d.split(".")
    try:
        getattr(importlib.import_module(m), parts[-1])
        p=".".join([m, parts[-1]])
    except ModuleNotFoundError:
        raise
    except AttributeError:
        if len(parts) == 1:
            raise
        try:
            getattr(importlib.import_module(m), parts[-2])
            p=".".join([m] + parts[-2:])
        except AttributeError:
            if len(parts) == 2:
                raise
            getattr(importlib.import_module(m), parts[-3])
            p=".".join([m] + parts[-3:])
    return p


class Correlation(unittest.TestCase):


    @points('p03-05.1')
    def test_lengths(self):
        result = lengths()
        self.assertAlmostEqual(result, 0.8717537758865832, places=4, msg="Wrong correlation!")

    @points('p03-05.1')
    def test_lengths_calls(self):
        with patch(patch_name(module_name, "scipy.stats.pearsonr")) as pcorr:
            result = lengths()
            pcorr.assert_called()


    @points('p03-05.2')
    def test_correlations(self):
        result = correlations()
        n, m = result.shape
        for r in range(n):
            for c in range(r):
                self.assertAlmostEqual(result[r,c], result[c,r], places=4,
                                       msg="The correlation matrix is not symmetric!")
            self.assertAlmostEqual(result[r,r], 1, places=4, msg="Values on the diagonal should be one!")

        self.assertAlmostEqual(result[0,1], -0.11756978, places=4,
                               msg="Incorrect value in position [0,1]!")
        self.assertAlmostEqual(result[0,2], 0.87175378, places=4,
                               msg="Incorrect value in position [0,2]!")
        self.assertAlmostEqual(result[0,3], 0.81794113, places=4,
                               msg="Incorrect value in position [0,3]!")
        self.assertAlmostEqual(result[1,2], -0.4284401, places=4,
                               msg="Incorrect value in position [1,2]!")
        self.assertAlmostEqual(result[1,3], -0.36612593, places=4,
                               msg="Incorrect value in position [1,3]!")
        self.assertAlmostEqual(result[2,3], 0.96286543, places=4,
                               msg="Incorrect value in position [2,3]!")

    @points('p03-05.2')
    def test_lengths_calls(self):
        with patch(patch_name(module_name, "np.corrcoef")) as pcorr:
            result = correlations()
            pcorr.assert_called()

if __name__ == '__main__':
    unittest.main()

