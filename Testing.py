# print(globals())
#
# print("Hello, there how are you? ")
# user_input = input("Enter your name please: ")
#
#
# def print_nice(*movie):
#     for value in movie:
#         print(value)
#
#
# def print_dic(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# data = {
#     "name": "Phil",
#     "age": 29,
#     "city": "Budapest",
#     "nationality": "British"
# }
#
# print_dic(**data)
#
# x = [1, 2, 3, 4, 5]
#
#
# def summation(*args):
#     print(sum(args))
#
#
# summation(*x)
#
#
# def para_printer(*args, **kwargs):
#     args = [repr(arg) for arg in args]
#     print(f"The positional arguments are: {', '.join(args)}")
#     kwargs = [f"{key} = {repr(value)}" for key, value in kwargs.items()]
#     print(f"The Keyword arguments are: {', '.join(kwargs)}")
#
#
# para_printer(1, "blue", [1, 23, 3], height=184, key=lambda x: x ** 2)
#
# country = {
#     "name": "Germany",
#     "population": "83 million",
#     "capital": "Berlin",
#     "currency": "Euro"
# }
#
# country_template = """Name: {name}
# Population: {population}
# Capital: {capital}
# Currency: {currency}"""
#
# print(country_template.format(**country))
# # print(*country.items(), sep="\n")
#
# print(*range(1, 21), sep=", ")
#
# print(globals())

#
# def cubed(i):
#     return i ** 3


# cubed_numbers = map(cubed, numbers)

# for i in cubed_numbers:
#     print(i)

# print(*cubed_numbers)
# cubed_numbers = list(map(cubed, numbers))
# print(cubed_numbers)


# def add(a, b):
#     return a + b


# odds = [1, 3, 5, 7, 9]
# evens = [2, 4, 6, 8, 10]
#
# totals = map(add, odds, evens)
# print(*totals, sep=", ")

# cubed_Numbers = map(lambda i: i ** 2, numbers)
# print(*cubed_Numbers)

# from operator import add
# from operator import methodcaller
#
# odds = [1, 3, 5, 7, 9]
# evens = [2, 4, 6, 8, 10]
# names = ["tom", "richard", "harold"]
#
# total = map(add, odds, evens)
# title_names = map(methodcaller("title"), names)
# print(*title_names)
# numbers = [1, 56, 3, 5, 24, 19, 88, 37]
# even_numbers = [i for i in numbers if i % 2 == 0]
#
# values = [0, "Hello", [], {}, 435, -4.2, ""]
# truthy_values = filter(None, values)
#
# print(*truthy_values, sep=", ")

from operator import methodcaller

# humpty_dumpty = [
#     "  Humpty Dumpty sat on a wall,  ",
#     "Humpty Dumpty had a great fall;     ",
#     "  All the king's horses and all the king's men ",
#     "    Couldn't put Humpty together again."
# ]
#
# humpty_dumpty_new = list(map(lambda sentence: sentence.strip(), humpty_dumpty))
# humpty_dumpty_new1 = map(methodcaller("strip"), humpty_dumpty)
# print(*humpty_dumpty_new, sep="\n")
# print(humpty_dumpty_new)
# print(*humpty_dumpty_new1, sep="\n")

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

new_names = [name.title() for name in names if len(name) < 8]
print(new_names)

value_no_negatives = filter(lambda number: number >= 0, range(-5, 11))
print(*value_no_negatives)
