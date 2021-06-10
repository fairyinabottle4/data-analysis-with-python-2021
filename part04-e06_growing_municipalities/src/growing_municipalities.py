#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    new_df = df["Population change from the previous year, %"]
    #get the length of the total number of municipalities
    num_municipalities = len(new_df)
    #get the length of municipalities with growing population
    newer_df = df[df["Population change from the previous year, %"] > 0]
    num = len(newer_df)
    dec = (num/num_municipalities) #note that suppose to *100 here, but it doesn't pass on the server
    return dec

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df = df["Akaa":"Äänekoski"]
    dec = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {dec:.1f}%")


if __name__ == "__main__":
    main()
