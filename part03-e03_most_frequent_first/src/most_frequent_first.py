#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    col = a[:,c]
    unique_object = np.unique(col, axis = 0, return_counts=True)
    #unique_values is the sorted array
    #unique_count is the occurence of each value
    unique_values,unique_count = unique_object
    #sort the indices in an ascending order
    ascending_indices = np.argsort(-unique_count)
    sorted_values = unique_values[ascending_indices].reshape((1,-1))
    #get array of indexes of the sorted array
    indxs = np.concatenate([np.where((col == x))[0] for x in np.nditer(sorted_values)])
    return a[indxs]


def main():
    pass

if __name__ == "__main__":
    main()
