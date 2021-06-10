#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    return (model.coef_[0], model.intercept_)


def main():
    np.random.seed(0)
    n=20  
    x=np.linspace(0, 10, n)
    y=x*2 + 1 + 1*np.random.randn(n) 
    slope, intercept= fit_line(x,y)
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    #for each value of x, plot the value of y where the line will intercept
    abline_values = [slope * i + intercept for i in x]
    plt.plot(x,y, 'x')
    plt.plot(x,abline_values,'b')
    plt.show()

    
if __name__ == "__main__":
    main()
