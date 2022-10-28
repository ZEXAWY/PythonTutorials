# If Statement

# friend = "Ahmed"
# user = input("Enter you name: ")
# if user == friend:
#     print(f"Hello, {user}.")
# ************************************************************************************************************
# odds= [1, 3, 5, 7, 9, 11]
# even = [2, 4, 6, 8, 10]
# user= int(input("Enter a y: "))
# if user in odds:
#     print(f"{user}, is Odd.")
# elif user in even:
#     print(f"{user}, is Even.")
# else:
#     print(f"{user}, is out of my range.")
# ************************************************************************************************************
# While loop

# is_learning = True
# while is_learning:
#     print("You r learning.")

# user = input("Are you still learning? (yes/no): ")
# while user == "yes":
#     print("you are learning.")
#     user = input("Are you still learning? (yes/no): ")
#
# print("Stopping the program.")

# x = int(input("enter a y: "))
# while x <= 100:
#     print("myten ahlak.")
#     x = int(input("enter a y: "))
#
# print("nase7 yad.")
# ************************************************************************************************************
# For loop

# friends = ["Ahmed", "Mohamed", "Islam"]
# for friend in friends:
#     print(friend)

# dahab = [
#     {"name": "Ahmed", "grade": 70},
#     {"name": "Mohamed", "grade": 80},
#     {"name": "Islam", "grade": 79},
#     {"name": "Seny", "grade": 69},
# ]
# for member in dahab:
#     name = member["name"]
#     grade = member["grade"]
#
#     print(f"{name}, has score of {grade}.")
# print("program ends.")
# ************************************************************************************************************
# iterating over Dictionaries:

# friends = {"Rolf": 25, "Anne": 26, "Ahmed": 24}
#
# for name,age in friends.items():
#     print(f"{name} is {age} old.")
# ************************************************************************************************************
# Break and Continue:
# cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok", ]
#
# for car in cars:
#     if car == "faulty":
#         print(f"found a {car} car, skipping the faulty car.")
#         break
#     print(f"Car is {car}")
#     print("shipping the new car to customer.")
# else:
#     print("All cars built successfully, no faulty cars.")
# ************************************************************************************************************
# list comprehension

# Sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# doubled_numbers = []
# for y in Sorted_numbers:
#     doubled_numbers.append(y * 2)
#     print(doubled_numbers)
# print(doubled_numbers)
# ************************************************************************************************************
# other way
# Sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# doubled_numbers = [y*2 for y in Sorted_numbers]
# print(doubled_numbers)
# ************************************************************************************************************
# other examples:
# friends_age = [22, 23, 25, 24, 36]
# age_strings = [f"My friends is {age} years old." for age in friends_age]
# print(age_strings)
# ************************************************************************************************************
# friends = ["Ahmed","Islam", "Mohamed"]
# lower = [name.lower() for name in friends]
# print(lower)

# friend = input("Enter your friend name: ")
# friends = ["Ahmed", "Islam", "Mohamed", "Seny"]
# friends_lower = [name.lower() for name in friends]
#
# if friend.lower() in friends_lower:
#     print(f"{friend.title()}, is your friends.")
# else:
#     print(f"{friend.title()}, is not your friend.")
# ************************************************************************************************************
# comprehension with conditionals:

# ages = [23, 24, 14, 27, 44]
# odds = [age for age in ages if age % 2 == 1]
# even = [age for age in ages if age % 2 == 0]

# friends = ["Ahmed", "mohamed", "seny", "Islam"]
# guests = ["Gimy", "Zahran", "Snoopy", "Mohamed", "Ahmed"]
#
# friends_lower = [friend.lower() for friend in friends]
#
# present_friend = [
#     name.title() for name in guests if name.lower() in friends_lower
# ]
#
# print(present_friend)
# ************************************************************************************************************
# friends = ["Ahmed", "Mohamed", "Seny", "Islam"]
# guests = ["Gimy", "Zahran", "Snoopy", "Mohamed", "Ahmed"]
#
# friends_lower = set([n.lower() for n in friends])
# guests_lower = set([n.lower() for n in guests])
#
# present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
# print(present_friends)
# ************************************************************************************************************
# friends = ["Ahmed", "Mohamed", "Seny", "Islam"]
# time_since_seen = [3, 5, 7, 8]
#
# long_timer = {
#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#     if time_since_seen[i] >=4
# }
# print(long_timer)

