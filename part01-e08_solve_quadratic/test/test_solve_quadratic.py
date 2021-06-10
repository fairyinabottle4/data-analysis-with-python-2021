#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import numpy as np

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.solve_quadratic"
solve_quadratic = load(module_name, "solve_quadratic")

def equation(a, b, c):
    return "%f*x**2 + %f*x + %f == 0" % (a,b,c)

@points('p01-08.1')
class SolveQuadratic(unittest.TestCase):

    def test_first(self):
        a=1; b=-3; c=2
        sol = solve_quadratic(a,b,c)
        self.assertIsInstance(sol, tuple, f"solve_quadratic should return a tuple. Got {type(sol)}")
        eq = equation(a, b, c)
        self.assertEqual(len(sol), 2, msg="Expected two solutions for equation %s!" % eq)
        for x in sol:
            self.assertAlmostEqual(a*x**2 + b*x + c, 0, places=4, msg="%f is not a solution for equation %s!" % (x, eq))

    def test_second(self):
        a=1; b=2; c=1
        sol = solve_quadratic(a,b,c)
        self.assertIsInstance(sol, tuple, f"solve_quadratic should return a tuple. Got {type(sol)}")
        eq = equation(a, b, c)
        self.assertEqual(len(sol), 2, msg="Expected two solutions for equation %s!" % eq)
        for x in sol:
            self.assertAlmostEqual(a*x**2 + b*x + c, 0, places=4, msg="%f is not a solution for equation %s!" % (x, eq))

    def test_third(self):
        a=-2; b=2; c=1
        sol = solve_quadratic(a,b,c)
        self.assertIsInstance(sol, tuple, f"solve_quadratic should return a tuple. Got {type(sol)}")
        eq = equation(a, b, c)
        self.assertEqual(len(sol), 2, msg="Expected two solutions for equation %s!" % eq)
        for x in sol:
            self.assertAlmostEqual(a*x**2 + b*x + c, 0, places=4, msg="%f is not a solution for equation %s!" % (x, eq))

    def test_random(self):
        b=0; a=c=1
        while b**2 - 4*a*c <= 0:  # while the solutions are complex, get new random coefficients
            r=np.random.rand(3)*10
            a, b, c = r
        sol = solve_quadratic(a,b,c)
        self.assertIsInstance(sol, tuple, f"solve_quadratic should return a tuple. Got {type(sol)}")
        eq = equation(a, b, c)
        self.assertEqual(len(sol), 2, msg="Expected two solutions for equation %s!" % eq)
        for x in sol:
            self.assertAlmostEqual(a*x**2 + b*x + c, 0, places=4, msg="%f is not a solution for equation %s!" % (x, eq))

if __name__ == '__main__':
    unittest.main()
