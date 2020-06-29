#Name
name = input('Enter the name: ')

# Age
age = input ("enter your age: ")

#city
city = input("Enter your city: ")

output = "your name is {}.You are {} years old and live in {}"
string = output.format(name,age,city)

print(string)
