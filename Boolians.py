# truthy = True
# falsy = False
#
# age = 30
# is_over_age = age >= 20
# print(f"{is_over_age}")
# is_under_age = age < 20
# print(f"{is_under_age}")
# is_thirty = age == 30
# print(f"{is_thirty}")


# my_number = 10
# user_number = int(input("Enter your y: "))
# matches = my_number == user_number
#
# print(f"You got it right, {matches}.")

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 2, 3, 4, 5]
# list_3 = list_1
# print(id(list_1))
# print(id(list_2))
# print(id(list_3))
#
# print(id(list_1) == id(list_2))
# print(id(list_1) is id(list_2))
# print(list_1 is list_3)
#
# Sorted_numbers = [1, 2, 3, 4]
# new_numbers = Sorted_numbers + [5]
#
# print(Sorted_numbers is new_numbers)
#
# Sorted_numbers = [1, 2, 3, 4]
# print(id(Sorted_numbers))
# Sorted_numbers.append(5)
# print(id(Sorted_numbers))

# Sorted_numbers = [1, 2, 3, 4, 5]
# print(Sorted_numbers)
# Sorted_numbers = str(Sorted_numbers)
# print(Sorted_numbers)
#
# print(", ".join(project_authors))
# project_authors = ["Mike", "Sofia", "Helen"]

# user_numbers = input("Please enter Sorted_numbers separated by commas: ")
# print(user_numbers)
# user_numbers = user_numbers.split(",")
# number_list = []
#
# for y in user_numbers:
#     number_list.append(y.strip())
# print(number_list)

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# user_numbers = input("Please enter Sorted_numbers separated by commas: ")
# user_numbers_list = list(user_numbers.strip())
# print(user_numbers_list)

# 1-
# split_input = input("Please enter your full name: ")
# split_input = split_input.split()
# first_name = split_input[0]
# last_name = split_input[1]
# print(split_input)
# print(f"Hello, {first_name} {last_name.title()}")

# 2-
# y = [1, 2, 3, 4, 5]
# singed_number = []
# for i in y:
#     singed_number.append(str(i))
# print(y)
# print(singed_number)
# print("|".join(singed_number))


# 3-
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
for quote in quotes:
    print(quote.strip("'"))

# quote_1 = quotes[0]
# quote_2 = quotes[1]
# quote_3 = quotes[2]
# quote_4 = quotes[3]
#
# print(f"""{quote_1}
# {quote_2}
# {quote_3}
# {quote_4}
# """
# )
