#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    snow = df["Snow depth (cm)"]
    max_snow = snow.max()
    print(max_snow)
    return max_snow

def main():
    result = snow_depth()
    print(f"Max snow depth: {result}")

if __name__ == "__main__":
    main()
