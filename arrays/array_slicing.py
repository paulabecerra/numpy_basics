#Just as list slicing is used in Python, we can use it in Numpy. To determine
#from where util where the slice goes we use (:) the colon character.

#x[start:stop:step]

#If we miss to include any of these argunents, the default values will be:
#start=0, stop=size of dimension, step=1.

import numpy as np

#With one-dimensional arrays:
x = np.arange(10)
print(x)

#To get the first five elements:
print(x[:5])

#To get the last five elements:
print(x[5:])

#To get a specific part of the array:
print(x[4:7])

#To get every other element:
print(x[::2])

#To get every other element starting at index 1:
print(x[1::2])


#Multidimensional subarrays
x1 = np.random.randint(10, size=(3, 4))
print(x1)

#To get two rows and three columns:
print(x1[:2, :3])

#To get all rows and every other column:
print(x1[:3, ::2])

#Subarrays can be reversed together:
print(x1[::-1, ::-1])


#Accesing rows and columns
print(x1[:, 1])

print(x1[0, :])
