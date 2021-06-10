#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import sklearn
import re

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.explained_variance"
explained_variance = load(module_name, "explained_variance")
main = load(module_name, "main")
ph = patch_helper(module_name)


class ExplainedVariance(unittest.TestCase):

    @points('p06-08.1')
    def test_values(self):
        v, ev = explained_variance()
        self.assertEqual(len(v), 10, msg="Incorrect number of variances returned by explained variance!")
        self.assertEqual(len(ev), 10, msg="Incorrect number of explained variances returned by explained variance!")
        self.assertAlmostEqual(sum(v), 9.41021150221, msg="Incorrect variances returned by explained variance!")
        self.assertAlmostEqual(sum(ev), 9.41021150221, msg="Incorrect explained variances returned by explained variance!")

    @points('p06-08.1')
    def test_pca(self):
        fit_method = spy_decorator(sklearn.decomposition.PCA.fit, "fit")
        with patch.object(sklearn.decomposition.PCA, "fit", new=fit_method),\
             patch(ph("sklearn.decomposition.PCA"), wraps=sklearn.decomposition.PCA) as mypca:
            v, ev = explained_variance()
            mypca.assert_called_once()
            args, kwargs = mypca.call_args
            if len(args) > 0:
                self.assertEqual(args[0], 10, msg="Expected parameter 10 to PCA function!")
            fit_method.mock.assert_called()
            args, kwargs = fit_method.mock.call_args
            df = args[0]
            self.assertEqual(df.shape[0], 400, msg="Incorrect number of rows in DataFrame to 'fit' method!")
            self.assertEqual(df.shape[1], 10, msg="Incorrect number of columns in DataFrame to 'fit' method!")

    @points('p06-08.1')
    def test_print(self):
        with patch(ph("plt.show")) as pshow:
            main()
            pshow.assert_called_once()
            out = get_stdout()
            self.assertIn("The variances are:", out, msg="You did not output the variances from the main function!")
            self.assertIn("The explained variances after PCA are:", out, msg="You did not output the explained variances from the main function!")

            m = re.search(r"^The variances are: *(.*)$", out, re.MULTILINE)
            variances = m[1].split()
            self.assertEqual(len(variances), 10, msg="Expected ten variances to be printed after 'The variances are:'!")
            for v in variances:
                self.assertRegex(v, r"^\d+\.\d\d\d$",
                                 msg="The variance should be printed with precision of three decimals!")

            m = re.search(r"^The explained variances after PCA are: *(.*)$", out, re.MULTILINE)
            evariances = m[1].split()
            self.assertEqual(len(evariances), 10,
                             msg="Expected ten explained variances to be printed after 'The explained variances after PCA are:'!")
            for e in evariances:
                self.assertRegex(e, r"^\d+\.\d\d\d$",
                                 msg="The explained variance should be printed with precision of three decimals!")

    @points('p06-08.2')
    def test_plot(self):
        with patch(ph("plt.plot")) as myplot:
            with patch(ph("plt.show")) as myshow:
                main()
                myplot.assert_called_once()
                myshow.assert_called_once()
                args = myplot.call_args[0]
                self.assertTrue((args[0] == np.arange(1,11)).all(), msg="Incorrect x values for plt.plot!")
                np.testing.assert_allclose(args[1], [8.075043,  8.890709,  9.410212,  9.410212,  9.410212,  9.410212, 9.410212,  9.410212,  9.410212,  9.410212], err_msg="Incorrect y values for plt.plot!")


if __name__ == '__main__':
    unittest.main()

