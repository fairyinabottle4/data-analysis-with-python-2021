#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.multiple_graphs"
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p03-09.1')
class MultipleGraphs(unittest.TestCase):

    
    def test_first(self):
        with patch(ph("plt.show")) as pshow,\
             patch(ph("plt.plot")) as pplot,\
             patch(ph("plt.xlabel")) as pxlabel,\
             patch(ph("plt.ylabel")) as pylabel:
            main()
            pshow.assert_called_once()
            pxlabel.assert_called_once()
            pylabel.assert_called_once()
            self.assertGreater(pplot.call_count, 0, msg="You should have called plt.plot!")
            self.assertLess(pplot.call_count, 3, msg="You should have called plt.plot at most two times!")
            if pplot.call_count == 2:
                np.testing.assert_array_equal(pplot.call_args_list[0][0][0], [2,4,6,7], err_msg="Wrong parameters to plot!")
                np.testing.assert_array_equal(pplot.call_args_list[0][0][1], [4,3,5,1], err_msg="Wrong parameters to plot!")
                np.testing.assert_array_equal(pplot.call_args_list[1][0][0], [1,2,3,4], err_msg="Wrong parameters to plot!")
                np.testing.assert_array_equal(pplot.call_args_list[1][0][1], [4,2,3,1], err_msg="Wrong parameters to plot!")
            else:
                np.testing.assert_array_equal(pplot.call_args_list[0][0], ([2,4,6,7], [4,3,5,1], [1,2,3,4], [4,2,3,1]),
                                              err_msg="Parameters to the plt.plot command were wrong")


if __name__ == '__main__':
    unittest.main()
    
