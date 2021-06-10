#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.diamond"
diamond = load(module_name, "diamond")

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

@points('p02-13.1')
class Diamond(unittest.TestCase):

    def test_type(self):
        d=diamond(3)
        self.assertEqual(d.dtype, int, msg="Incorrect element type!")

    def test_shape(self):
        for n in range(1,10):
            d=diamond(n)
            correct_shape=(2*n-1,)*2
            self.assertEqual(d.shape, correct_shape,
                             msg="Incorrect shape for call 'diamond(%i)'!" % n)

    def test_content(self):
        for n in range(1,10):
            d=diamond(n)
            if n==1:
                size=1
            else:
                size=4*n-4
            self.assertEqual(np.sum(d), size,
                             msg="Incorrect number of 1s for call 'diamond(%i)'!" % n)

    def test_calls(self):
        with patch(patch_name(module_name, 'np.eye'), wraps=np.eye) as peye:
            with patch(patch_name(module_name, 'np.concatenate'), wraps=np.concatenate) as pconcatenate:
                d=diamond(3)
                peye.assert_called()
                pconcatenate.assert_called()

if __name__ == '__main__':
    unittest.main()

