#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd
from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.cycling_weather"
cycling_weather = load(module_name, "cycling_weather")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p05-02.1')
class CyclingWeather(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = cycling_weather()
        
    def setUp(self):
        self.df = cycling_weather()
        
    def test_shape(self):
        self.assertEqual(self.df.shape, (8760, 28),
                         msg="Incorrect shape returned by cycling_weather function!")

    def test_column_names(self):
        cols=['Year', 'Precipitation amount (mm)', 'Snow depth (cm)',
        'Air temperature (degC)', 'Weekday', 'Day', 'Month', 'Hour',
        'Auroransilta', 'Eteläesplanadi', 'Huopalahti (asema)',
        'Kaisaniemi/Eläintarhanlahti', 'Kaivokatu', 'Kulosaaren silta et.',
        'Kulosaaren silta po. ', 'Kuusisaarentie', 'Käpylä, Pohjoisbaana',
        'Lauttasaaren silta eteläpuoli', 'Merikannontie',
        'Munkkiniemen silta eteläpuoli', 'Munkkiniemi silta pohjoispuoli',
        'Heperian puisto/Ooppera', 'Pitkäsilta itäpuoli',
        'Pitkäsilta länsipuoli', 'Lauttasaaren silta pohjoispuoli',
        'Ratapihantie', 'Viikintie', 'Baana']
        self.assertCountEqual(self.df.columns, cols, msg="Incorrect column names!")

    def test_calls(self):
        with patch(ph("cycling_weather"), wraps=cycling_weather) as pcw,\
            patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
            patch(ph("pd.merge"), wraps=pd.merge) as pmerge:
            main()
            pcw.assert_called_once()
            pmerge.assert_called_once()
            self.assertEqual(prc.call_count, 2,
                             msg="You should have called pd.read_csv exactly twice")
            
if __name__ == '__main__':
    unittest.main()
    
