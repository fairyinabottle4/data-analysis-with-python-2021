#!/usr/bin/env python3

import unittest

import numpy as np
import math

from tmc import points

from tmc.utils import load, get_stdout

nonconvex_clusters = load('src.nonconvex_clusters', 'nonconvex_clusters')

class NonconvexClusters(unittest.TestCase):


    @points('p06-06.1')
    def test_size(self):
        df = nonconvex_clusters()
        self.assertEqual(df.shape, (4,4), msg="Function nonconvex_clusters returned a DataFrame of incorrect shape!")

    @points('p06-06.1')
    def test_type(self):
        df = nonconvex_clusters()
        self.assertEqual(list(df.dtypes.values), [float, float, float, float],
                         msg="Function nonconvex_clusters returned a DataFrame of incorrect colum types!")

    @points('p06-06.1')
    def test_eps(self):
        df = nonconvex_clusters()
        np.testing.assert_allclose(df.eps.values, [0.05, 0.10, 0.15, 0.20], err_msg="Incorrect eps values!")

    @points('p06-06.1')
    def test_columns(self):
        df = nonconvex_clusters()
        self.assertEqual(list(df.columns.values), ["eps", "Score","Clusters","Outliers"],
                         msg="Incorrect column names in DataFrame returned by nonconvex_clusters!")

    @points('p06-06.2')
    def test_scores(self):
        df = nonconvex_clusters()
        self.assertAlmostEqual(df.loc[1, "Score"], 1.0, msg="Incorrect score!")
        self.assertAlmostEqual(df.loc[2, "Score"], 1.0, msg="Incorrect score!")
        self.assertTrue(math.isnan(df.Score[0]), msg="Expected NaN in Score[0]!")
        self.assertTrue(math.isnan(df.Score[3]), msg="Expected NaN in Score[3]!")

    @points('p06-06.3')
    def test_clusters(self):
        df = nonconvex_clusters()
        np.testing.assert_allclose(df.Clusters, [12, 2, 2, 1], err_msg="Incorrect values in Clusters column!")

    @points('p06-06.4')
    def test_outliers(self):
        df = nonconvex_clusters()
        np.testing.assert_allclose(df.Outliers, [118, 3, 0, 0], err_msg="Incorrect values in Outliers column!")

if __name__ == '__main__':
    unittest.main()

