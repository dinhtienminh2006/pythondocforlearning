#Creating matrices
import numpy as np

data = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(data)
#You can aggregate matrices the same way you aggregated vectors:
print(data.min())
print(data.max())
print(data.sum())

#Once you’ve created your matrices,
#       you can add and multiply them using arithmetic operators if you have two matrices that are the same size.
data2 = np.array([[3,2,6], [3,5,1], [2,8,9]])
sum_1 = data + data2
print(sum_1)

# you can aggregate them across columns or rows using the axis parameter
data3 = np.array([[1, 2], [5, 3], [4, 6]])
print(data.max(axis = 0))       #axis = 0 -> cột
print(data.min(axis = 1))       #axis = 1 -> hàng

#You can do these arithmetic operations on matrices of different sizes
# but only if one matrix has only one column or one row
# In this case, NumPy will use its broadcast rules for the operation. (tự động mở rộng size để cho cả hai array = nhau)
data4 = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data4 + ones_row)

#the random.Generator class for random number generation for that
rng = np.random.default_rng()  # the simplest way to generate random numbers
print(rng.random(4))
y = np.random.random(10)
print(y)        #Pick random number
#You can generate a 2 x 4 array of random integers between 0 and 4 with:
print(rng.integers(5, size =(2,4)))
