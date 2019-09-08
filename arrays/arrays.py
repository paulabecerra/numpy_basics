#Fixed-type arrays with Python
import numpy as np
import array
A = list(range(10))
B = array.array('i', A)
print(B)

#Creating Arrays from Python Lists
#Integer arrays:
C = [1,2,3,4,5,6]
D = np.array(C)
print(D)

#If the data used do not have the same type Numpy will upcast if possible:
E = np.array([3.2, 4, 5, 6, 7])
print(E)
#All values in this example are converted to floating values

#Unlike Python, Numpy arrays can be explicitly multidimensional:
#Nested lists result in multidimensional arrays:
F = np.array([range(i, i+3) for i in [2, 4, 6]])
print(F)
