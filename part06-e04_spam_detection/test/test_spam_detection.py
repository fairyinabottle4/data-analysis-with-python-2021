#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

from tmc import points

from tmc.utils import load, get_stdout, patch_helper, spy_decorator

import sklearn

module_name="src.spam_detection"
spam_detection = load(module_name, 'spam_detection')
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p06-04.1')
@points('p06-04.2')
class SpamDetection(unittest.TestCase):


    def test_first(self):
        accuracy, total, misclassified = spam_detection(random_state=0, fraction=0.1)
        self.assertEqual(accuracy, 0.96, msg="Incorrect accuracy, when random_state=0 and fraction=0.1!")
        self.assertEqual(total, 75, msg="Incorrect sample size, when random_state=0 and fraction=0.1!")
        self.assertEqual(misclassified, 3, msg="Incorrect misclassified count, when random_state=0 and fraction=0.1!")

    def test_second(self):
        accuracy, total, misclassified = spam_detection(random_state=5, fraction=0.1)
        self.assertAlmostEqual(accuracy, 0.9066666666666666, msg="Incorrect accuracy, when random_state=5 and fraction=0.1!")
        self.assertEqual(total, 75, msg="Incorrect sample size, when random_state=5 and fraction=0.1!")
        self.assertEqual(misclassified, 7, msg="Incorrect misclassified count, when random_state=5 and fraction=0.1!")

    def test_calls(self):
        predict_method = spy_decorator(sklearn.naive_bayes.MultinomialNB.predict, "predict")
        score_method = spy_decorator(sklearn.naive_bayes.MultinomialNB.score, "score")
        fit_method = spy_decorator(sklearn.naive_bayes.MultinomialNB.fit, "fit")
        with patch(ph("sklearn.model_selection.train_test_split"),
                   wraps=sklearn.model_selection.train_test_split) as tts,\
             patch(ph("sklearn.metrics.accuracy_score"),
                   wraps=sklearn.metrics.accuracy_score) as acs,\
             patch.object(sklearn.naive_bayes.MultinomialNB, "fit", new=fit_method),\
             patch.object(sklearn.naive_bayes.MultinomialNB, "predict", new=predict_method),\
             patch.object(sklearn.naive_bayes.MultinomialNB, "score", new=score_method),\
             patch(ph("sklearn.naive_bayes.MultinomialNB"),
                   wraps=sklearn.naive_bayes.MultinomialNB) as mnb:

            random_state=7
            accuracy, total, misclassified = spam_detection(random_state, fraction=0.1)

            # Check that train_test_split is called with correct parameters
            tts.assert_called_once()
            args, kwargs = tts.call_args
            self.assertIn("random_state", kwargs,
                          msg="You did not specify random_state argument"
                          "to train_test_split function!")
            self.assertEqual(kwargs["random_state"], random_state,
                             msg="Incorrect random_state argument!")
            if "train_size" in kwargs:
                self.assertEqual(kwargs["train_size"], 0.75,
                                 msg="Incorrect train_size argument!")
            if "test_size" in kwargs:
                self.assertEqual(kwargs["test_size"], 0.25,
                                 msg="Incorrect test_size argument!")
            # Check that accuracy_score is called
            self.assertTrue(acs.call_count == 1 or score_method.mock.call_count == 1,
                            msg="Expected that either the accuracy_score function or the score method is called exactly once!")

            # Check that MultinomialNB is called
            mnb.assert_called_once()

            # Check that fit and predict methods of MultinomialNB object are called
            predict_method.mock.assert_called()
            fit_method.mock.assert_called()


if __name__ == '__main__':
    unittest.main()

