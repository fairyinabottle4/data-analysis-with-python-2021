#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    to_add = []
    for row in a:
        to_add.append(np.array(row))
    return to_add    

def get_columns(a):
    to_add = []
    b = a.T
    for row in b:
        to_add.append(np.array(row))

    return to_add    

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
