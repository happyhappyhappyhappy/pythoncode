import numpy as np

a = np.zeros((2, 3))
print(a)
# [[0, 0, 0],
#  [0, 0, 0]]

a[0][2] = 1
# [[1, 0, 0],
#  [0, 0, 0]]
print(a)
