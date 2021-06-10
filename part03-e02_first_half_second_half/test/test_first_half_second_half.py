#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
from tmc import points

from tmc.utils import load, get_stdout

module_name="src.first_half_second_half"
first_half_second_half = load(module_name, "first_half_second_half")

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



@points('p03-02.1')
class FirstHalfSecondHalf(unittest.TestCase):


    def test_shape(self):
        n=10
        for m in range(2, 8):
            a = np.random.randn(n, 2*m)
            result = first_half_second_half(a)
            self.assertEqual(result.shape[1], 2*m,
                             msg="Incorrect number of columns for array %s!" % a)
            self.assertLessEqual(result.shape[0], n,
                                 msg="There cannot be more rows than in the input array %s!" % a)

    def test_simple(self):
        n=10
        a = np.random.randn(n, 2)
        result = first_half_second_half(a)
        correct = np.sum(a[:,0] > a[:,1])
        self.assertEqual(result.shape[1], 2, msg="Incorrect number of columns for random array %s" % a)
        self.assertEqual(result.shape[0], correct, msg="Wrong result for random array %s" % a)

    def test_content(self):
        n=10
        for m in range(2, 8):
            a = np.random.randn(n, 2*m)
            result = first_half_second_half(a)
            for row in result:
                self.assertGreater(np.sum(row[0:m]), np.sum(row[m:]),
                                   msg="Wrong result for array %s!" % a)

    def test_calls(self):
        n=10
        m=4
        a = np.random.randn(n, 2*m)
        with patch(patch_name(module_name, "np.sum"), side_effect=np.sum) as psum:
            result = first_half_second_half(a)
            self.assertEqual(psum.call_count, 2, msg="Expected exactly two calls to function np.sum!")

if __name__ == '__main__':
    unittest.main()
