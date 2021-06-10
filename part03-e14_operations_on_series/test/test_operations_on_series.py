#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.operations_on_series"
create_series = load(module_name, "create_series")
modify_series = load(module_name, "modify_series")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p03-14.1')
class OperationsOnSeries(unittest.TestCase):

    
    def test_creation(self):
        self.assertEqual("", "")
        L1=[2,3,4]
        L2=[9,8,7]
        indices=list("abc")
#        with patch(patch_name(module_name, "pd.core.series.Series"), wraps=pd.core.series.Series) as ps:
        with patch(ph("pd.Series"), wraps=pd.Series) as ps:
            ret = create_series(L1, L2)
            self.assertEqual(len(ret), 2, msg="Expected a pair of Series as a return value from function create_series!")
            s1, s2 = ret
            #ps.assert_called()
            self.assertEqual(ps.call_count, 2, msg="Expected the constructor pd.Series to be called exactly twice!")
        np.testing.assert_array_equal(s1.values, L1,
                                      err_msg="Expected values of first series to be %s" % L1)
        np.testing.assert_array_equal(s2.values, L2,
                                      err_msg="Expected values of second series to be %s" % L2)
        np.testing.assert_array_equal(s1.index, indices,
                                      err_msg="Expected the index of first series to be %s" % indices)
        np.testing.assert_array_equal(s2.index, indices,
                                      err_msg="Expected the index of second series to be %s" % indices)



    def test_modification(self):
        indices=list("abc")
        s1 = pd.Series([0,1,2], index=indices)
        s2 = pd.Series([3,4,5], index=indices)
        ret = modify_series(s1, s2)
        self.assertEqual(len(ret), 2, msg="Expected modify_series to return a pair of Series!")
        t1, t2 = ret
        self.assertIsInstance(t1, pd.Series, msg="Expected modify_series to return a pair of Series!")
        self.assertIsInstance(t2, pd.Series, msg="Expected modify_series to return a pair of Series!")
        t1_ind=list("abcd")
        t2_ind=list("ac")
        np.testing.assert_array_equal(t1.index, t1_ind,
                                      err_msg="Expected the index of first series to be %s!" % t1_ind)
        np.testing.assert_array_equal(t2.index, t2_ind,
                                      err_msg="Expected the index of second series to be %s!" % t2_ind)
        
        np.testing.assert_array_equal(t1.values, [0,1,2,4],
                                      err_msg="Values of first series is not correct!")
        np.testing.assert_array_equal(t2.values, [3, 5],
                                      err_msg="Values of second series is not correct!")

    def test_main(self):
        with patch(ph("create_series"), wraps=create_series) as pcs,\
             patch(ph("pd.Series.__add__"), side_effect=[pd.Series()]) as padd,\
             patch(ph("modify_series"), wraps=modify_series) as pms:
            main()
            pcs.assert_called()
            pms.assert_called()
            padd.assert_called()
            
if __name__ == '__main__':
    unittest.main()
    
