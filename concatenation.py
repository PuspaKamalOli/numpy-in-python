import numpy as np

a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[7, 8, 9], [10, 11, 12]])
a3 = np.array([1, 2, 3])
a4 = np.array([[1], [2], [3]])

# list all elements of both array
print(np.concatenate((a1, a2), axis=None))

# concatenate vertically
print(np.concatenate((a1, a2)))
print(np.concatenate((a1, a2), axis=0))

# concatenate horizontally
print(np.concatenate((a1, a2), axis=1))

# converts into row matrix
print(np.hstack(a4))
# converts into column matrix
print(np.vstack(a3))
