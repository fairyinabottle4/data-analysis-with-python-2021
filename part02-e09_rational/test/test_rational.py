#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.rational"
Rational = load(module_name, "Rational")

@points('p02-09.1')
class RationalTest(unittest.TestCase):

    
    def test_print(self):
        r1=Rational(1,4)
        print(r1)
        pattern = r'<src\.rational\.Rational object at 0x[0-9a-f]+>'
        message = "The rational object is not printable: define '__str__' method!"
        result = get_stdout().split('\n')
        self.assertEqual(len(result), 1, msg="Expected one line of output!")
        self.assertNotRegex(result[0], pattern, msg = message)
        self.assertIn("1", result[0], msg = message)
        self.assertIn("4", result[0], msg = message)
        #self.assertEqual(, "")

    def test_proddiv(self):
        r1=Rational(1,4)
        r2=Rational(2,3)
        self.assertEqual(r1*r2, Rational(2,12), msg="Incorrect result for operation %s * %s!" % (r1,r2))
        self.assertEqual(r1/r2, Rational(3,8), msg="Incorrect result for operation %s / %s!" % (r1,r2))

    def test_plusminus(self):
        r1=Rational(1,4)
        r2=Rational(2,3)
        self.assertEqual(r1+r2, Rational(11,12), msg="Incorrect result for operation %s + %s!" % (r1,r2))
        self.assertEqual(r1-r2, Rational(-5,12), msg="Incorrect result for operation %s - %s!" % (r1,r2))

    def test_comparison(self):
        r1=Rational(1,4)
        r2=Rational(2,3)
        self.assertEqual(r1==r2, False, msg="Incorrect result for operation %s == %s!" % (r1,r2))
        self.assertEqual(r1<r2, True, msg="Incorrect result for operation %s < %s!" % (r1,r2))
        self.assertEqual(r1>r2, False, msg="Incorrect result for operation %s > %s!" % (r1,r2))


    
if __name__ == '__main__':
    unittest.main()
    
