#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.multiplication_table_revisited"
multiplication_table = load(module_name, "multiplication_table")

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


@points('p02-16.1')
class MultiplicationTableRevisited(unittest.TestCase):


    def test_content(self):
        for n in range(1,10):
            a = multiplication_table(n)
            self.assertEqual(a.shape, (n,n), msg="Incorrect shape!")
            for (i,j), x in np.ndenumerate(a):
                self.assertEqual(i*j, x, msg="Incorrect value at pos (%i,%i)!" %(i,j))

    def test_calls(self):
        with patch(patch_name(module_name, "np.arange"), wraps=np.arange) as parange:
            a = multiplication_table(4)
            parange.assert_called()


if __name__ == '__main__':
    unittest.main()

