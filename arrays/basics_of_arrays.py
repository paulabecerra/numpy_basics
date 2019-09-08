#This file shows different examples of Numpy array manipulation. How to access
#data and subarrays, split, reshape and join arrays.
#It's important to get to know them well.

#NumPy Array Attributes

import numpy as np

#One-dimensional array
x1 = np.random.randint(10, size=6)
print(x1)

#Two-dimensional array:
x2 = np.random.randint(10, size=(3,4))
print(x2)

#Three-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))
print(x3)
