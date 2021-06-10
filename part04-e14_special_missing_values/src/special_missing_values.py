#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df.replace({"New": None, "Re": None}, value=None, inplace=True)
    df.dropna(axis=0, how='any', inplace=True)
    df[["Pos", "LW"]] = df[["Pos", "LW"]].astype('float')    
    remaining = df[df["Pos"] > df["LW"]]
    return remaining

def main():
    special_missing_values()

if __name__ == "__main__":
    main()
