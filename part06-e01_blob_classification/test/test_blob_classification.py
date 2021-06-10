#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

import numpy as np
from sklearn.datasets import make_blobs
import sklearn

from tmc import points
from tmc.utils import load, get_stdout, patch_helper, spy_decorator

module_name="src.blob_classification"
blob_classification = load(module_name, 'blob_classification')
main = load(module_name, "main")
ph = patch_helper(module_name)


@points('p06-01.1')
class BlobClassification(unittest.TestCase):


    def test_correctness(self):
        a=np.array([[2.  , 2.  , 0.  , 2.5 , 0.76],
                    [2.  , 3.  , 1.  , 1.5 , 0.96],
                    [2.  , 2.  , 6.  , 3.5 , 0.84],
                    [2.  , 2.  , 3.  , 1.2 , 1.  ],
                    [2.  , 4.  , 4.  , 2.7 , 0.8 ]])
        idx=np.arange(5)
        np.random.shuffle(idx)
        for row in a[idx]:
            X,y = make_blobs(100, int(row[0]), centers=int(row[1]),
                                      random_state=int(row[2]), cluster_std=row[3])
            acc=blob_classification(X, y)
            self.assertAlmostEqual(acc, row[-1], msg="Incorrect accuracy score!")

    def test_calls(self):
        row = [2.  , 2.  , 0.  , 2.5 , 0.76]
        X,y = make_blobs(100, int(row[0]), centers=int(row[1]),
                         random_state=int(row[2]), cluster_std=row[3])
        predict_method = spy_decorator(sklearn.naive_bayes.GaussianNB.predict, "predict")
        fit_method = spy_decorator(sklearn.naive_bayes.GaussianNB.fit, "fit")
        with patch(ph("sklearn.model_selection.train_test_split"),
                   wraps=sklearn.model_selection.train_test_split) as tts,\
            patch(ph("sklearn.metrics.accuracy_score"),
                  wraps=sklearn.metrics.accuracy_score) as acs,\
            patch.object(sklearn.naive_bayes.GaussianNB, "fit", new=fit_method),\
            patch.object(sklearn.naive_bayes.GaussianNB, "predict", new=predict_method),\
            patch(ph("sklearn.naive_bayes.GaussianNB"),
                  wraps=sklearn.naive_bayes.GaussianNB) as gnb:

            acc=blob_classification(X, y)

            # Check that train_test_split is called with correct parameters
            tts.assert_called_once()
            args, kwargs = tts.call_args
            self.assertIn("random_state", kwargs,
                          msg="You did not specify random_state argument"
                          "to train_test_split function!")
            self.assertEqual(kwargs["random_state"], 0,
                             msg="Incorrect random_state argument!")
            if "train_size" in kwargs:
              self.assertEqual(kwargs["train_size"], 0.75, msg="Incorrect train_size argument!")
            elif "test_size" in kwargs:
              self.assertEqual(kwargs["test_size"], 0.25, msg="Incorrect test_size argument!")

            # Check that accuracy_score is called
            acs.assert_called_once()

            # Check that GaussianNB is called
            gnb.assert_called_once()

            # Check that fit and predict methods of GaussianNB object are called
            predict_method.mock.assert_called()
            fit_method.mock.assert_called()

if __name__ == '__main__':
    unittest.main()

