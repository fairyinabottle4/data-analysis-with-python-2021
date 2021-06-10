#!/usr/bin/env python3

import pandas as pd

def top_bands():
    charts = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    charts["Artist"] = charts["Artist"].str.title()
    bands["Band"] = bands["Band"].str.title()
    merged_list = pd.merge(bands, charts, left_on='Band', right_on='Artist')
    return merged_list

def main():
    top_bands()

if __name__ == "__main__":
    main()
