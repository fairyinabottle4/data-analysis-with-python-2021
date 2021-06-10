#!/usr/bin/env python3

from numpy.core.numeric import identity
import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    presidents = df["President"]
    a = presidents.str.split(',')
    b = a.map(lambda x: x[::-1])
    c = b.map(lambda x: " ".join(x))
    d = c.str.strip()
    df["President"] = d
    vp = df["Vice-president"]
    e = vp.str.split(',')
    f = e.map(lambda x: x[::-1])
    g = f.map(lambda x: " ".join(x))
    h = g.str.strip()
    i = h.str.title()
    df["Vice-president"] = i
    start = df["Start"]
    j = start.map(lambda x: x.split()[0])
    j = j.map(int)
    df["Start"] = j
    k = df["Seasons"]
    l = k.map(lambda x: 2 if x == 'two' else int(x))
    df["Seasons"] = l
    last = df["Last"]
    m = last.map(lambda x: np.nan if x == '-' else float(x))
    df['Last'] = m
    types = {'President': object, "Start": int, "Last": float, "Seasons": int, "Vice-president": object}
    df.astype(types)
    print(df)
    return df

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
