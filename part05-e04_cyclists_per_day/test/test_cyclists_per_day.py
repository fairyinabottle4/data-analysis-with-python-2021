#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.cyclists_per_day"
cyclists_per_day = load(module_name, "cyclists_per_day")
main = load(module_name, "main")
ph = patch_helper(module_name)


class CyclistsPerDay(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = cyclists_per_day()

    def setUp(self):
        self.df = cyclists_per_day()
        
    @points('p05-04.1')
    def test_shape(self):
        self.assertEqual(self.df.shape, (1547, 20),
                         msg="cyclists_per_day returned DataFrame of wrong shape!")

#    def test_index(self):
#        self.assertCountEqual(self.df.index, range(1,32), msg="Incorrect index!")

    @points('p05-04.1')
    def test_columns(self):
        cols=['Auroransilta', 'Eteläesplanadi',
              'Huopalahti (asema)', 'Kaisaniemi/Eläintarhanlahti', 'Kaivokatu',
              'Kulosaaren silta et.', 'Kulosaaren silta po. ', 'Kuusisaarentie',
              'Käpylä, Pohjoisbaana', 'Lauttasaaren silta eteläpuoli',
              'Merikannontie', 'Munkkiniemen silta eteläpuoli',
              'Munkkiniemi silta pohjoispuoli', 'Heperian puisto/Ooppera',
              'Pitkäsilta itäpuoli', 'Pitkäsilta länsipuoli',
              'Lauttasaaren silta pohjoispuoli', 'Ratapihantie', 'Viikintie',
              'Baana']
        self.assertCountEqual(self.df.columns, cols, msg="Incorrect columns!")


    @points('p05-04.2')
    def test_calls(self):
        method = spy_decorator(pd.core.frame.DataFrame.plot, "plot")
        with patch(ph("cyclists_per_day"), wraps=cyclists_per_day) as pcpd,\
             patch.object(pd.core.frame.DataFrame, "plot", new=method),\
             patch(ph("plt.plot")) as pplot,\
             patch(ph("plt.show")) as pshow:
            main()
            pcpd.assert_called_once()
            func_called = pplot.call_count == 1
            method_called = method.mock.call_count == 1
            self.assertTrue(func_called or method_called,
                            msg="You must call either plt.plot or plot method of a DataFrame!")
            pshow.assert_called_once()
            
if __name__ == '__main__':
    unittest.main()
    
