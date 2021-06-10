#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

module_name="src.acronyms"
acronyms = load(module_name, "acronyms")

@points('p01-18.1')
class Acronyms(unittest.TestCase):

    
    def test_first(self):
        result = acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU.""")
        self.assertIsInstance(result, list, f"acronyms should return a list. Got {type(result)}")
        self.assertEqual(result, ['EU', 'GDPR', 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6', '3AU'])

    def test_empty(self):
        result = acronyms("")
        self.assertIsInstance(result, list, f"acronyms should return a list. Got {type(result)}")
        self.assertEqual(result, [], msg="Empty list expected for empty input string!")
        
if __name__ == '__main__':
    unittest.main()
    
