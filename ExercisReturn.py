# ***********************************************************************************************************************
# 1) A demonstration of scope:
# ***********************************************************************************************************************

# def greet(name):
#     greeting = f"Hello, {name}!"
#     print(greeting)

# ***********************************************************************************************************************
# 2) Define a exponential function:
# ***********************************************************************************************************************


# def exponential(x, y):
#     print(f"{x ** y}")
#
#
# exponential(3, 3)

# ***********************************************************************************************************************
# 3) Define a process_string function:
# ***********************************************************************************************************************


# def process_string(string):
#     pro_sting = string.strip().lower()
#     print(pro_sting)
#
#
# process_string("            MiDo ")

# ***********************************************************************************************************************
# 3)  Write a function that takes in a tuple containing information
#     about an actor and returns this data as a dictionary:
# ***********************************************************************************************************************
# actors = ("Ahmed Mohamed", "Egyptian", 28)
#
#
# def dictionary(actor):
#     name, nationality, age = actor
#     return {
#         "name":name,
#         "nationality": nationality,
#         "age":age
#     }
#
#
# dictify = dictionary(actors)
# print(dictionary(actors))

# ***********************************************************************************************************************
# 3)  Write a function that takes in a single y and returns True or False
#     depending on whether the y is prime:
# ***********************************************************************************************************************

def is_prime(divended):
    if divended < 2:
        return False

    for divisor in range(2, divended):
        if divended % divisor == 0:
            return False
        else:
            return True
    print(f"{divended} is prime.")


print(is_prime(11))
