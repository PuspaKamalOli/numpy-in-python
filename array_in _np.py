import numpy as np

print(np.__version__)

# array
array = np.array([[1, 2, 3], [3, 8, 5]])

# methods:
# shape of matrix
print(array.shape)

# number of elements
print(array.size)

# data type of each element
print(array.dtype)

# no of dimension
print(array.ndim)

# data type and bit of elements
print(array.itemsize)
