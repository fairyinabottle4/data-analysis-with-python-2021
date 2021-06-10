#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np


from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.bicycle_timeseries"
bicycle_timeseries = load(module_name, "bicycle_timeseries")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-08.1')
class BicycleTimeseries(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = bicycle_timeseries()

    def setUp(self):
        self.df = bicycle_timeseries()
        
    def test_shape(self):
        self.assertEqual(self.df.shape, (37128, 20), msg="Incorrect shape!")

    def test_columns(self):
        cols = ['Auroransilta', 'Eteläesplanadi', 'Huopalahti (asema)',
                'Kaisaniemi/Eläintarhanlahti', 'Kaivokatu', 'Kulosaaren silta et.',
                'Kulosaaren silta po. ', 'Kuusisaarentie', 'Käpylä, Pohjoisbaana',
                'Lauttasaaren silta eteläpuoli', 'Merikannontie',
                'Munkkiniemen silta eteläpuoli', 'Munkkiniemi silta pohjoispuoli',
                'Heperian puisto/Ooppera', 'Pitkäsilta itäpuoli',
                'Pitkäsilta länsipuoli', 'Lauttasaaren silta pohjoispuoli',
                'Ratapihantie', 'Viikintie', 'Baana']
        np.testing.assert_array_equal(self.df.columns, cols, err_msg="Incorrect columns!")

    def test_index(self):
        self.assertIsInstance(self.df.index[0], pd.Timestamp,
                              msg="Expected index to have type timestamp!")
        self.assertEqual(self.df.index[0], pd.to_datetime("2014-1-1 00:00"),
                         msg="Incorrect first index!")
        
        self.assertEqual(self.df.index[1], pd.to_datetime("2014-1-1 01:00"),
                         msg="Incorrect second index!")

    def test_calls(self):
        with patch(ph("bicycle_timeseries"), wraps=bicycle_timeseries) as pbts,\
             patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
             patch(ph("pd.to_datetime"), wraps=pd.to_datetime) as pdatetime:
            main()
            pbts.assert_called_once()
            prc.assert_called_once()
            pdatetime.assert_called()
   
if __name__ == '__main__':
    unittest.main()
    
