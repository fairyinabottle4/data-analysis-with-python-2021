#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', index_col=0)
    subset = df.iloc[0:10, [1,2]]
    print(pd.DataFrame(subset))
    return pd.DataFrame(subset)

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()
