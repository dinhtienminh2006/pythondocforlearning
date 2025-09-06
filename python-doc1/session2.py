#List
students = ["A", "B", "C", "D", "E", "F"]
print(students[1:4])    #Không bao gồm phần tử cuối

#Hàm thao tác với List
student_names = ['Nguyen', 'Hung', 'Trung', 'Minh', 'Linh']
math_scores = [10,9,8,7,6]

student_names.extend(math_scores)       #Nối 2 list lại với nhau
student_names.append("Phong")           #Thêm các phân tữ riêng biệt vào cuối danh sách
student_names.insert(3, "Tuyết")       #Chèn phần tử vào list nơi bạn muốn   ( index_number, object)
student_names.pop()                     #Loại bỏ phần tử cuối cùng nếu không có index(remove specified index)
student_names.clear()                   #Empties the list, the list still there but has no content
print(student_names.count("Trung"))     #Đếm số phần tử
print(student_names)

math_scores.sort()                      #Sắp xếp theo thứ tự tăng dần

math_scores.sort(reverse = True)        #Sắp xếp theo thứ tự giảm dần
math_scores.reverse()                   #Lật ngược lại

#del student_names
#del math_scores
for x in math_scores:
    print(x)
[print(x) for x in student_names]       #Short way to write

for i in range(len(student_names)):     #Dùng hàm for để print index
    print(student_names[i])

y = 0
while y < len(student_names):
    print(student_names[y])
    y += 1

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]       #Syntax: [expression for item in iterable if condition == True]
print(newlist)

#Sort Lists
def myfunc(n):
    return abs(n - 50)

z = [100, 50, 65, 82, 23]
z.sort(key = myfunc)
print(z)

a1 = [1,2,3,4,5]
a2 = a1.copy()      #Copy the list
print(a2)

#Tuple
#Chúng ta không thể thay đổi các phân tử trong tuple. Vì nó immutable, not support item assignment
coordinates = (60, 150)
coordinates_2 = [(60,120), (1,5), (45, 60)]         #Sử dụng List để tạo danh sách các Tuple
print(coordinates_2[0])

#Tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))                   #use len to print out the element in a tuple
#To create a tuple with only one item, you have to add a comma after the item
tuple1 = ("apple",)
print(type(tuple1))         #Return tuple type


#LIST [], TUPLE ()
#LIST CÓ THE THAY DOI PHAN TU TRONG KHI TUPLE LA NHUNG PHAN TU CO DINH
