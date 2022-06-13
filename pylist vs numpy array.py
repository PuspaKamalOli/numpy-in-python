# pylist vs nplist
import math
import numpy as np

pylist = [1, 2, 3, 4, 5]
nplist = np.array([1, 2, 3, 4, 5])

# appends 4
pylist = pylist + [4]

# add 4 to each elements of arrat
nplist = nplist + [4]
print('pylist: ' + str(pylist) , ', nplist: ' + str(nplist))

# repeats each elements 2 times
pylist_1 = pylist * 2

# multiply each elements by 2
nplist_1 = nplist * 2

print(pylist_1, nplist_1)

# givers squareroot of each elements
nplist_2 = np.sqrt(pylist)
print(nplist_2)

# print(math.sqrt(pylist)):which shows error
