#If, elif, else, and some operators
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")

#Các toán tử logic
if (a > b) and (a > c):  #and -> thoả cả 2 điểu kiện
    print("a is the highest number")
if (a == b) or (a == c):    #or -> thoả 1 trong 2 điều kiện
    print("At least 1 value equal to a")

x = 5
print(not(x > 3 and x < 10))    #not -> reverse the result, return False if the result is True

#is, is not, in, not in
c = int(input("Enter a number: "))
d = int(input("Enter another number: "))
if c is d:                          #Returns True if both variables are the same object
    print("Same number")
elif c is not d:                    #Returns False if both variables are the not same object
    print("Different number")

welcome_word = "Welcome to Python"
user_input = input()
if user_input in welcome_word:              #Return True if a sequence with the specified value is present in object
    print("Welcome to Python")
elif user_input not in welcome_word:        #Return False if a sequence with the specified value is not present in object
    print("Check again")
