#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_stdout

coefficient_of_determination = load('src.coefficient_of_determination', 'coefficient_of_determination')

class CoefficientOfDetermination(unittest.TestCase):

    @points('p05-12.1')
    def test_all_features(self):
        scores = coefficient_of_determination()
        self.assertAlmostEqual(scores[0], 1.0, msg="Incorrect coefficient of determination!")

    @points('p05-12.2')
    def test_individual_features(self):
        scores = coefficient_of_determination()

        sums=[0.0258828579115,0.0968186306153,0.0881564161891,0.868276772892]
        for i in range(1,5):
            self.assertAlmostEqual(sums[i-1], sum(scores[i:i+2]),
                                   msg="Incorrect individual coefficients of determination!")


if __name__ == '__main__':
    unittest.main()
    
