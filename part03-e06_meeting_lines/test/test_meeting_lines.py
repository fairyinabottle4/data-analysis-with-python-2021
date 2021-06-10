#!/usr/bin/python3

import unittest
from unittest.mock import patch

import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper
module_name='src.meeting_lines'
meeting_lines = load(module_name, 'meeting_lines')
ph = patch_helper(module_name)

@points('p03-06.1')
class MeetingLines(unittest.TestCase):


    def test_first(self):
        a1=1
        b1=4
        a2=3
        b2=2
        x, y = meeting_lines(a1,b1,a2,b2)

        self.assertAlmostEqual(y, a1*x + b1, msg="Meeting point in not on line a1=%i, b1=%i" % (a1,b1))
        self.assertAlmostEqual(y, a2*x + b2, msg="Meeting point in not on line a2=%i, b2=%i" % (a2,b2))

    def test_calls(self):
        with patch(ph("np.linalg.solve"), wraps=np.linalg.solve) as psolve:
            a1=1
            b1=4
            a2=3
            b2=2
            meeting_lines(a1,b1,a2,b2)
            psolve.assert_called()

    def test_underdetermined(self):
        a1=1
        b1=4
        p=(a1,b1,a1,b1)
        system="(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        with self.assertRaises(np.linalg.linalg.LinAlgError,
                               msg="Under determined system %s should raise an exception!" % system):
            meeting_lines(*p)

    def test_inconsistent(self):
        a1=1
        b1=4
        p=(a1,b1,a1,b1)
        system="(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        with self.assertRaises(np.linalg.linalg.LinAlgError,
                               msg="Inconsistent system %s should raise an exception!" % system):
             meeting_lines(*p)

if __name__ == '__main__':
    unittest.main()

