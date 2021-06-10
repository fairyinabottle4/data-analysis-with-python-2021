#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.word_frequencies"
word_frequencies = load(module_name, "word_frequencies")

@points('p02-04.1')
class WordFrequencies(unittest.TestCase):

    def test_first(self):
        d = word_frequencies("src/alice.txt")
        self.assertEqual(d['creating'], 3, msg="Incorrect count for word 'creating'!")
        self.assertEqual(d['Carroll'], 3, msg="Incorrect count for word 'Carroll'!")
        self.assertEqual(d['sleepy'], 2, msg="Incorrect count for word 'sleepy'!")
        self.assertEqual(d['Rabbit'], 28, msg="Incorrect count for word 'Rabbit'!")

        self.assertEqual(len(d), 2424, msg="Wrong number of words in the dictionary!")

    def test_calls(self):
        with patch('builtins.open', wraps=open) as o:
            d = word_frequencies("src/alice.txt")
            o.assert_called()

if __name__ == '__main__':
    unittest.main()

