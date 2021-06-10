#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
import matplotlib.pyplot as plt

from tmc import points
from tmc.utils import load, get_stdout, patch_helper

module_name="src.radial_fade"
radial_distance = load(module_name, "radial_distance")
radial_mask = load(module_name, "radial_mask")
radial_fade = load(module_name, "radial_fade")
center = load(module_name, "center")
main = load(module_name, "main")
ph = patch_helper(module_name)

class RadialFade(unittest.TestCase):

    @points('p03-12.1')
    def test_center(self):
        a=np.zeros((10,11))
        cy, cx = center(a)
        self.assertEqual((cy, cx), (4.5, 5), msg="Wrong center for image of shape %s!" % (a.shape,))

        a=np.zeros((10,9,3))
        cy, cx = center(a)
        self.assertEqual((cy, cx), (4.5, 4), msg="Wrong center for image of shape %s!" % (a.shape,))

    @points('p03-12.1')
    def test_radial_distance(self):
        a=np.zeros((3,3,3))
        rd = radial_distance(a)
        self.assertEqual(rd.shape, a.shape[:2],
                         msg="radial_distance returned array of wrong shape for input array of shape %s!" %
                         (a.shape,))
        np.testing.assert_array_equal(rd[0], np.array([np.sqrt(2), 1, np.sqrt(2)]),
                                      err_msg="Incorrect values at the first row of radial distance matrix!")
        np.testing.assert_array_equal(rd[1], np.array([1, 0, 1]),
                                      err_msg="Incorrect values at the second row of radial distance matrix!")
        np.testing.assert_array_equal(rd[2], np.array([np.sqrt(2), 1, np.sqrt(2)]),
                                      err_msg="Incorrect values at the third row of radial distance matrix!")

        a=np.zeros((2,2,3))
        rd = radial_distance(a)
        self.assertEqual(rd.shape, a.shape[:2],
                         msg="radial_distance returned array of wrong shape for input array of shape %s!" % (a.shape,))
        np.testing.assert_allclose(rd[0], np.array([1/np.sqrt(2), 1/np.sqrt(2)]),
                                   err_msg="Incorrect values at the first row of radial distance matrix!")
        np.testing.assert_allclose(rd[1], np.array([1/np.sqrt(2), 1/np.sqrt(2)]),
                                   err_msg="Incorrect values at the second row of radial distance matrix!")

        for n in range(1,10, 2):
            a=np.zeros((n,n,3))
            rd = radial_distance(a)
            self.assertGreaterEqual(rd.max(), 0.0, msg="The radial distance cannot be negative!")

    @points('p03-12.2')
    def test_radial_mask(self):
        for n in range(1, 10):
            for m in range(1, 10):
                a=np.zeros((n, m, 3))
                rm = radial_mask(a)
                self.assertEqual(rm.shape, a.shape[:2], msg="Incorrect shape of radial mask!")
                self.assertLessEqual(rm.max(), 1.0, msg="Maximum value in the mask cannot be above 1.0")
                self.assertLessEqual(0.0, rm.min(), msg="Minimum value in the mask cannot be below 0.0")
                cy = (n-1)//2
                cx = (m-1)//2
                self.assertEqual(rm[cy, cx], 1.0, msg="Value of the radial mask should be 1 in the center!")

    @points('p03-12.2')
    def test_radial_mask_size_one(self):
        n=1
        a=np.zeros((n,n,3))
        rm = radial_mask(a)
        self.assertEqual(rm[0,0], 1.0, msg="Are you sure the radial_mask function works correctly for arrays of size 1")

    @points('p03-12.2')
    def test_radial_fade(self):
        for n in range(1, 10):
            for m in range(1, 10):
                a=np.random.randn(n,m,3)
                result = radial_fade(a)
                cy = (n-1) // 2
                cx = (m-1) // 2
                self.assertTrue((result[cy,cx] == a[cy,cx]).all(),
                            msg="In the center of the image there should be no fading!")

    @points('p03-12.2')
    def test_main(self):
        with patch(ph("plt.subplots"), side_effect=plt.subplots) as psubplots,\
             patch(ph("plt.subplot"), side_effect=plt.subplot) as psubplot, \
             patch(ph("radial_mask"), side_effect=radial_mask) as pradial_mask,\
             patch(ph("radial_fade"), side_effect=radial_mask) as pradial_fade,\
             patch(ph("plt.show")) as pshow:
            main()
            if psubplots.call_count > 0:
                psubplots.assert_called_once()
            else:
                self.assertEqual(psubplot.call_count, 3, msg="expected 3 calls to subplot or one to subplots")
            pshow.assert_called()
            pradial_mask.assert_called()
            pradial_fade.assert_called()


if __name__ == '__main__':
    unittest.main()

