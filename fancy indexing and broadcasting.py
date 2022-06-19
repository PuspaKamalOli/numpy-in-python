import numpy as np

# fancy indexing
a1 = np.array([2, 60, 80, 4, 6, 8, 2, 90, 10])
l1 = [4, 5, 6, 1, 3]
print(a1[l1])
# broadcasting:add a3 to each element respectively
a3 = np.array([1, 2, 3])
a4 = np.array([[4, 5, 6], [6, 7, 8], [3, 5, 7]])
a5 = [6]
print(a3 + a4)
print(a4 + a5)
