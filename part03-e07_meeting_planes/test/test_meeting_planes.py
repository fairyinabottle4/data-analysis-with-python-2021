#!/usr/bin/python3

import unittest
from unittest.mock import patch

import numpy as np
from numpy.linalg.linalg import LinAlgError

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name = 'src.meeting_planes'
meeting_planes = load(module_name, 'meeting_planes')
ph = patch_helper(module_name)

@points('p03-07.1')
class MeetingPlanes(unittest.TestCase):

    
    def test_first(self):
        a1=1
        b1=4
        c1=5
        
        a2=3
        b2=2
        c2=1
        
        a3=2
        b3=4
        c3=1
        p=(a1,b1,c1,
           a2,b2,c2,
           a3,b3,c3)
        system="(a1=%i, b1=%i, c1=%i, a2=%i, b2=%i, c2=%i, a3=%i, b3=%i, c3=%i)" % p
        
        x, y, z = meeting_planes(a1, b1, c1,
                                 a2, b2, c2,
                                 a3, b3, c3)
        
        self.assertAlmostEqual(z, a1*y + b1*x+c1, msg="Solution %f does not satisfy the first equation of system %s!" % (z, system))
        self.assertAlmostEqual(z, a2*y + b2*x+c2, msg="Solution %f does not satisfy the second equation of system %s!" % (z, system))
        self.assertAlmostEqual(z, a3*y + b3*x+c3, msg="Solution %f does not satisfy the third equation of system %s!" % (z, system))

    def test_calls(self):
        a1=1
        b1=4
        c1=5
        
        a2=3
        b2=2
        c2=1
        
        a3=2
        b3=4
        c3=1

        with patch(ph("np.linalg.solve"), wraps=np.linalg.solve) as psolve:
            meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
            psolve.assert_called_once()
            
    def test_underdetermined(self):
        a1=1
        b1=4
        c1=2
        p=(a1,b1,c1,
           a1,b1,c1,
           a1,b1,c1)
        system="(a1=%i, b1=%i, c1=%i, a2=%i, b2=%i, c2=%i, a3=%i, b3=%i, c3=%i)" % p
        with self.assertRaises(np.linalg.linalg.LinAlgError,
                               msg="Under determined system %s should raise an exception!" % system):
            meeting_planes(*p)


    def test_inconsistent(self):
        a1=1
        b1=4
        c1=2
        p=(a1,b1,c1,
           a1,b1,c1,
           a1,b1,c1+1)
        system="(a1=%i, b1=%i, c1=%i, a2=%i, b2=%i, c2=%i, a3=%i, b3=%i, c3=%i)" % p
        with self.assertRaises(np.linalg.linalg.LinAlgError,
                               msg="Inconsistent system %s should raise an exception!" % system):
            meeting_planes(*p)



if __name__ == '__main__':
    unittest.main()
    
