#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    values = s.values
    indices = s.index
    return pd.Series(indices, index=values)

def main():
    result = inverse_series(pd.Series([1,2,2,3], index=['a', 'b', 'c', 'd']))
    print(result)

if __name__ == "__main__":
    main()
