# while True:
#     try:
#         y = int(input("Please enter a whole y: "))
#         break
#     except ValueError:
#         print("You didn't enter a valid integer!")


# def average(Sorted_numbers):
#     try:
#         mean = math.fsum(Sorted_numbers) / len(Sorted_numbers)
#         print(mean)
#     except ZeroDivisionError:
#         print(0)
#     except TypeError:
#         print("You provided invalid values!")


# def average(Sorted_numbers):
#     try:
#         mean = math.fsum(Sorted_numbers) / len(Sorted_numbers)
#         print(mean)
#     except (ZeroDivisionError, TypeError):
#         print("The average cannot be calculated using the value you provide.")


# def average(Sorted_numbers):
#     try:
#         mean = math.fsum(Sorted_numbers) / len(Sorted_numbers)
#     except ZeroDivisionError:
#         print(0)
#     except TypeError:
#         print("You provided invalid values!")
#     else:
#         print(mean)
#
#
# series_of_numbers = ["saw"]
#
# average(series_of_numbers)

# def finally_flex():
#     try:
#         return
#     finally:
#         print("you return when i say you can return.")
#
#
# finally_flex()


# exercises:
# 1-

# grades = input("Please Enter your grades: ").split(",")
#
# try:
#     grade = [int(grade) for grade in grades]
#     print(grade)
# except ValueError:
#     print("The value you entered is in invalid format.\nPlease Enter the right format for the program to run.")


# 2-
def func():
    try:
        return "coming from the try clause"
    finally:
        return "coming from the final clause."


print(func())

# 3-

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: cannot find data.txt")