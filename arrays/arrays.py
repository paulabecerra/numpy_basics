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

#Creating Arrays from Scratch
#Create a length-10 integer array filled with zeros
G = np.zeros(10, dtype=int)
print(G)

#Create a 3x5 array filled with 3.14
H = np.full((3, 5), 3.14)
print(H)

#Create an array filled with a linear sequence starting at 0, ending at 20,
#stepping by 2 (this is similar to the built-in range() function)
I = np.arange(0, 20, 2)
print(I)

#Create an array of five values evenly spaced between 0 and 1
J = np.linspace(0, 1, 5)
print(J)

#Create a 3x3 array of uniformily distributed random values between 0 and 1
K = np.random.random((3, 3))
print(K)

#Create a 3x3 array of normally distributed random values with mean 0 and
#standard deviation 1:
L = np.random.normal(0, 1, (3, 3))
print(L)

#Create a 3x3 array of random integers in the interval [0, 10]:
M = np.random.randint(0, 10, (3, 3))
print(M)

#Create a 3x3 identity matrix
N = np.eye(3)
print(N)
