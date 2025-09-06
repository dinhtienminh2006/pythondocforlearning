#Transpoing and reshaping a matrix
import numpy as np

#You may also need to switch the dimensions of a matrix when a certain input shape is different from your dataset
data = np.array([1, 2, 3, 4, 5 ,6])
print(data.reshape(2 ,3))       #Tạo ra matrix có 2 lists, mỗi list có 3 đơm vị index
print(data.reshape(3, 2))

#You can also use .transpose() to reverse or change the axes of an array according to the values you specify.
data2 = np.arange(6).reshape(2,3)
print(data2.transpose())
print(data2.T)  #Or this way

#Use transpose(a, argsort(axes)) to invert the transposition of tensors when using the axes keyword argument.
a = np.ones((2,3))
b = np.transpose(a, (1,0)).shape        #Vị trí index mới vào index cũ -> 2,3 => 3,2
print(b)
c = np.ones((1,2,3,4,5))
d = np.transpose(c, (1,0,2,3,4)).shape
print(d)

x = np.ones((2, 3, 4, 5))
y = np.transpose(x).shape           #Lật ngược nếu không có axes
print(y)

#How to reverse an array
#Reversing a 1D array
arr1 = np.array([1,2,3,4,5,6,7,8])
reversed_arr1 = np.flip(arr1)
print(reversed_arr1)

#Reversing a 2D array
arr_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr_2 = np.flip(arr_2)
print(reversed_arr_2)

reversed_arr_2_row = np.flip(arr_2, axis = 0)       #Reverse only the row
print(reversed_arr_2_row)

reversed_arr_2_col = np.flip(arr_2, axis = 1)       #Reverse only the column
print(reversed_arr_2_col)

#Reverse the contents of only one column or row
arr_2[1] = np.flip(arr_2[1])
print(arr_2)

arr_2[:, 1] = np.flip(arr_2[:, 1])
print(arr_2)

#Reshaping and flattening multidimensional arrays
#There are two popular ways to flatten an array: .flatten() and .ravel()
#The new array created using ravel() have any changes to the new array will affect the parent array as well

x = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
x_2 = x.flatten()
print(x_2)
print(x)            #The original was not affected

y = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
y_2 = y.ravel()
y_2[2] = 0
print(y)            #The original was affected
print(y_2)
