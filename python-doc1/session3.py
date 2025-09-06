#Thao tác với hàm
def announcer_hello(name_customer, pass_system):
    print(f"Welcome {name_customer} to our Banking")
    print(f"Your password is: {pass_system}. To log in our system")

name_customer = input("What is your name? ")
pass_system = int(input("Enter your password: "))
announcer_hello(name_customer, pass_system)

def customer_data(place, country, city):
    print(f"""Please write down your basic information
                Place of living: {place}
                Country of living: {country}
                City of Living: {city}""")

place = input("Enter your place: ")
country = input("Enter your country: ")
city = input("Enter your city: ")
customer_data(place,country,city)

#Return trong hàm
def add(a,b):
    return a + b

result = add(4,6)
print(result)