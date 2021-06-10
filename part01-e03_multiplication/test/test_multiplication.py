#!/usr/bin/env python3

import unittest


from tmc import points

from tmc.utils import load, get_stdout

import re

module_name="src.multiplication"
main = load(module_name, "main")

@points('p01-03.1')
class Multiplication(unittest.TestCase):

    
    def test_lines(self):
        main()
        result = get_stdout()
        lines = result.split('\n')
        self.assertEqual(len(lines), 11, msg="The output must contain 11 lines")

    def test_content(self):
        main()
        result = get_stdout()
        lines = result.split('\n')
        for i, line in enumerate(lines):
            self.assertTrue(line.startswith("4 multiplied by %i is" % i))
            m = re.search("4 multiplied by %i is (.*)" % i, line)
            x = m.group(1)
            self.assertEqual(x, str(4*i), msg="4*%i is not %s" % (i, x))

if __name__ == '__main__':
    unittest.main()
    
