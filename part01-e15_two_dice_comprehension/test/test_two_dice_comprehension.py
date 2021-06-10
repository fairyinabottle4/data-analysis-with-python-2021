#!/usr/bin/env python3

import re
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.two_dice_comprehension"
main = load(module_name, "main")

@points('p01-15.1')
class TwoDice(unittest.TestCase):


    def test_lines(self):
        main()
        result = get_stdout().split('\n')
        self.assertEqual(len(result), 4, msg="Output should contain four lines!")

    def test_content(self):
        main()
        result = get_stdout().split('\n')
        pattern = r'\((\d),\s*(\d)\)'
        s = set()
        for line in result:
            self.assertRegex(line, pattern, msg="Line %s did not contain a pair of numbers!" % line)
            m = re.match(pattern, line)
            a = int(m.group(1))
            b = int(m.group(2))
            self.assertEqual(a+b, 5)
            self.assertTrue(a in range(1,7), msg="The value of a dice should be between 1 and 6!")
            self.assertTrue(b in range(1,7), msg="The value of a dice should be between 1 and 6!")
            s.add((a,b))
        self.assertEqual(len(s), 4, msg="Output should contain four pairs!")


if __name__ == '__main__':
    unittest.main()

