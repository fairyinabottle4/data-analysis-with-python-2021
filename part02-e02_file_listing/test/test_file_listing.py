#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import re
from tmc import points

from tmc.utils import load, get_stdout, patch_helper

module_name="src.file_listing"
file_listing = load(module_name, "file_listing")
ph = patch_helper(module_name)

@points('p02-02.1')
class FileListing(unittest.TestCase):


    def test_size(self):
        result=file_listing()
        self.assertIsInstance(result, list, f"file_listing should return a list. Got {type(result)}.")
        self.assertEqual(len(result), 47, msg="The returned list should contain 47 tuples!")

        for t in result:
            self.assertIsInstance(t, tuple, f"All entries in the return list should be tuples. {t} is of type {type(t)}.")
            self.assertEqual(len(t), 6, msg="Each tuple should have six elements!")

    def test_content(self):
        result=file_listing()
        self.assertIsInstance(result, list, f"file_listing should return a list. Got {type(result)}.")
        for t in result:
            self.assertIsInstance(t, tuple, f"All entries in the return list should be tuples. {t} is of type {type(t)}.")
            self.assertIsInstance(t[0], int, msg="size has wrong type!")
            self.assertIsInstance(t[1], str, msg="month has wrong type!")
            self.assertIsInstance(t[2], int, msg="day has wrong type!")
            self.assertIsInstance(t[3], int, msg="hour has wrong type!")
            self.assertIsInstance(t[4], int, msg="minute has wrong type!")
            self.assertIsInstance(t[5], str, msg="filename has wrong type!")

            months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
            self.assertIn(t[1], months, msg="Incorrect month!")

            self.assertIn(t[2], range(1,32),
                          msg="The day should be between 1 and 31 for tuple %s!" % (t,))
            self.assertIn(t[3], range(0,24),
                          msg="The hour should be between 0 and 23 for tuple %s!" % (t,))
            self.assertIn(t[4], range(0,60),
                          msg="The minutes should be between 0 and 59 for tuple %s!" % (t,))

    def test_names(self):
        result = file_listing()
        self.assertIsInstance(result, list, f"file_listing should return a list. Got {type(result)}.")
        names = {t[-1] for t in result}
        self.assertTrue(names.issuperset({'example_figure.py', 'exception_hierarchy.pdf',
            'exception_hierarchy.png', 'exception_hierarchy.svg', 'extra.ipynb', 'face.png',
            'generate_contents.py', '.git', '.gitignore'}))


    def test_called(self):
        with patch('builtins.open', side_effect=open) as o,\
             patch(ph('re.compile'), side_effect=re.compile) as c,\
             patch(ph('re.match'), side_effect=re.match) as m,\
             patch(ph('re.fullmatch'), side_effect=re.fullmatch) as fm,\
             patch(ph('re.search'), side_effect=re.search) as s,\
             patch(ph('re.findall'), side_effect=re.findall) as fa,\
             patch(ph('re.finditer'), side_effect=re.finditer) as fi:
            result=file_listing()
            o.assert_called()
            self.assertTrue(c.called or m.called or fm.called or s.called or fa.called or fi.called,
                            msg="Expected that one of the following was called: "
                            "re.match, re.fullmatch, re.search, re.findall, re.finditer!")


if __name__ == '__main__':
    unittest.main()

