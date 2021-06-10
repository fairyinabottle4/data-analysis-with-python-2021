#!/usr/bin/env python3

from os import sep
import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',', index_col="country")
    df.drop(["year", "sex", "age"], axis=1, inplace=True)
    df["mean"] = df["suicides_no"] / df["population"]
    df2 = df.groupby("country")
    df3 = df2["mean"].mean()
    print(df3)
    return df3

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
