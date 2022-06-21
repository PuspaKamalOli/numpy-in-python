import numpy as np

# 2x3 matrix of zeros only
print(np.zeros((2, 3)))

# 3x3 matrix of ones only
print(np.ones((3, 3)))

# identity matrix of 2x2
print(np.eye(2, 2))
# 2x2 matrix of 8 only
print(np.full((2, 2), 8))
# creates an array of 6 elements from  0 and 9 with equal interval
print(np.linspace(0, 10, 6))
