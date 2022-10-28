# #  # So far we've been using functions such as `print`, `len`, and `zip`.
# # # But we haven't learned how to create our own functions, or even how they really work.
# #
# # # Let's create our own function. The building blocks are:
# # # def
# # # the name
# # # brackets
# # # colon
# # # any code you want, but it must be indented if you want it to run as part of the function.
# #
# #
# # # def greet():
# # #     name = input("Enter your name: ")
# # #     print(f"Hello, {name}!")
# #
# #
# # # Running this does nothing, because although we have defined a function, we haven't executed it.
# # # We must execute the function in order for its contents to run.
# #
# # # greet()
# #
# # # You can put as much or as little code as you want inside a function, but prefer shorter functions to longer ones.
# # # You'll usually be putting code that you want to reuse inside functions.
# #
# # # Any variables declared inside the function are not accessible outside it.
# # # print(name)  # ERROR!
# #
# #
# # # Imagine you've got some code that calculates the fuel efficiency of a car:
# #
# # # car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}
# # #
# # # mpg = car["mileage"] / car["fuel_consumed"]
# # # name = f"{car['make']} {car['model']}"
# # # print(f"{name} does {mpg} miles per gallon.")
# #
# # # You could put this in a function:
# #
# #
# # # def calculate_mpg():
# # #     car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}
# # #
# # #     mpg = car["mileage"] / car["fuel_consumed"]
# # #     name = f"{car['make']} {car['model']}"
# # #     print(f"{name} does {mpg} miles per gallon.")
# # #
# # #
# # # calculate_mpg()
# #
# # # But this is not a very reusable function since it only calculates the mpg of a single car.
# # # What if we made it calculate the mpg of "any" arbitrary car?
# #
# # car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}
# # #
# # #
# # def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
# #     mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
# #     name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
# #     print(f"{name} does {mpg} miles per gallon.")
# #
# #
# # # calculate_mpg(car)
# #
# # # This means that given a list of cars with the correct data format, we can run the function for all of them!
# #
# # cars = [
# #      {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
# #      {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
# #      {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
# #      {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
# # ]
# #
# # for car in cars:
# #     calculate_mpg(car)
#
# # *********************************************************************************************************
# # 1- Defining our first function:
# # *******************************
# # def get_even_numbers():
# #     Sorted_numbers = []
# #     for y in range(1, 11):
# #         Sorted_numbers.append(y * 2)
# #     print(Sorted_numbers)
# #
# #
# # get_even_numbers()
#
# # Other way:
# # Sorted_numbers = []
# # for y in list(range(2, 21, 2)):
# #     Sorted_numbers.append(y)
# # print(Sorted_numbers)
#
#
# # *********************************************************************************************************
# # 2- Function parameters and arguments:
# # *************************************
#
# # def get_even_numbers(amount):
# #     Sorted_numbers = []
# #     for y in range(1, amount + 1):
# #         Sorted_numbers.append(y * 2)
# #     print(Sorted_numbers)
# #
# #
# # get_even_numbers(10)
#
#
# # *********************************************************************************************************
# # 3- Specifying multiple parameters:
# # **********************************
#
# # def x_print(user_string, amount):
# #     for x in range(amount):
# #         print(user_string)
# #
# #
# # x_print("Ahmed", 5)
#
#
# # *********************************************************************************************************
# # 4- Keyword arguments:
# # *********************
#
# # def x_print(requested_output, quantity):
# #     for x in range(quantity):
# #         print(requested_output)
# #
# #
# # x_print("Hello", quantity=5)
# # *********************************************************************************************************
# # 4- First class function and lamda function:
# # *******************************************
#
# # def add(a, b):
# #     print(a + b)
# #
# #
# # adder = add
# # print(add)
# # print(adder)
# #
# # Sorted_numbers = [56, 3, 45, 29, 102, 30, 73]
# # highest_number = max(Sorted_numbers)
# # print(highest_number)
# # def average_grades(student):
# #     return student["grade_average"]
#
#
# # students = [
# #     {"name": "Hannah", "grade_average": 83},
# #     {"name": "Charlie", "grade_average": 91},
# #     {"name": "Peter", "grade_average": 85},
# #     {"name": "Rachel", "grade_average": 79},
# #     {"name": "Lauren", "grade_average": 92}
# # ]
# #
# # discoloration = max(students, key=average_grades)
# # print(discoloration)
#
#
# def add(x, y):
#     print(x + y)
#
#
# def subtract(x, y):
#     print(x - y)
#
#
# def multiply(x, y):
#     print(x * y)
#
#
# def divide(x, y):
#     if y == 0:
#         print("You can't divide by 0!")
#     else:
#         print(x / y)
#
# # operations = {
# #     "a": add,
# #     "s": subtract,
# #     "m": multiply,
# #     "d": divide
# # }
# # selected_option = input("""Please select one of the following option:
# # 'a': to add
# # 's': to subtract
# # 'm': to multiply
# # 'd': to divide
# #
# # what would you like to do? """)
# #
# # operation = operations.get(selected_option)
# #
# # if operation:
# #     a = int(input("Please select your y: "))
# #     b = int(input("Please select your second y: "))
# #
# #     operation(a, b)
# # else:
# #     print("invalid value.")
#
#
# # students = [
# #     {"name": "Hannah", "grade_average": 83},
# #     {"name": "Charlie", "grade_average": 91},
# #     {"name": "Peter", "grade_average": 85},
# #     {"name": "Rachel", "grade_average": 79},
# #     {"name": "Lauren", "grade_average": 92}
# # ]
# #
# # discoloration = max(students, key=lambda student: student["grade_average"])
# # print(discoloration)
#
#
#  operations = {
#     "a": lambda a,b: a+b,
#     "s": lambda a,b: a-b,
#     "m": lambda a,b: a*b,
#     "d": divide
# }
# selected_option = input("""Please select one of the following option:
# 'a': to add
# 's': to subtract
# 'm': to multiply
# 'd': to divide
#
# what would you like to do? """)

#
# operation = operations.get(selected_option)
#
# if operation:
#     a = int(input("Please select your y: "))
#     b = int(input("Please select your second y: "))
#
#     operation(a, b)
# else:
#     print("invalid value.")


# **********************************************************
# exercises:
# ***********


def average(student):
    return student["name"]


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

sorted_students = sorted(students, key=lambda student: student["name"])
# print(sorted_students)


exponentiate = lambda base, exponent: base ** exponent
print(exponentiate(2, 4))



