#!/usr/bin/env python3

import unittest


from tmc import points

from tmc.utils import load, get_stdout

module_name="src.hello_world"
main = load(module_name, "main")

@points('p01-01.1')
class HelloWorld(unittest.TestCase):

    
    def test_first(self):
        main()
        self.assertEqual(get_stdout(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()
    
