# methods with multidimensional np_array
import numpy as np

np_array = np.array([[1, 2], [4, 5]])
print(np_array)

# gives inverse of matrix
print(np.linalg.inv(np_array))

# determinants of matrix
print(np.linalg.det(np_array))

# diagonal of matrix
print(np.diag(np_array))

# transpose matrix
print(np_array.T)
