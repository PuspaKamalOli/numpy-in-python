import numpy as np

a_1 = np.array([[1, 2], [3, 4], [4, 9]])
print(a_1)
list_1 = []
list_2 = []
# iterate by row
for i in np.nditer(a_1):
    list_1.append(i)
print(list_1)
# iterate by column
for j in np.nditer(a_1, order='f'):
    list_2.append(j)
print(list_2)
