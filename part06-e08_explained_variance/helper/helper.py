#!/usr/bin/env python3

import numpy as np
import pandas as pd

rng=np.random.RandomState(0)
X=rng.randn(3,400)
p=rng.rand(10,3)  # Random projection into 10d
X=np.dot(p, X)
print(X)

df=pd.DataFrame(X.T)
df.columns = [ "X%i" % i for i in range(1,11) ]

print(df.head())

df.to_csv("data.tsv", sep="\t", index=None)
