#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.last_week"
last_week = load(module_name, "last_week")
ph = patch_helper(module_name)

            

class LastWeek(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.df = last_week()

    def setUp(self):
        self.df = last_week()

    @points('p04-15.1')
    def check_column(self, col, correct, nans, column_name):
        for row in range(1, 41):
            if row in nans:
                self.assertTrue(pd.isnull(col.iloc[row-1]),
                                msg="Expected a nan on row %i column %s!" % (row, column_name))
        np.testing.assert_array_equal(col[col.notnull()], correct,
                                      err_msg="Incorrect values in column %s!" % column_name)
        
    @points('p04-15.1')
    def test_base(self):
        self.assertEqual(len(self.df), 40, msg="Incorrect number of rows!")
        np.testing.assert_array_equal(self.df.Pos, range(1,41), err_msg="Incorrect Pos column!")

    @points('p04-15.1')
    def test_title(self):
        titles=np.array(['I WANT TO HOLD YOUR HAND', 'SHE LOVES YOU',
       'YOU WERE MADE FOR ME', 'SECRET LOVE',
       'I ONLY WANT TO BE WITH YOU', 'GLAD ALL OVER', 'DOMINIQUE',
       "DON'T TALK TO HIM", 'TWENTY FOUR HOURS FROM TULSA', 'MARIA ELENA',
       'GERONIMO', "YOU'LL NEVER WALK ALONE", "I'LL KEEP YOU SATISFIED",
       'I WANNA BE YOUR MAN', 'SWINGING ON A STAR', 'KISS ME QUICK',
       'STAY', 'NOT TOO LITTLE - NOT TOO MUCH', 'MONEY',
       'ALL I WANT FOR CHRISTMAS IS A BEATLE', 'IF I RULED THE WORLD',
       "IT'S ALMOST TOMORROW", 'HIPPY HIPPY SHAKE', 'HUNGRY FOR LOVE',
       'I (WHO HAVE NOTHING)', 'BLUE BAYOU/MEAN WOMAN BLUES',
       'WE ARE IN LOVE', 'COUNTRY BOY', 'WHAT TO DO {1963}',
       'SUGAR AND SPICE', 'BLOWING IN THE WIND',
       'AT THE PALACE (PARTS 1 AND 2)', 'DEEP PURPLE', 'I CAN DANCE',
       'FROM RUSSIA WITH LOVE', "YESTERDAY'S GONE"],
      dtype=object)
        self.check_column(self.df.Title, titles, [35,38,39,40], "Title")

    @points('p04-15.1')
    def test_artist(self):
        artists=np.array(['THE BEATLES', 'THE BEATLES', 'FREDDIE AND THE DREAMERS',
       'KATHY KIRBY', 'DUSTY SPRINGFIELD', 'THE DAVE CLARK FIVE',
       'THE SINGING NUN', 'CLIFF RICHARD', 'GENE PITNEY',
       'LOS INDIOS TABAJARAS', 'THE SHADOWS', 'GERRY AND THE PACEMAKERS',
       'BILLY J KRAMER AND THE DAKOTAS', 'THE ROLLING STONES',
       'BIG DEE IRWIN', 'ELVIS PRESLEY', 'THE HOLLIES', 'CHRIS SANDFORD',
       'BERN ELLIOTT AND THE FENMEN', 'DORA BRYAN', 'HARRY SECOMBE',
       'MARK WYNTER', 'SWINGING BLUE JEANS',
       'JOHNNY KIDD AND THE PIRATES', 'SHIRLEY BASSEY', 'ROY ORBISON',
       'ADAM FAITH', 'HEINZ', 'BUDDY HOLLY', 'THE SEARCHERS',
       'PETER, PAUL AND MARY', 'WILFRED BRAMBELL AND HARRY H CORBETT',
       'NINO TEMPO AND APRIL STEVENS', 'BRIAN POOLE AND THE TREMELOES',
       'MATT MONRO', 'CHAD STUART AND JEREMY CLYDE'], dtype=object)
        self.check_column(self.df.Artist, artists, [35,38,39,40], "Artist")

    @points('p04-15.1')
    def test_publisher(self):
        publishers=np.array(['PARLOPHONE', 'PARLOPHONE', 'COLUMBIA', 'DECCA', 'PHILIPS',
       'COLUMBIA', 'PHILIPS', 'COLUMBIA', 'UNITED ARTISTS', 'RCA',
       'COLUMBIA', 'COLUMBIA', 'PARLOPHONE', 'DECCA', 'COLPIX', 'RCA',
       'PARLOPHONE', 'DECCA', 'DECCA', 'FONTANA', 'PHILIPS', 'PYE', 'HMV',
       'HMV', 'COLUMBIA', 'LONDON', 'PARLOPHONE', 'DECCA', 'CORAL', 'PYE',
       'WARNER BROTHERS', 'PYE', 'LONDON', 'DECCA', 'PARLOPHONE',
       'EMBER'], dtype=object)
        self.check_column(self.df.Publisher, publishers, [35,38,39,40], "Publisher")

    @points('p04-15.2')
    def test_peak_pos(self):
        pps=np.array([1.0, 1.0, 3.0, 4.0, 5.0, 7.0, 2.0, 5.0, 11.0, 1.0, 4.0, 13.0,
                      17.0, 17.0, 14.0, 20.0, 18.0, 12.0, 20.0, 6.0, 3.0, 26.0, 2.0,
                      13.0, 17.0, 31.0, 20.0, 37.0])
        self.check_column(self.df["Peak Pos"], pps,
                          [6,9,15,16,23,27,29,32, 35, 38,39,40], "Peak Pos")

    @points('p04-15.1')
    def test_woc(self):
        wocs=np.array([ 4., 18.,  8.,  8.,  5.,  6.,  4.,  8.,  4.,  8.,  4., 12.,  8.,
        6.,  4.,  2.,  5.,  3.,  5.,  4.,  6.,  7.,  2.,  5., 13., 14.,
        2.,  4.,  2., 10., 10.,  4.,  7.,  4.,  6.,  3.])
        self.check_column(self.df.WoC, wocs, [35,38,39,40], "WoC")

    @points('p04-15.2')
    def test_lw(self):
        self.check_column(self.df.LW, [], range(1,41), "LW")

        
if __name__ == '__main__':
    unittest.main()
    
