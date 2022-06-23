# solving linear equations
import numpy as np

# given two equations:
# 2x+3y=40
# 7x+2y=55
# we have to find value of x and y using numpy array:
a_1 = np.array([[2, 3], [7, 2]])
a_2 = np.array([40, 55])
print(np.linalg.solve(a_1, a_2))
# where first element of array is the value of x and second is of y respectively
# eigen values
a_3 = np.array([[1, 2], [4, 5]])
print(np.linalg.eig(a_3))
