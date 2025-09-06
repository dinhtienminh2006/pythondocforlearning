#Why use Numpy
#  - Python lists can contain elements of a variety of types, quite fast when used to perform individual operations on a handful of elements.
#  - improve speed, reduce memory consumption
#  - offer a high-level syntax for performing a variety of common processing tasks

# Array: a structure for storing and retrieving data

#Some restriction in Numpy array:
# + All elements of the array must be the same type of data
# + The total size of array cant change once created
# + The shape must be rectangular


import numpy as np
exp1 = np.array([1,2,3,4,5,6,7])  #Python sequence
print(exp1)
print(exp1[0])

#Like the original list, array is mutable(can change variable)
exp2 = np.array([1,2,3,4,5,6,7])
exp2[0] = 3
print(exp2)

#Slicing an array returns a view(an object that refers to the data in the original array)
exp3 = np.array([1,2,3,4,5,6,7,8])
print(exp3[:4])
b = exp3[4:]
b[1] = 20
print(exp3)

#Array attributes: contains the ndim, shape, size, and dtype attributes of an array
exp4 = np.array([1,2,3,4,5,6,7])
print(exp4.ndim)                    #The number of dimensions of an array is contained in the ndim attribute

print(exp4.shape)                   #The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension.
if len(exp4.shape) == exp4.ndim:
    print("True")
else:
    print("False")
