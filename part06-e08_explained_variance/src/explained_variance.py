#!/usr/bin/env python3

from math import exp
from numpy.core.fromnumeric import cumsum
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    variance = df.var(axis=0)
    pca = PCA()
    pca.fit(df)
    exp_variance = pca.explained_variance_
    return variance, exp_variance

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    v_str_list = " ".join([f"{x:.3f}" for x in v])
    ev_str_list = " ".join([f"{x:.3f}" for x in ev])

    print(f"The variances are: {v_str_list}")
    print(f"The explained variances after PCA are: {ev_str_list}")
    cum_sum = np.cumsum(ev)
    num_terms = len(cum_sum)
    plt.plot(np.arange(1, 1+num_terms), cum_sum)
    plt.show()

if __name__ == "__main__":
    main()
