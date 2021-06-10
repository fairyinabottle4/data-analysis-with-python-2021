#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    temp = df[df["Air temperature (degC)"] < 0]
    return len(temp)

def main():
    result = below_zero()
    print(f"Number of days below zero: {result}")
if __name__ == "__main__":
    main()
