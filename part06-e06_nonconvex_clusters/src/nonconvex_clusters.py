#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df[["X1", "X2"]]
    y = df["y"]
    vals = np.arange(0.05, 0.2, 0.05)
    results =[]
    for val in vals:
        model = DBSCAN(val)
        model.fit(X)
        clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        idx = model.labels_ == -1
        outliers = np.count_nonzero(model.labels_ == -1)
        # outliers = np.sum(idx) (both methods of counting outliers and clusters work)
        # clusters = max(model.labels_) + 1
        if clusters == len(y.unique()):
            permutation = find_permutation(clusters, y, model.labels_)
            new_labels = [ permutation[label] for label in model.labels_[~idx]]
            score = accuracy_score(y[~idx], new_labels)
        else: 
            score = np.nan    
        results.append([val, score, clusters, outliers])

    return pd.DataFrame(data=results, columns=["eps", "Score", "Clusters", "Outliers"], dtype="float64")

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
