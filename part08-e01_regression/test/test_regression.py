#!/usr/bin/env python3

import os
import re
import pandas as pd
import numpy as np
import statsmodels
import matplotlib.pyplot as plt
import matplotlib

import unittest
from unittest.mock import patch, MagicMock

from tmc import points
from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.regression"
regression = load(module_name, "regression")
main = load(module_name, "main")
ph = patch_helper(module_name)

def get_exercises(nb):
    pattern = r"^#\s*exercise\s+(\d+)\s*"
    result = {}
    for cell in nb.cells:
        if cell.cell_type == "code" and re.match(pattern, cell.source):
            m = re.match(pattern, cell.source)
            n = int(m.group(1))
            assert n not in result, "Overlapping exercise number %i" % n
            result[n] = cell.source
    return result

inputnb = "src/project_notebook_regression_analysis.ipynb"
exercises = {}
# UNCOMMENT THE BELOW THREE LINES
import nbformat
nb = nbformat.read(inputnb, as_version=4)
exercises = get_exercises(nb)

#print("Read %i exercises:" % len(exercises))
#print(exercises.keys())



def find_interaction(var1, var2, params):
    interaction1 = var1 + ":" + var2
    interaction2 = var2 + ":" + var1
    if interaction1 in params:
        return interaction1
    elif interaction2 in params:
        return interaction2
    else:
        return None

