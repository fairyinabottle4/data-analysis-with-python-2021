#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    charts = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    a = charts.groupby("Publisher")
    b = a.sum()["WoC"]
    c = b.sort_values(ascending=False)
    top = c.index[0]
    singles = charts[charts["Publisher"] == top]
    return singles

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
