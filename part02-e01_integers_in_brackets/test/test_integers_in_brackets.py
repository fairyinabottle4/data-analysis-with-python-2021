#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.integers_in_brackets"
integers_in_brackets = load(module_name, "integers_in_brackets")

@points('p02-01.1')
class IntegersInBrackets(unittest.TestCase):

    
    def test_first(self):
        s="  afd [asd] [12 ] [a34]  [\t -43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [12, -43, 12], msg="Incorrect result for string %s!" % s)

    def test_second(self):
        s="  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [47, 12], msg="Incorrect result for string %s!" % s)

    def test_empty(self):
        result = integers_in_brackets("")
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [],
                         msg="Incorrect result for an empty string!")

if __name__ == '__main__':
    unittest.main()
    
