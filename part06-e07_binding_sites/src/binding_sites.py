#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from scipy.spatial.kdtree import distance_matrix
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def toint(x):
    if (x == 'A'):
        return 0
    elif (x == 'C'):
        return 1
    elif (x == 'G'):
        return 2
    elif (x == 'T'):
        return 3
    else:
        return 10

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    X = df["X"]
    y = df["y"]
    y = y.to_numpy()
    # X = X.to_numpy() (is there a way to vectorize this operation?)
    mat = []
    for seq in X:
        seq_arr = []
        for char in seq:
            seq_arr.append(toint(char))
        mat.append(seq_arr)    
    return (np.array(mat), y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distance = pairwise_distances(X, metric='hamming')
    model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    model.fit_predict(distance)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score


def main():
    # print(get_features_and_labels('src/data.seq'))
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
