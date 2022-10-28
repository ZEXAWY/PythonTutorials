# """
# here some examples of functions accepts many arguments as parameters:
# """
#
#
# # def mull(x, y):
# #     print(x * y)
#
# # def mull(*args):
# #     print(args[0] * args[1])
# #
# #
# # mull(3, 5)
# #
# #
# # def multipart(*names):
# #     for name in names:
# #         print(f"Hello, {name.title()}")
# #
# #
# # multipart("Rolf", "Ahmed", "mohamed", "Snoopy", "Islam", "Seny", "Gimy")
#
# def multigreet(*names):
#     for name in names:
#         print(f"Hello, {name.title()}")
#
#
# multigreet("galal", "safwat", "seny", "sadat", "zika", "zex")
#
# phile = dict(name="Phil", age=29, city="Budapest", nationality="British")
#
# print(phile)
# print()
#
#
# def pretty(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# pretty(title="the zex's", director="zex", year=1994)
# print()
#
#
# # def print_movie(*args):
# #     for value in args:
# #         print(value)
# #
# #
# # movie = {
# #     "title":"THE MATRIX",
# #     "director": "the zex",
# #     "year": 1993
# # }
# #
# # print_movie(*movie.keys())
# # print_movie(*movie.values())
#
#
# def print_movie(**kwargs):
#     for key, value in kwargs.items() :
#         print(f"{key}: {value}")
#
#
# movie = {
#     "title":"THE MATRIX",
#     "director": "the zex",
#     "year": 1993
# }
#
# print_movie(studio= "Marvel", **movie)
"""
here is some exercises about the above args and keyword arguments:
"""
# 1-
# def summation(*args):
#     print(sum(args))
#
#
# summation(1, 2, 3, 4, 5, 6)

# 2-
# def arg_printer(*args, **kwargs):
#     args = [repr(arg) for arg in args]
#     print(f"The positional args are: {','.join(args)}")
#     kwargs = [f"{key} = {repr(value)}" for key, value in kwargs.items()]
#     print(f"The keyword arguments are: {', '.join(kwargs)}")
#
#
# arg_printer(1, "blue", [1, 23, 5], weight=184, key=lambda x: x ** 2)

# 3-
# country = {
#     "name": "Germany",
#     "population": "83 million",
#     "capital": "Berlin",
#     "currency": "Euro"
# }
#
#
# country_template = """name: {name}
# population: {population}
# capital: {capital}
# currency: {currency}"""
# print(country_template.format(**country))

# 4-
print(*range(1, 21), sep="\n")

