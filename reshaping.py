import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5]])

# creates array of range 0-7
b = np.arange(0, 8)
print(b)
# creates row matrix
print(b[np.newaxis, :])
# creates column matrix
print(b[:, np.newaxis])
# converts matrix into 3x2
print(a.reshape((3, 2)))
