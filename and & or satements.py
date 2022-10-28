# and statement

age = int(input("Enter your age: "))
can_learn_programing = 0 < age < 150
print(f"You can learn programming: {can_learn_programing}.")

# or statement
age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65
print(f"at {age}, You are usually not working: {usually_not_working}.")

# bool() Function
print(bool(0))  # False
print(bool("Zex"))  # True

# Examples to use Booleans

name = input("Enter you name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}."
print(greeting)
"""
if we are going to write something in here you should know better than anyone that it's only testing things.
so be carefully using these codes because it may harm your files in bad ways.
again be careful 
"""