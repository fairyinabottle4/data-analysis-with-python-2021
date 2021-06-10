#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import sklearn

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.plant_classification"
plant_classification = load(module_name, 'plant_classification')
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p06-02.1')
class PlantClassification(unittest.TestCase):


    def test_correctness(self):
        acc = plant_classification()
        self.assertAlmostEqual(acc, 0.966667, places=5, msg="Incorrect accuracy score!")

    def test_accuracy_called(self):
        score_method = spy_decorator(sklearn.naive_bayes.GaussianNB.score, "score")
        with patch(ph('sklearn.metrics.accuracy_score'),
                   side_effect=sklearn.metrics.accuracy_score) as accuracy, \
             patch.object(sklearn.naive_bayes.GaussianNB, "score", new=score_method):
            acc = plant_classification()
            try:
                score_method.assert_called_once()
            except:
                accuracy.assert_called_once()

    def test_third(self):
        with patch(ph('sklearn.model_selection.train_test_split'),
                   side_effect=train_test_split) as split:
            acc = plant_classification()
            split.assert_called_once()
            args, kwargs = split.call_args
            self.assertIn('random_state', kwargs,
                          msg="You did not give the random_state argument to"
                          "train_test_split!")
            self.assertEqual(kwargs['random_state'], 0,
                             msg="Incorrect argument value passed to train_test_split function!")
            if "test_size" in kwargs:
                self.assertEqual(kwargs["test_size"], 0.2,
                                 msg="Incorrect argument value passed to train_test_split function!")
            else:
                self.assertIn('train_size', kwargs,
                              msg="You did not give the train_size argument to train_test_split!")
                self.assertEqual(kwargs['train_size'], 0.8,
                                 msg="Incorrect argument value passed to train_test_split function!")

    def test_gaussian(self):
        predict_method = spy_decorator(sklearn.naive_bayes.GaussianNB.predict, "predict")
        fit_method = spy_decorator(sklearn.naive_bayes.GaussianNB.fit, "fit")

        with patch.object(sklearn.naive_bayes.GaussianNB, "fit", new=fit_method),\
             patch.object(sklearn.naive_bayes.GaussianNB, "predict", new=predict_method),\
             patch(ph('sklearn.naive_bayes.GaussianNB'),
                   wraps=sklearn.naive_bayes.GaussianNB) as mock_gaussian:
            acc = plant_classification()
            mock_gaussian.assert_called_once()

            # Check that fit and predict methods of GaussianNB object are called
            predict_method.mock.assert_called()
            fit_method.mock.assert_called()

if __name__ == '__main__':
    unittest.main()

