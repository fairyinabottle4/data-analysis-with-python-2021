#!/usr/bin/env python3

import numpy as np
import pandas as pd

features=5
samples=1000

X=np.random.rand(samples, features)*100

b=np.array([3, -1, 7, 0, -20])

y=np.sum(X*b, axis=1)

print(X.shape, y.shape)
m=np.hstack([X, y[:,np.newaxis]])
df=pd.DataFrame(m)
df.columns = "X1 X2 X3 X4 X5 Y".split()
df.to_csv("mystery_data.tsv", index=False, sep='\t')

