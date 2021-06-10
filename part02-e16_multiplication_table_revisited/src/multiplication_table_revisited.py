#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    
    a = np.arange(0,n)
    b = a.reshape(n,1)
    a_broadcast, b_broadcast = np.broadcast_arrays(a,b)
    m = a_broadcast * b_broadcast
    return m

def main():
    print(multiplication_table(9))

if __name__ == "__main__":
    main()
