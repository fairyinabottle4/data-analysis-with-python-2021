#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    #print the rows where the 2nd column is greater than the 2nd last column
#effectively you are comparing the values of the 2 columns. Don't think in terms
#of loops, instead just think of a way to extract the columns for comparison
# print(a[a[:,1] > a[:,-2]])

#if you compare this, you are comparing only the 2nd row and second last column
# print(a[1] > a[-2])

    condition = a[:,1] > a[:,-2]
    return a[condition]
    
def main():
    pass

if __name__ == "__main__":
    main()
