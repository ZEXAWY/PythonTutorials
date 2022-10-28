# names = ["Ahmed", "Mohamed", "Zakaria"]
# print(names)
# names = [name.lower() for name in names]
# print(names)
# names = set(names)
# print(names)


# def cube(y):
#     return y ** 3


from operator import methodcaller

numbers = [2, 3, 4, 5, 6]
# cubed_numbers = map(cube, Sorted_numbers)
# # print(cubed_numbers) calling the function itself not the value inside it
# # for y in cubed_numbers:
# #     print(y)
# print(*cubed_numbers, sep="\n")

# print()


# def add(a, b):
#     return a + b


# odds = [1, 3, 5, 7, 9]
# evens = [2, 4, 6, 8, 10]

# total = map(add, odds, evens)
# print(*total, sep=", ")
# print()


# this line taking the values from line 13 and its not related to the code above him
# cubed_numbers = map(lambda y: y ** 3, Sorted_numbers)
# print(*cubed_numbers)
print()

# from operator import add

# # def add(a, b):
# #     return a + b


# odds = [1, 3, 5, 7, 9]
# evens = [2, 4, 6, 8, 10]

# # totals = map(lambda a, b: a+b, odds, evens)
# totals = map(add, odds, evens)
# print(*totals, sep=", ")

names = ["tom", "richard", "harold"]
title_names = list(map(methodcaller("title"), names))
print(title_names)

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)


def is_even(number):
    return number % 2 == 0


print()
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print()
print(*truthy_values, sep=", ")
