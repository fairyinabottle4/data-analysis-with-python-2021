#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    #Find dot product for the numerator
    prod = np.multiply(X,Y)
    dotProduct = np.sum(prod)

    #find the norm of both X and Y
    normX = np.sqrt(np.sum(np.square(X)))
    normY = np.sqrt(np.sum(np.square(Y)))

    #This gives the whole fraction
    fraction = dotProduct/(np.multiply(normX,normY))
    angle = np.arccos(fraction)

    #changing from degrees to radians
    result = angle*180/np.pi
    return np.array(result)





def main():
    A = np.array([[0,1,0], [1,1,0]])
    B = np.array([[0,0,1], [-1,1,0]])
    result = vector_angles(A,B)
    print(result)

if __name__ == "__main__":
    main()
