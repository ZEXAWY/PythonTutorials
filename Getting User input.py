# input function always react as str

my_name = "Zex"
your_name = input("Enter your name: ")

print(f"Hello {your_name}, My name is {my_name}.")

# So we had to change the str input to a float or integer, so we can do mathematical operation on it
# like tho following example

age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months")

age = int(input("Enter your age: "))
print(f"You have lived for {age_num * 12} months")

age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months")
