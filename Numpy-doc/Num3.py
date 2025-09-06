#Indexing and Slicing : use in the same ways you slice Python lists
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,11,13,15])
print(a[a < 4])
five_up = a[a>5]
print(five_up)
five_up_checking = (a>5) | (a==5)   #Kết hợp toán tử logic
print(five_up_checking)

#Use np.nonzero() to select elements or indices from an array
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

c = np.nonzero(b < 5)           #The first array represents the row indices where value are found
print(c)                        #The second array represents the column indices where value are found

def f(x,y):
    return 10 * x + y

d = np.fromfunction(f,(5,4))
print(d)
print(d[2, 3])      #(row, column)
print(d[0:5 , 1])   #Each row in the second column
print(d[:, 1])      #Equivalend to previous example
print(d[1:3, :])    #Each column in the second and third row

#The dots (...) represent as many colons as needed to produce a complete indexing tuple
#   Example:  x[1,2,...] = x[1, 2, :, :, :]

#How to create an array from existing data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array(x[3:5])        #New array from x array
print(y)

#Stack two existing arrays
x1 = np.array([[1, 1],
               [2, 2]])

x2 = np.array([[3, 3],
               [4, 4]])
x3 = np.vstack([x1, x2])        #Vertically
x4 = np.hstack([x1, x2])        #Horiziontally
print(x4, x3)

#Split an array
y1 = np.arange(1, 25).reshape(2, 12)
y2 = np.hsplit(y1, 3)    #split this array into three equally shaped arrays
print(y2)

y3 = np.hsplit(y1, (3, 4))   #If you wanted to split your array after the third and fourth column
print(y3)
