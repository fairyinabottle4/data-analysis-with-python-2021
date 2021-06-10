#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.top_bands"
top_bands = load(module_name, "top_bands")
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p05-03.1')
class TopBands(unittest.TestCase):
    
    def test_shape(self):
        df = top_bands()
        self.assertEqual(df.shape, (9, 13), msg="Incorrect shape!")

    def test_columns(self):
        df = top_bands()
        cols = ['Pos', 'LW', 'Title', 'Artist', 'Publisher', 'Peak Pos', 'WoC', 'Band',
                'Singer', 'Lead guitar', 'Rhythm guitar', 'Bass', 'Drums']
        self.assertCountEqual(df.columns, cols, msg="Incorrect columns!")
                         
    def test_calls(self):
        merge_method = spy_decorator(pd.core.frame.DataFrame.merge, "merge")
        with patch(ph("top_bands"), wraps=top_bands) as ptop,\
            patch(ph("pd.read_csv"), wraps=pd.read_csv) as prc,\
            patch.object(pd.core.frame.DataFrame, "merge", new=merge_method),\
            patch(ph("pd.merge"), wraps=pd.merge) as pmerge:
            main()
            ptop.assert_called_once()
            self.assertEqual(prc.call_count, 2,
                             msg="You should have called pd.read_csv exactly twice")
            self.assertTrue(pmerge.call_count == 1 or merge_method.mock.call_count == 1, msg="Call merge exactly once!")
            
            if pmerge.call_count >= 1:
                args, kwargs = pmerge.call_args             # function called
            else:
                args, kwargs = merge_method.mock.call_args  # method called
                
            self.assertTrue("left_on" in kwargs,
                            msg="You should have used 'left_on' argument of pd.merge!")
            self.assertTrue("right_on" in kwargs,
                            msg="You should have used 'right_on' argument of pd.merge!")
            params = [kwargs["left_on"], kwargs["right_on"]]
            self.assertTrue(("Artist" in params or ["Artist"] in params) and
                            ("Band" in params or ["Band"] in params) ,
                            msg="You should have merged on 'Artist' and 'Band' columns!")

if __name__ == '__main__':
    unittest.main()
    
