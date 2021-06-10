#!/usr/bin/env python3

from os import sep
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    #sepal length and petal length correspond to index 0 and 2
    sepal_length = data[:,0]
    petal_length = data[:,2]
    result = scipy.stats.pearsonr(sepal_length, petal_length)
    return result[0]

def correlations():
                 #sepal length | sepal width | petal length | petal width
    #sepal length       1      |    -0.118   |   0.871      |     0.817      
    #sepal width    -0.118     |      1      |   -0.428     |    -0.366        
    #petal length    0.871     |    -0.428   |     1        |    0.962       
    #petal width     0.817     |    -0.366   |    0.962     |      1
    # data = load()
    # sepal_length = data[:,0]
    # sepal_width = data[:,1]
    # petal_length = data[:,2]
    # petal_width = data[:,3]
    # row1_b = np.corrcoef(sepal_length, petal_length)[0,1] #0.871
    # row1_c = np.corrcoef(sepal_length, sepal_width)[0,1] #-0.118
    # row1_d = np.corrcoef(sepal_length, petal_width)[0,1] #0.817
    # row2_c = np.corrcoef(sepal_width, petal_length)[0,1] #-0.428
    # row2_d = np.corrcoef(sepal_width, petal_width)[0,1] #-0.366
    # row3_d = np.corrcoef(petal_length, petal_width)[0,1] #0.962
    # mat = np.eye(4)
    # mat[0][1] = row1_c
    # mat[1][0] = row1_c
    # mat[2][0] = row1_b
    # mat[0][2] = row1_b
    # mat[3][0] = row1_d
    # mat[0][3] = row1_d
    # mat[1][2] = row2_c
    # mat[2][1] = row2_c
    # mat[1][3] = row2_d
    # mat[3][1] = row2_d
    # mat[2][3] = row3_d
    # mat[3][2] = row3_d
    data = load()
    sepal_length = data[:,0]
    sepal_width = data[:,1]
    petal_length = data[:,2]
    petal_width = data[:,3]
    return np.corrcoef((sepal_length, sepal_width, petal_length, petal_width))
    #moral of the story is, you can use either method to calculate correlation coefficient
    #but if you want a table, numpy corrcoef is probably the way to go
    #if you just want the individual value, you can use scipy stats pearsonr

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
