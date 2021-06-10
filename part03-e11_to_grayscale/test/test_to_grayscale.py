#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
import matplotlib.pyplot as plt

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.to_grayscale"
to_grayscale = load(module_name, "to_grayscale")
to_red = load(module_name, "to_red")
to_green = load(module_name, "to_green")
to_blue = load(module_name, "to_blue")
main = load(module_name, "main")
ph = patch_helper(module_name)

class ToGrayscale(unittest.TestCase):

    def setUp(self):
        self.n = 100
        self.m = 100
        self.a = np.random.randint(0, 256, (self.n, self.m, 3))


    @points('p03-11.1')
    def test_gray(self):
        g = to_grayscale(self.a)
        self.assertEqual(g.shape, (self.n,self.m),
                         "The shape of the image should be unchanged by to_grayscale!")
        X = np.random.randint(0, self.m, 1000)
        Y = np.random.randint(0, self.n, 1000)
        for x, y in zip(X, Y):
            self.assertAlmostEqual(g[y, x], (0.2126*self.a[y, x, 0] + 0.7152*self.a[y, x, 1] + 0.0722*self.a[y, x, 2]),
                                   places=4, msg="Incorrect grayness value!")

    @points('p03-11.2')
    def test_red(self):
        r = to_red(self.a)
        np.testing.assert_array_equal(r.shape, self.a.shape, err_msg="Incorrect shape!")
        np.testing.assert_array_equal(r[:,:,0], self.a[:,:,0], err_msg="The red component should be fixed!")
        np.testing.assert_array_equal(r[:,:,[1,2]], 0, err_msg="The blue and green components should be zero")

    @points('p03-11.2')
    def test_green(self):
        g = to_green(self.a)
        np.testing.assert_array_equal(g.shape, self.a.shape, err_msg="Incorrect shape!")
        np.testing.assert_array_equal(g[:,:,1], self.a[:,:,1], err_msg="The green component should be fixed!")
        np.testing.assert_array_equal(g[:,:,[0,2]], 0, err_msg="The red and blue components should be zero")

    @points('p03-11.2')
    def test_blue(self):
        b = to_blue(self.a)
        np.testing.assert_array_equal(b.shape, self.a.shape, err_msg="Incorrect shape!")
        np.testing.assert_array_equal(b[:,:,2], self.a[:,:,2], err_msg="The blue component should be fixed!")
        np.testing.assert_array_equal(b[:,:,[0,1]], 0, err_msg="The red and green components should be zero")

    @points('p03-11.2')
    def test_main(self):
        with patch(ph("plt.show")) as pshow, \
             patch(ph("plt.imshow"), side_effect=plt.imshow) as pimshow, \
             patch(ph("plt.subplots"), side_effect=plt.subplots) as psubplots, \
             patch(ph("plt.subplot"), side_effect=plt.subplot) as psubplot:
            main()
            pshow.assert_called()
            pimshow.assert_called()
            if psubplots.call_count > 0:
                psubplots.assert_called_once()
            else:
                self.assertEqual(psubplot.call_count, 3, msg="Expected 3 calls to subplot or one to subplots")

if __name__ == '__main__':
    unittest.main()

