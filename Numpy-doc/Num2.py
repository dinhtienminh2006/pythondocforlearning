#Adding, removing, sorting elements
import numpy as np

arr = np.array([10,5,6,3,1,2])
print(np.sort(arr))

#argsort, which is an indirect sort along a specified axis,
arr2 = np.array([1,2,3])        #Default axis is -1(the last axis)
print(np.argsort(arr2))

x = np.array([[1,2,3], [4,5,6]])
y = np.argsort(x, axis=1)       #Sorts along first axis(down)
print(y)
z = np.take_along_axis(x,y,axis=1)
print(z)

#lexsort, which is an indirect stable sort on multiple keys,
#key là mảng cùng chiều, sắp xếp theo thứ tự từ trái sang phải nhưng key cuối cùng được ưu tiên.
surnames = ["Dinh", "Nguyen", "Dinh"]
firstnames = ["Minh", "Tu", "Anh"]
data = np.lexsort((surnames, firstnames))
print(data)
for i in data:
    print(surnames[i], firstnames[i])

list_data1 = [1, 5, 1, 4, 3, 4, 4]
list_data2 = [9, 4, 0, 4, 0, 2, 1]
data_2 = np.lexsort((list_data2, list_data1))
print(data_2)
for i in data_2:
    print(list_data1[i], list_data2[i])

x2 = [[1, 2, 3, 4],
     [4, 3, 2, 1],
     [2, 1, 4, 3]]
y2 = [[2, 2, 1, 1],
     [1, 2, 1, 2],
     [1, 1, 2, 1]]
z2 = np.lexsort((x2, y2), axis=1)
print(z2)

#searchsorted, which will find elements in a sorted array
#returned index i satisfies
#       left:    a[i-1] < v <= a[i]
#       right:   a[i-1] <= v < a[i]
test_1 = np.searchsorted([11,12,13,14,15,16], 13)
print(test_1)
test_2 = np.searchsorted([11,12,13,14,15,16], 14, side='right')
print(test_2)


