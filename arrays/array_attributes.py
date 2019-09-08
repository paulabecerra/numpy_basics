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

#Each array has attributes ndim (the number of dimensions), shape (the size of
#each dimension), size (the total size of the array):

print("x1 ndim: ", x1.ndim)
print("x1 shape: ", x1.shape)
print("x1 size: ", x1.size)

print("x2 ndim: ", x2.ndim)
print("x2 shape: ", x2.shape)
print("x2 size: ", x2.size)

print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)

#We can also access the type of data that the array has:

print("x1 data type: ", x1.dtype)
print("x2 data type: ", x2.dtype)
print("x2 data type: ", x2.dtype)

#With itemsize we cab list the size (in bites) of each array element. nbytes
#lists that total size (in bites) of the array:

print("itemsize: ", x1.itemsize, "bytes")
print("nbytes: ", x1.nbytes, "bytes")
