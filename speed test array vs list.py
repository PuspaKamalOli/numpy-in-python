import random
import numpy as np
from timeit import default_timer as timer

start_2 = timer()
py_list = [i for i in range(1, 1000, 10)]
print(py_list)
stop_2 = timer()
time_2 = start_2 - stop_2
print('time taken by py_list:' + str(time_2))

start_1 = timer()
np_array = np.array([i for i in range(1, 1000, 10)])
print(np_array)
stop_1 = timer()
time_1 = start_1 - stop_1
print('time taken by np_list:' + str(time_1))
