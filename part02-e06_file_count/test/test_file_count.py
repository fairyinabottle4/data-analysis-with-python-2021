#!/usr/bin/env python3

import sys
import unittest
from unittest.mock import patch
from itertools import repeat

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.file_count"
file_count = load(module_name, "file_count")
main = load(module_name, "main")

class FileCount(unittest.TestCase):

    @points('p02-06.1')
    def test_first(self):
        l, w, c = file_count("src/test.txt")
        self.assertEqual(l, 8, msg="Wrong number of lines for file 'test.txt'!")
        self.assertEqual(w, 105, msg="Wrong number of words for file 'test.txt'!")
        self.assertEqual(c, 647, msg="Wrong number of characters for file 'test.txt'!")

    @points('p02-06.1')
    def test_calls(self):
        with patch('builtins.open', side_effect=open) as o:
            file_count("src/test.txt")
            o.assert_called_once()


    @points('p02-06.2')
    def test_main(self):
        orig_argv = sys.argv
        n = 7
        sys.argv[1:] = ["file%i" % i for i in range(n)]
        with patch('src.file_count.file_count', side_effect=repeat((0,0,0))) as fc:
            main()
            self.assertEqual(fc.call_count, n,
                             msg="Wrong number of calls to function 'file_count' for %i command line parameters!" % n)
        result = get_stdout().split('\n')
        for i, line in enumerate(result):
            self.assertEqual(line.strip(), "0\t0\t0\tfile%i" % i,
                             msg="Wrong result on line %i!" % i)
        sys.argv = orig_argv

if __name__ == '__main__':
    unittest.main()

