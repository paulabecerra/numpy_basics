#List indexing in Numpy is very similar to list indexing in Python. In a one-dimensional
# array, we can access the ith value (counting from zero) by specifying the
#desired index in square brackets:

import numpy as np

#One-dimensional array
x1 = np.random.randint(10, size=6)
print(x1)

#Three-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))

#To get the 0th index in the array we can use:
print(x1[0])

#It's important to remember that we can access indices from the end using
#negative indexes:
print(x1[-1])

#Multidimensional Arrays:
x2 = np.random.randint(10, size=(3,4))
print(x2)

#In multidimensional arrays, we cabn access items using a comma-separated
#tuple of indices:
#Two-dimensional array:
print(x2[0, 0])
print(x2[1, 1])
print(x2[2, 2])

#Values can also be changed using the same notation:
x2[0, 0] = 12
print(x2)

#It's important to remember that Numpy Arrays have a fixed type.#
