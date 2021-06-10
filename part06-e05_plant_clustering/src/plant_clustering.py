#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    data = load_iris()
    X, y = data.data, data.target
    print(X)
    model = KMeans(3, random_state=0)
    model.fit(X)
    permutation = find_permutation(3, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
