#!/usr/bin/env python3

from os import sep
import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', sep="\t")
    shape = df.shape
    print(f"Shape: {shape[0]}, {shape[1]}")
    columns = df.columns
    for i in range(len(columns)):
        if i == 0:
            print("Columns:")
            print(columns[i])
        else:
            print(columns[i])    


if __name__ == "__main__":
    main()
