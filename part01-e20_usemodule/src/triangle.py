#!/usr/bin/env python
__doc__ = "This module provides basic operations for triangles."
from math import sqrt

__author__ = "Keith Low"
__version__ = "1.0"

def hypothenuse(b, h):
    '''Returns the length of the hypothenuse given the breadth and height 
    of the triangle. This can be found by square rooting the sum of the sqaures of the 
    breadth and height.'''
    return sqrt(b**2 + h**2)


def area(b, h):
    '''Returns the area of the triangle. This can be found by halving the 
    product of the base and height of the triangle.'''
    return 0.5 * b * h    