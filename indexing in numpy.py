import numpy as np

a_1 = np.array([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
print(a_1)

# all elements of first column
print(a_1[:, 0])

# all elements of first row
print(a_1[0, :])

# elements of index 0 and 1 of row 1
print(a_1[1, 0:2])

# 3rd element of second row
print(a_1[1, 2])

# last element of last element
print(a_1[-1, -1])

# return true and false whether condition is satisfied or not
print(a_1 > 2)

# return elements that satisfy the condition
print(a_1[a_1 < 6])

# return elements that satisfy condition and replace with 8 that do not
print(np.where(a_1 > 5, a_1, 8))

# work as a filter function
even = np.argwhere(a_1 % 2 == 0).flatten()
print(a_1[even])
