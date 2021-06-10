#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if (n == 0):
        m = a.shape[0]
        return np.eye(m)
    if n < 0:
         a = np.linalg.inv(a)
         n = -1*n
    gen_ex = (a for x in range(n))
    return reduce(lambda x, y: x@y, gen_ex)       

def main():
    return

if __name__ == "__main__":
    main()
