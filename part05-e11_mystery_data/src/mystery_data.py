#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    model = LinearRegression(fit_intercept=False)
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    Y = df["Y"]
    #you need to think of them as one giant system of linear equations
    #hence all the X values go together
    X = df.loc[:, "X1": "X5"]
    model.fit(X, Y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f"Coefficient of X1 is {coefficients[0]}")
    print(f"Coefficient of X2 is {coefficients[1]}")
    print(f"Coefficient of X3 is {coefficients[2]}")
    print(f"Coefficient of X4 is {coefficients[3]}")
    print(f"Coefficient of X5 is {coefficients[4]}")
    
if __name__ == "__main__":
    main()
