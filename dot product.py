import numpy as np


def dot_product():
    a_1 = np.array([2, 3, 1, 6, 9])
    a_2 = np.array([29, 56, 34, 5, 6])
    print('dot product is : ',end='')
    return np.dot(a_1, a_2)


print(dot_product())
