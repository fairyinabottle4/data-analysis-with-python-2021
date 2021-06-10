#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(x,y)
    a = model.score(x, y)
    to_add = [a]
    for column in df.columns:
        r = df.loc[:, column]
        r = r.values.reshape(-1,1)
        model.fit(r,y)
        s = model.score(r, y)
        to_add.append(s)
    return to_add    

def main():
    lst = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {lst[0]}")
    print(f"R2-score with feature(s) X1: {lst[1]}")
    print(f"R2-score with feature(s) X2: {lst[2]}")
    print(f"R2-score with feature(s) X3: {lst[3]}")
    print(f"R2-score with feature(s) X4: {lst[4]}")
    print(f"R2-score with feature(s) X5: {lst[5]}")


if __name__ == "__main__":
    main()