class Regression(unittest.TestCase):


    def check_explanators(self, explanators, params):
        for e in explanators:
            if type(e) == tuple:
                assert len(e) == 2
                var1, var2 = e
                val = find_interaction(var1, var2, params)
                self.assertNotEqual(val, None,
                                 msg="Model parameters are missing interaction between variable %s and %s!" % e)
            else:
                self.assertTrue(e in params, msg="Model parameter %s missing!" % e)


    @points('p08-01.0')
    def test_00_imports(self):
        exec(exercises[0])
        self.assertTrue("statsmodels" in locals(), msg="Module statsmodels was not loaded!")
        self.assertTrue("pd" in locals(), msg="Module pandas was not loaded!")

    @points('p08-01.1')
    def test_01_load(self):
        #exec(exercises[0])
        describe_method = spy_decorator(pd.core.frame.DataFrame.describe, "describe")
        with patch("pandas.read_csv", wraps=pd.read_csv) as prc,\
             patch.object(pd.core.frame.DataFrame, "describe", new=describe_method):
            exec(exercises[1])
            prc.assert_called()
            #fram=int()
            self.assertTrue("fram" in locals(), msg="DataFrame 'fram' was not loaded!")
            myfram = locals()["fram"]
            self.assertIsInstance(myfram, pd.core.frame.DataFrame,
                                  msg="'fram' is not a DataFrame object!")
            self.assertEqual(myfram.shape, (1394, 14),
                             msg="The read DataFrame had incorrect shape!")
            #koe.assert_called()
            describe_method.mock.assert_called()

    @points('p08-01.2')
    def test_02_rescale(self):
        exec(exercises[2])
        self.assertTrue("rescale" in locals(), msg="Could not find function 'rescale'!")
        s = pd.Series(np.random.randn(10)*6 + 3)
        myrescale = locals()["rescale"]
        s2 = myrescale(s)
        mean = s2.mean()
        sigma = s2.std()
        self.assertAlmostEqual(mean, 0, msg="Expected rescale to return series having expectation 0!")
        self.assertAlmostEqual(sigma, 0.5,
                               msg="Expected rescale to return series having standard deviation 0.5!")


    @points('p08-01.3')
    def test_03_rescaled_variables(self):
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        myfram = locals()["fram"]
        for variable in "sAGE sFRW sSBP sDBP sCHOL sCIG".split():
            self.assertIn(variable, myfram,
                          msg="Expected rescaled variable %s in the DataFrame!" % variable)
            mean = myfram[variable].mean()
            std = myfram[variable].std()
            self.assertAlmostEqual(mean, 0,
                                   msg="Expected variable %s to have expectation 0!" % variable)
            self.assertAlmostEqual(std, 0.5,
                                   msg="Expected variable %s to have standard deviation 0.5!" % variable)
    @points('p08-01.4')
    def test_04_sbp1(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[4])
        myfit = locals()["fit"]
        self.assertAlmostEqual(myfit.params.Intercept, 150.0199, places=2, msg="Incorrect intercept!")
        self.assertAlmostEqual(myfit.params.sFRW, 17.7205, places=2,
                               msg="Incorrect coefficient for sFRW!")
        self.assertAlmostEqual(myfit.params.sCHOL, 4.9169, places=2,
                               msg="Incorrect coefficient for sCHOL!")
        self.assertAlmostEqual(myfit.params["SEX[T.male]"], -4.0659, places=2,
                               msg="Incorrect coefficient for gender!")

    @points('p08-01.5')
    def test_05_sbp_with_age(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[5])
        myfit = locals()["fit"]
        self.assertAlmostEqual(myfit.params.sAGE, 8.1332, places=2,
                               msg="Incorrect coefficient for sAGE!")
        self.assertEqual(len(myfit.params), 5, msg="Expected four explanatory variables and an intercept!")


    @points('p08-01.6')
    def test_06_sbp_with_interactions(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[6])
        myfit = locals()["fit"]
        self.assertIn("sAGE", myfit.params, msg="Missing explanatory variable sAGE!")
        self.assertAlmostEqual(myfit.params.sAGE, 10.218851215627154, places=2,
                               msg="Incorrect coefficient for sAGE!")
        interaction = find_interaction("sFRW", "sAGE", myfit.params)
        found = interaction is not None
        self.assertAlmostEqual(myfit.params[interaction], -2.0865742749328025, places=2,
                               msg="Incorrect coefficient for sFRW:sAGE!")
        self.assertEqual(len(myfit.params), 11, msg="Expected ten explanatory variables and an intercept!")

    @points('p08-01.7')
    def test_07_sbp_with_interactions_visualization(self):
        plot_method = spy_decorator(pd.core.frame.DataFrame.plot.scatter, "scatter")
        with patch("matplotlib.pyplot.scatter", wraps=matplotlib.pyplot.scatter) as pltscatter,\
             patch.object(pd.core.frame.DataFrame.plot, "scatter", new=plot_method),\
             patch("statsmodels.graphics.regressionplots.abline_plot",
                   wraps=statsmodels.graphics.regressionplots.abline_plot) as abplot:
            exec(exercises[0])
            exec(exercises[1])
            exec(exercises[2])
            exec(exercises[3])
            exec(exercises[6])
            exec(exercises[7])
            myfit = locals()["fit"]
            #abplot.assert_called()
            self.assertEqual(abplot.call_count, 3, msg="Expected abline_plot to be called three times!")
            self.assertTrue(pltscatter.call_count > 0 or plot_method.mock.call_count > 0,
                            msg="Expected call to make a scatter plot!")


    @points('p08-01.8')
    def test_08_sbp_with_cigarets(self):
        plot_method = spy_decorator(pd.core.frame.DataFrame.plot.scatter, "scatter")
        with patch("matplotlib.pyplot.scatter", wraps=matplotlib.pyplot.scatter) as pltscatter,\
             patch.object(pd.core.frame.DataFrame.plot, "scatter", new=plot_method),\
             patch("statsmodels.graphics.regressionplots.abline_plot",
                   wraps=statsmodels.graphics.regressionplots.abline_plot) as abplot:
            exec(exercises[0])
            exec(exercises[1])
            exec(exercises[2])
            exec(exercises[3])
            exec(exercises[8])
            myfit = locals()["fit"]
            self.assertIn("sCIG", myfit.params, msg="Missing explanatory variable sCIG!")
            self.assertAlmostEqual(myfit.params.sCIG, 3.7733, places=2,
                                   msg="Incorrect coefficient for sCIG!")
            interaction = find_interaction("sFRW", "sCIG", myfit.params)

            found = interaction is not None
            self.assertTrue(found, msg="Missing explanatory variable sFRW:sCIG!")
            self.assertAlmostEqual(myfit.params[interaction], 3.6765, places=2,
                                   msg="Incorrect coefficient for sFRW:sCIG!")
            self.assertEqual(len(myfit.params), 16, msg="Expected 15 explanatory variables and an intercept!")
            #abplot.assert_called()
            self.assertEqual(abplot.call_count, 3, msg="Expected abline_plot to be called three times!")
            self.assertTrue(pltscatter.call_count > 0 or plot_method.mock.call_count > 0,
                            msg="Expected call to make a scatter plot!")

    @points('p08-01.9')
    def test_09_high_blood_pressure(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[9])
        myfram = locals()["fram"]
        myfit = locals()["fit"]
        self.assertIn("HIGH_BP", myfram.columns, msg="No variable HIGH_BP in DataFrame 'fram'!")
        self.assertEqual(int, myfram["HIGH_BP"].dtype, msg="Use type 'int' for variable HIGH_BP!")
        self.assertEqual(len(myfit.params), 4, msg="Expected 3 explanatory variables and an intercept!")
        found = "error_rate_orig" in locals()
        self.assertTrue(found, msg="Result variable 'error_rate_orig' missing!")
        myerror_rate_orig = locals()["error_rate_orig"]
        self.assertAlmostEqual(myerror_rate_orig, 0.35581061692969873, places=4, msg="Incorrect error rate!")

    @points('p08-01.10')
    def test_10_high_blood_pressure2(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[9])
        exec(exercises[10])
        myfram = locals()["fram"]
        myfit = locals()["fit"]
        self.assertIn("HIGH_BP", myfram.columns, msg="No variable HIGH_BP in DataFrame 'fram'!")
        self.assertEqual(int, myfram["HIGH_BP"].dtype, msg="Use type 'int' for variable HIGH_BP!")
        self.assertEqual(len(myfit.params), 7, msg="Expected 6 explanatory variables and an intercept!")
        found = "error_rate" in locals()
        self.assertTrue(found, msg="Result variable 'error_rate' missing!")
        myerror_rate = locals()["error_rate"]
        self.assertAlmostEqual(myerror_rate, 0.3278335724533716, places=4, msg="Incorrect error rate!")


    @points('p08-01.11')
    def test_11_high_blood_pressure3(self):
        scatter_method = spy_decorator(matplotlib.axes.Axes.scatter, "scatter")
        plot_method = spy_decorator(matplotlib.axes.Axes.plot, "plot")
