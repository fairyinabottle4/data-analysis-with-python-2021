#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    #what you need to do here as in the previous question is to compare
    #two sub matrices directly and let the function do the work for you as compared
    #to the traditional core python method of using a loop
    m = int(a.shape[1] / 2)
    b = a[:,:m]
    c = a[:,m:]
    d = np.sum(b,axis=1) > np.sum(c,axis=1)
    return np.array(a[d])

def main():
    a = np.array([[1, 3, 4, 2],
                [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
