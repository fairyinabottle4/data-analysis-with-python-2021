#!/usr/bin/env python3

from os import remove
import numpy as np
#import scipy.linalg

def vector_lengths(a):
    b = np.square(a)
    c = np.sum(b, axis=1)
    d = np.sqrt(c)
    return d

def main():
    a = np.array([[5, 1, 3, 3, 7],
        [9, 3, 5, 2, 4],
        [7, 6, 8, 8, 1],
        [6, 7, 7, 8, 1]])

    result = vector_lengths(a)
    print(result)

if __name__ == "__main__":
    main()
