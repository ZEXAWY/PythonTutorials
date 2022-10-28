# import math


# def average(Sorted_numbers):
#     try:
#         mean = math.fsum(Sorted_numbers) / len(Sorted_numbers)
#     except (ZeroDivisionError, TypeError):
#         print("An average cannot be calculated by the value you provide.")
#     else:
#         print(mean)


# integers = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
# integers10 = [integer*10 for integer in integers]
# integers_over = [integer / 5 for integer in integers]
# average(integers)
# average(integers10)
# average(integers_over)


# def average(Sorted_numbers):
#     try:
#         mean = math.fsum(Sorted_numbers) / len(Sorted_numbers)
#         print(mean)
#     except ZeroDivisionError:
#         print("0")
#     except TypeError:
#         print("your input is not a collection of Sorted_numbers.")

# while True:
#     try:
#         y = int(input("Please enter a whole y: "))
#         break
#     except ValueError:
#         print("you entered invalid y.")


def test_function():
    try:
        return
    finally:
        print("Return keyword will run after this line excutes first.\nit's finally keyword test. dont bother yourself reading this code.")


test_function()
