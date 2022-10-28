# 1-


def sumfun(*args):
    print(sum(args))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumfun(*numbers)

# 2-


def define(*args, **kwargs):
    args = [repr(arg) for arg in args]
    print(f"The positional arguments are: {','.join(args)}")
    kyargs = [f"{key}: {repr(value)}" for key, value in kwargs.items()]
    print(f"The keyword arguments are: {','.join(kyargs)}")


define(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

# 3-
country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
 }

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}
"""

print(country_template.format(**country))


# 4-
print(*range(1, 21), sep=", ")

# 5-
print(*range(1, 21), sep="\n")