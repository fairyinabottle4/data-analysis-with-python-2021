#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.multiplication_table"
main = load(module_name, "main")

@points('p01-04.1')
class MultiplicationTable(unittest.TestCase):


    def test_lines(self):
        main()
        result = get_stdout().split("\n")
        self.assertEqual(len(result), 10, msg="The output should contain ten lines!")

    def test_content(self):
        main()
        result = get_stdout().split("\n")
        for i, line in enumerate(result):
            j = i + 1
            numbers = list(map(int, line.split()))
            self.assertEqual(numbers, list(range(j, 11*j, j)))

if __name__ == '__main__':
    unittest.main()