# time_since_seen = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [
#     time_since_seen[i] * 2 for i in range(len(time_since_seen)) if time_since_seen[i] < 4
# ]
#
# print(y)
# ************************************************************************************************************
# dict and zip functions:
# friends = ["Ahmed", "Mohamed", "Seny", "Islam"]
# time_since_seen = [3, 5, 7, 8]
#
# zip_fun = dict(zip(friends, time_since_seen))
# print(zip_fun)
# for name, time in zip_fun.items():
#     x = name
#     y = time
#     print(f"{x}, has been seen {y} minutes ago.")
# ************************************************************************************************************
# functions:
# cars = [
#     {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
#     {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
#     {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
#     {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
# ]
#
#
# def calculate_mpg(vehicle, intro):
#     print(intro)
#     mpg = vehicle["mileage"] // vehicle["fuel_consumed"]
#     name = f"{vehicle['make']} {vehicle['model']}"
#     print(f"{name} does {mpg}% miles per gallon.")
#
#
# for car in cars:
#     calculate_mpg(car, "Zex New Line: ")
# ************************************************************************************************************
# Function and return value:
# cars = [
#     {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
#     {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
#     {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
#     {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
# ]
#

# def calculate_mpg(car):
#     mpg = car["mileage"] // car["fuel_consumed"]
#     return mpg
#
#
# def car_name(car):
#     name = f"{car['make']} {car['model']}"
#     return name
#
#
# def print_car_info(car):
#     name = car_name(car)
#     mpg = calculate_mpg(car)
#
#     print(f"{name} does {mpg}% miles per gallon.")
#
#
# for vehicle in cars:
#     print_car_info(vehicle)
# ************************************************************************************************************
# return value:
# def divide(x, y):
#     if y == 0:
#         return "Are you idiot? you can't divide by zero."
#     else:
#         return x / y
#
#
# print(divide(60, 15))
# ************************************************************************************************************
# Lambda function
# def divide(x, y):
#     return x / y

# divide = lambda x, y: x / y
# print(divide(10, 5))
# print(divide(13, 6))

# Other way calling lambda function:
# print((lambda x, y: x / y)(15, 3))


# another example:
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
#
# students = [
#     {"name": "Ahmed", "grades": (67, 70, 79, 80, 100)},
#     {"name": "Mohamed", "grades": (90, 94, 87, 90, 97)},
#     {"name": "Islam", "grades": (88, 92, 94, 95, 91)},
#     {"name": "Snoopy", "grades": (40, 70, 56, 67, 88)},
#     {"name": "Seny", "grades": (51, 48, 62, 43, 97)},
# ]
#
# for self in students:
#     print(average(self["grades"]))

# Other way using lambda in the previous example:

# average = lambda sequence: sum(sequence) / len(sequence)
#
# students = [
#     {"name": "Ahmed", "grades": (67, 70, 79, 80, 100)},
#     {"name": "Mohamed", "grades": (90, 94, 87, 90, 97)},
#     {"name": "Islam", "grades": (88, 92, 94, 95, 91)},
#     {"name": "Snoopy", "grades": (40, 70, 56, 67, 88)},
#     {"name": "Seny", "grades": (51, 48, 62, 43, 97)},
# ]
#
# for self in students:
#     print(average(self["grades"]))
# ************************************************************************************************************
# Higher order and first class fun:

# def greet():
#     print("Hello")
#
#
# greet()

# another example showing that:
#
# def before_and_after(fun):
#     print("before")
#     fun()
#     print("after")
#
#
# def greet():
#     print("hello")
#
#
# before_and_after(greet)

# another example :

# ************************************************************************************************************
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum,  # lambda seq: sum(seq)
    "top": max
}

students = [
    {"name": "Ahmed", "grades": (67, 70, 79, 80, 100)},
    {"name": "Mohamed", "grades": (90, 94, 87, 90, 97)},
    {"name": "Islam", "grades": (88, 92, 94, 95, 91)},
    {"name": "Snoopy", "grades": (40, 70, 56, 67, 88)},
    {"name": "Seny", "grades": (51, 48, 62, 43, 97)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    result = operations[operation](grades)
    print(result)
