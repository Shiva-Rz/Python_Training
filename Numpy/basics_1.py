# import numpy as np

# array = np.array([1, 3, 4, 5, 6])
# print(array)
# print(type(array))

# print(np.__version__)

import numpy as np

array_1 = np.array([11, 3, 5, 16, 8, 12, 2])

value = np.searchsorted(array_1, [0, 1, 10, 4]) # [16, 12, 11, 8, 5, 3, 2] 
# [16, 12, 11, 10, 8, 5, 4, 3, 2, 1, 0]
print(value)

# 2, 3, 5, 8, 11, 12, 16