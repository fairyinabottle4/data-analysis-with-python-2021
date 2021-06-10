#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

import numpy as np
import sklearn

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name = 'src.word_classification'
get_features = load(module_name, 'get_features')
contains_valid_chars = load(module_name, 'contains_valid_chars')
get_features_and_labels = load(module_name, 'get_features_and_labels')
word_classification = load(module_name, 'word_classification')
ph = patch_helper(module_name)

class WordClassification(unittest.TestCase):


    @points('p06-03.1')
    def test_get_features(self):
        a = np.array(["abc", "zaka"])
        f = get_features(a)
        self.assertEqual(f.shape[0], 2, msg="Feature array returned by get_features had incorrect shape!")
        self.assertEqual(f.shape[1], 29, msg="Feature array returned by get_features had incorrect shape!")
        self.assertEqual(f[0,0], 1, msg="Feature array returned by get_features had incorrect content in pos [0,0]!")
        self.assertEqual(f[0,1], 1, msg="Feature array returned by get_features had incorrect content in pos [0,1]!")
        self.assertEqual(f[0,2], 1, msg="Feature array returned by get_features had incorrect content in pos [0,2]!")

        self.assertEqual(f[1,0], 2, msg="Feature array returned by get_features had incorrect content in pos [1,0]!")
        self.assertEqual(f[1,25], 1, msg="Feature array returned by get_features had incorrect content in pos [1,25]!")
        self.assertEqual(f[1,10], 1, msg="Feature array returned by get_features had incorrect content in pos [1,10]!")

    @points('p06-03.2')
    def test_contains_valid_chars(self):
        alphabet="abcdefghijklmnopqrstuvwxyzäö-"
        inputs=[alphabet, alphabet+"#", alphabet[1:], "","ä"]
        expected=[True, False, True, True]
        for s,e in zip(inputs, expected):
            self.assertEqual(contains_valid_chars(s), e, msg="Incorrect result from call contains_valid_chars('%s')!" % s)


    @points('p06-03.3')
    def test_get_features_and_labels(self):
        X, y = get_features_and_labels()
        self.assertEqual(len(X.shape), 2, msg="Incorrect dimension of feature matrix X returned by get_features_and_labels!")
        self.assertEqual(X.shape, (y.shape[0], 29), msg="Incorrect shape of feature matrix X returned by get_features_and_labels!")
        self.assertEqual(y.shape[0], 157006, msg="Incorrect shape of target vector y returned by get_features_and_labels!")
        self.assertEqual(sum(y), 63260, msg="Incorrect content in target vector y returned by get_features_and_labels!")

    @points('p06-03.4')
    def test_word_classification(self):
        v = word_classification()
        self.assertEqual(len(v), 5, msg="Expected that function word_classification returns 5 accuracy scores!")

        good=True
        try:
            correct=[0.89370104, 0.89678673, 0.89758288, 0.89685042, 0.89643642]
            for a, b in zip(correct, v):
                self.assertAlmostEqual(a, b, msg="Incorrect accuracy score returned by word_classification!")
        except AssertionError:
            good=False


        if not good:
            # Result of non-shuffled cross validation
            correct=[0.86833706, 0.96897443, 0.842957,   0.87366338, 0.88320352]
            for a, b in zip(correct, v):
                self.assertAlmostEqual(a, b, msg="Incorrect accuracy score returned by word_classification!")

    @points('p06-03.4')
    def test_word_classification_calls(self):
        with patch(ph("sklearn.model_selection.cross_val_score"),
                   wraps=sklearn.model_selection.cross_val_score) as cvs,\
             patch(ph("sklearn.model_selection.KFold"),
                   wraps=sklearn.model_selection.KFold) as kf:
            v = word_classification()
            cvs.assert_called()
            kf.assert_called()
            args, kwargs = kf.call_args
            self.assertIn("random_state", kwargs,
                          msg="You did not specify random_state argument to KFold function!")
            self.assertEqual(kwargs["random_state"], 0,
                             msg="Incorrect random_state argument!")
            self.assertIn("shuffle", kwargs,
                          msg="You did not specify shuffle argument to KFold function!")
            self.assertEqual(kwargs["shuffle"], True,
                             msg="Incorrect shuffle argument!")
if __name__ == '__main__':
    unittest.main()

