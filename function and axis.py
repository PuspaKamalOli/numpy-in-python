import numpy as np
import pandas as pd
import matplotlib as plt

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# sum of all elements
print(x.sum())

# sum of row
print(x.sum(axis=1))
# mean of each elements
print(x.mean())
# mean of columns
print(x.mean(axis=0))
# standard deviation
print(x.std())
# variants
print(x.var())
