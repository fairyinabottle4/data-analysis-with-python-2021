#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.commute"
commute = load(module_name, "commute")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-09.1')
class Commute(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = commute()

    def setUp(self):
        self.df = commute()
        
    def test_shape(self):
        self.assertEqual(self.df.shape, (7,20), msg="Incorrect shape!")

    def test_index(self):
        weekdays = "mon tue wed thu fri sat sun".title().split()
        numbers=list(range(1,8))
        a = np.all(self.df.index == weekdays)
        b = np.all(self.df.index == numbers)
        self.assertTrue(a or b,
                        msg="Incorrect index! Expected either %s or %s" % (numbers, weekdays))

    def test_content(self):
        self.assertEqual(self.df.values.sum(), 1264606.0, msg="Sum of all elements was incorrect!")

        
    def test_calls(self):
        method = spy_decorator(pd.core.frame.DataFrame.groupby, "groupby")
        with patch(ph("commute"), wraps=commute) as pcommute,\
             patch.object(pd.core.frame.DataFrame, "groupby", new=method),\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
             patch(ph("plt.show")) as pshow,\
             patch(ph("pd.to_datetime"), wraps=pd.to_datetime) as pdatetime:
            main()
            pcommute.assert_called_once()
            prc.assert_called_once()
            pshow.assert_called_once()
            pdatetime.assert_called()
            method.mock.assert_called()
            
if __name__ == '__main__':
    unittest.main()
    
