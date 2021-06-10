#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.prepend"
Prepend = load(module_name, "Prepend")

@points('p02-08.1')
class PrependTest(unittest.TestCase):

    
    def test_first(self):
        p = Prepend("+++ ")
        p.write("Hello")
        p.write("Goodbye")
        result=get_stdout().split('\n')
        self.assertEqual(len(result), 2,
                         msg="Expected two lines of output!")
        self.assertEqual(result[0], "+++ Hello")
        self.assertEqual(result[1], "+++ Goodbye")


if __name__ == '__main__':
    unittest.main()
    
