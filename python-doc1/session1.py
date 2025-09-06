#Biến và kiểu dữ liêu
#Variable là gì:
#   + Là nơi dùng để lưu trữ dữ liệu
#   + Python không có câu lệnh để khai báo một biến
#   + Một biến sẽ được tạo ra ngay khi bạn gán một giá trị cho nó

character_name = input("What is your name? ")
character_age = int(input("How old are you? "))
print(f"Your name is {character_name} and your age is {character_age}")
# 3 kiểu dữ liệu phổ biến: string, number, boolean

#Thao tác với string
print("Dinh Tien Minh \nSinh Vien DHQT")
print("""DINH TIEN MINH 
HOC CONG NGHE THONG TIN""")         #2 cách xuống dòng

print("DINH TIEN MINH \n\"HOC IT\"")

subject = input("Enter your subject: ")
print("What is this " + subject)

object_name = "THIS IS PYTHON"
print(object_name[6])             #Index bắt đầu từ 0
print(object_name.index("S"))     #Đếm vị trí index
print(object_name.replace("S", "I"))  #Thay đổi index

#Nối chuỗi với hàm format
num = 3
text = "{} Là số môn học mà tôi đã pass"

print(text.format(num))

my_age = 27
my_wife_age = 25
text_2 = "Năm nay tôi {} tuổi. Còn vợ tôi {} tuổi"
print(text_2.format(my_age, my_wife_age))