#        with patch("matplotlib.pyplot.scatter", wraps=matplotlib.pyplot.scatter) as pltscatter:
        with patch("matplotlib.pyplot.subplots", wraps=matplotlib.pyplot.subplots) as psubplots,\
             patch.object(matplotlib.axes.Axes, "plot", new=plot_method),\
             patch.object(matplotlib.axes.Axes, "scatter", new=scatter_method):
            exec(exercises[0])
            exec(exercises[1])
            exec(exercises[2])
            exec(exercises[3])
            exec(exercises[9])
            exec(exercises[10])
            exec(exercises[11])
            myfram = locals()["fram"]
            psubplots.assert_called()
            self.assertEqual(scatter_method.mock.call_count, 2,
                          msg="Expected scatter method to be called twice!")
            self.assertEqual(plot_method.mock.call_count, 6,
                             msg="Expected plot method to be called six times!")

            (args1, kwargs1), (args2, kwargs2)  = scatter_method.mock.call_args_list
            self.assertIn(len(args1[0]), [663, 731], msg="Incorrect number of points in subfigure 1!")
            self.assertEqual(len(args1[0]), len(args1[1]), msg="Incorrect number of points in subfigure 1!")

            self.assertIn(len(args2[0]), [663, 731], msg="Incorrect number of points in subfigure 2!")
            self.assertEqual(len(args2[0]), len(args2[1]), msg="Incorrect number of points in subfigure 2!")


    @points('p08-01.12')
    def test_12_train_test_split(self):
        orig = pd.DataFrame(np.random.randn(10,10))
        df = orig.copy()
        exec(exercises[0])
        exec(exercises[12])
        self.assertTrue("train_test_split" in locals(),
                        msg="Could not find function 'train_test_split' %s, %s!" % (locals(), exercises[12]))
        mytrain_test_split = locals()["train_test_split"]
        np.random.seed(1)
        train1, test1 = mytrain_test_split(df, train_fraction=0.8)
        self.assertTrue(orig.equals(df), msg="The train_test_split function should not modify the original DataFrame!")
        self.assertEqual(len(train1), 8, msg="Expected training set to have size 0.8*originalsize!")
        self.assertEqual(len(test1), 2, msg="Expected training set to have size 0.2*originalsize!")
        np.random.seed(1)
        train2, test2 = mytrain_test_split(df, train_fraction=0.8)
        self.assertTrue(train1.equals(train2),
                        msg="If called twice with the same parameters and same seed, the result should be the same!")
        self.assertTrue(test1.equals(test2),
                        msg="If called twice with the same parameters and same seed, the result should be the same!")

    @points('p08-01.13')
    def test_13_cross_validation(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[9])
        exec(exercises[12])
        #mytrain_test_split = locals()["train_test_split"]
        #with patch("mytrain_test_split", wraps=mytrain_test_split) as psplit:
        exec(exercises[13])
        self.assertIn("error_model", locals(), msg="Could not find variable 'error_model'!")
        myerror_model = locals()["error_model"]
        #myerror_null = locals()["error_null"]
        self.assertAlmostEqual(np.mean(myerror_model), 0.3311827956989248,
                               places=4, msg="Incorrect mean error rate!")
        #self.assertAlmostEqual(np.mean(myerror_null), x,
        #                       places=4, msg="Incorrect mean error rate by null model!")


    @points('p08-01.14')
    def test_14_chd(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[14])
        myfram = locals()["fram"]
        self.assertIn("hasCHD", myfram.columns, msg="No variable hasCHD in DataFrame 'fram'!")
        self.assertEqual(int, myfram["hasCHD"].dtype, msg="Use type 'int' for variable hasCHD!")
        self.assertAlmostEqual(myfram.hasCHD.mean(), 0.22022955523672882, places=4, msg="Variable hasCHD has incorrect mean!")


    @points('p08-01.15')
    def test_15_chd2(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[14])
        exec(exercises[15])
        myfram = locals()["fram"]
        myfit = locals()["fit"]
        self.assertIn("hasCHD", myfram.columns, msg="No variable hasCHD in DataFrame 'fram'!")
        self.assertEqual(int, myfram["hasCHD"].dtype, msg="Use type 'int' for variable hasCHD!")
        self.assertEqual(len(myfit.params), 7, msg="Expected 6 explanatory variables and an intercept!")
        self.check_explanators("sCHOL sCIG sFRW".split() +
                               [("sCHOL", "sCIG"), ("sCHOL", "sFRW"), ("sCIG", "sFRW")], myfit.params)
        found = "error_rate" in locals()
        self.assertTrue(found, msg="Result variable 'error_rate' missing!")
        myerror_rate = locals()["error_rate"]
        self.assertAlmostEqual(myerror_rate, 0.22022955523672882, places=4, msg="Incorrect error rate!")

    @points('p08-01.16')
    def test_16_chd_visualization(self):
        with patch("matplotlib.pyplot.scatter", wraps=matplotlib.pyplot.scatter) as pltscatter,\
            patch("matplotlib.pyplot.plot", wraps=matplotlib.pyplot.plot) as pltplot:
            exec(exercises[0])
            exec(exercises[1])
            exec(exercises[2])
            exec(exercises[3])
            exec(exercises[14])
            exec(exercises[15])
            exec(exercises[16])
            pltscatter.assert_called()
            pltplot.assert_called()

    @points('p08-01.17')
    def test_17_chd_prediction(self):
        exec(exercises[0])
        exec(exercises[1])
        exec(exercises[2])
        exec(exercises[3])
        exec(exercises[14])
        exec(exercises[15])
        exec(exercises[16])
        exec(exercises[17])
        self.assertTrue("point" in locals(), msg="Could not find variable 'point'!")
        mypoint = locals()["point"]
        self.assertIsInstance(mypoint, dict, msg="Expected variable 'point' to be a dictionary!")
        for v in "sCHOL sCIG sFRW".split():
            self.assertIn(v, mypoint, msg="The point dictionary does not contain value for %s!" % v)
        self.assertTrue("predicted" in locals(), msg="Could not find variable 'predicted'!")
        mypredicted = locals()["predicted"]
        self.assertIsInstance(mypredicted, float,
                              msg="Expected the variable 'predicted' to have type 'float', got %s!" % type(mypredicted))
        self.assertAlmostEqual(mypredicted, 0.2161616602504101, places=4, msg="Incorrect predicted probability for the point!")

if __name__ == '__main__':
    unittest.main()


