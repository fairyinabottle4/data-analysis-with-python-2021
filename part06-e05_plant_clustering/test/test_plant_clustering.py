#!/usr/bin/env python3

import unittest
from unittest.mock import patch


from sklearn.cluster import KMeans
import sklearn

from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.plant_clustering"
plant_clustering = load(module_name, 'plant_clustering')
main = load(module_name, "main")
ph = patch_helper(module_name)

@points('p06-05.1')
class PlantClustering(unittest.TestCase):


    def test_correctness(self):
        acc = plant_clustering()
        self.assertAlmostEqual(acc, 0.8933333333333333, places=5, msg="Incorrect accuracy score!")

    def test_accuracy(self):
        with patch(ph('sklearn.metrics.accuracy_score'), wraps=sklearn.metrics.accuracy_score) as accuracy:
            acc = plant_clustering()
            accuracy.assert_called()


    def test_kmeans(self):
        with patch(ph('sklearn.cluster.KMeans'), side_effect=KMeans) as mock:
            acc = plant_clustering()
            mock.assert_called()
            args, kwargs = mock.call_args
            
            correct = ((len(args) > 0 and args[0]== 3) or
                       ("n_clusters" in kwargs and kwargs["n_clusters"] == 3))
            self.assertTrue(correct, msg="Expected number of clusters given to KMeans to be 3!")
            self.assertIn("random_state", kwargs,
                          msg="You did not specify random_state argument"
                          "to KMeans function!")
            self.assertEqual(kwargs["random_state"], 0,
                             msg="Incorrect random_state argument!")

            
if __name__ == '__main__':
    unittest.main()
    
