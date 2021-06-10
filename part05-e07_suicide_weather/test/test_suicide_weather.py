#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.suicide_weather"
suicide_weather = load(module_name, "suicide_weather")
suicide_fractions = load(module_name, "suicide_fractions")
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p05-07.1')
class SuicideWeather(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.tup = suicide_weather()

    def setUp(self):
        self.tup = suicide_weather()

    def test_return_value(self):
        suicide_n, temperature_n, common_n, corr = self.tup
        self.assertEqual(suicide_n, 141, msg="Incorrect size of suicide Series!")
        self.assertEqual(temperature_n, 191, msg="Incorrect size of temperature Series!")
        self.assertEqual(common_n, 108, msg="Incorrect size of common Series!")
        self.assertAlmostEqual(corr, -0.5580402318136322, places=4,
                               msg="Incorrect Spearman correlation!")

    def test_calls(self):
        method = spy_decorator(pd.core.series.Series.corr, "corr")
        f_method = spy_decorator(pd.core.frame.DataFrame.corr, "corr")
        with patch(ph("suicide_fractions"), wraps=suicide_fractions) as psf,\
             patch(ph("pd.read_html"), wraps=pd.read_html) as phtml,\
             patch.object(pd.core.series.Series, "corr", new=method),\
             patch.object(pd.core.frame.DataFrame, "corr", new=f_method),\
             patch(ph("suicide_weather"), wraps=suicide_weather) as psw:
            main()
            psf.assert_called_once()
            psw.assert_called_once()
            phtml.assert_called_once()
            if not f_method.mock.called:
                method.mock.assert_called()
                args, kwargs = method.mock.call_args
            else:
                args, kwargs = f_method.mock.call_args
            correct = ((len(args) > 1 and args[1]== "spearman") or
                       ("method" in kwargs and kwargs["method"] == "spearman"))
            self.assertTrue(correct, msg="You did not compute Spearman correlation!")

        out = get_stdout()
        self.assertRegex(out, r"Suicide DataFrame has \d+ rows",
                         msg="Output line about Suicide was incorrect!")
        self.assertRegex(out, r"Temperature DataFrame has \d+ rows",
                         msg="Output line about Temperature was incorrect!")
        self.assertRegex(out, r"Common DataFrame has \d+ rows",
                         msg="Output line about Common was incorrect!")
        self.assertRegex(out, r"Spearman correlation:\s+[+-]?\d+\.\d+",
                         msg="Output line about correlation was incorrect!")

if __name__ == '__main__':
    unittest.main()

