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
# Me testing myself:
# drinks = [
#     {"name": "Mohamed", "drink": "tea", "price": 4, "amount": 4},
#     {"name": "Seny", "drink": "coffee", "price": 8, "amount": 2},
#     {"name": "Ahmed", "drink": "hookah", "price": 4, "amount": 10},
#     {"name": "Islam", "drink": "cold drinks", "price": 10, "amount": 2}
# ]
#
#
# def drinks_cal(drink, intro):
#     print(intro)
#     drink_price = drink["price"] * drink["amount"]
#     name = f"Mr.{drink['name']}"
#     drink_name = f"{drink['drink']}"
#     print(f"{name} pays {drink_price}EGP for drinking {drink_name}")
#     if drink_price > 18:
#         print(f"{name} paid too much xD.")
#     else:
#         print(f"{name} haven't paid enough :/ .")
#
#
# for d in drinks:
#     drinks_cal(d, "At Dahab Cafe: ")
#
# print("***********")
# print("Price list: \n***********")
#
# y = []
#
#
# def drink1(drink):
#     x = drink['drink']
#     y.append(x)
#
#
# for dr in drinks:
#     drink1(dr)
# print(y)

# ************************************************************************************************************
# x = list(range(1, 101))
# print(x)
# for i in range(1, len(x) + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(f"{i}")
# ************************************************************************************************************
# movie = ("12 Angry Men", "Sidney Lumet", 1957)
#
# title, director, year = movie
# print(title)
# print(director)
# print(year)
# ************************************************************************************************************
# movies = [
#     ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004),
#     ("Memento", "Christopher Nolan", 2000),
#     ("Requiem for a Dream", "Darren Aronofsky", 2000)
# ]
#
# # for title, director, year in movies:
# #     print(f"{title} ({year}), directed by {director}")
# for index in range(len(movies)):
#     print(f"{index+1}. {movies[index][0]} ({movies[index][2]}), directed by {movies[index][1]}.")
# ************************************************************************************************************


# def fun(x, y):
#     for counter, i in enumerate(range(y), start=1):
#         print(f"{counter} {x}")
#     print(range(y))
#
#
# fun("Ahmed", 5)
# print()
# fun("Ahmed", y=5)

# ************************************************************************************************************
# Exercise 1:
# *****************

"""
def summation(x, y):
    x + y
    print(x + y)


def sub(x, y):
    x - y
    print(x - y)


def multiplication(x, y):
    x * y
    print(x * y)


def division(x, y):
    if y == 0:
        print(f"can't divide by Zero")
    else:
        print(x / y)


tv_show = [{
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
]
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]


def print_show_info(shows):
    print(f"You have ({len(shows)}) movies.")
    for counter, show in enumerate(shows, start=1):
        print(f"{counter}- {show['title']}({show['initial_release']}), -({show['seasons']}) seasons.")


friends = ["Rolf", "John", "Mary"]
x = friends[0:2]


def palindrome():
    split_input = input("Enter a word: ")
    split_input = split_input.strip().lower()
    user_input_inverse = split_input[::-1]
    if list(user_input_inverse) == list(split_input):
        print("True")
    else:
        print("False")



palindrome()
"""

# ************************************************************************************************************
# Exercise Seny:
# *****************

# movies = [("Blue elephant", "seny", 2016, 30000000)]
# movie_title = input("Enter movie title: ")
# movie_director = input("Enter movie director: ")
# movie_release_year = int(input("Enter release year: "))
# movie_budget = int(input("Enter movie budget: "))
# movie_list = (movie_title, movie_director, movie_release_year, movie_budget)
# print(f"{movie_list[0]} ({movie_list[2]})")
# movies.append(movie_list)
# print()
# print(movies)
# print()
# movies.pop(0)
# print(movies)
# ************************************************************************************************************
# Exercise Seny_2:
# *****************
# ay_7aga = input("ekteb rakam ya mota5alef: ")
# if int(ay_7aga) > 0:
#     print("el rakam positive ya mota5alef.")
# elif int(ay_7aga) == 0:
#     print("el rakam zero ya teez olla")
#
# else:
#     print("el rakam negative ya mota5alef.")


# hour_worked = int(input("e4ta8alt kam sa3a ya teez l 2olla: "))
# hourly_wage = int(input("bt2bd kam y bdani: "))
# over_time = hourly_wage - 40
# over_amount = over_time * (hourly_wage * 1.1)
# if hour_worked > 40:
#     print(f"leek overtime = {over_time} hours.")
#     print(f"l mafrood t2bab {(40 * hourly_wage) + over_amount}")
# else:
#     print(f"nta matrood.")

#
# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]
#
# for employee in employees:
#     print(f"{employee[0]} should be paid {employee[1] * employee[2]}.")
# prices = []
# for i in employees:
#     prices.append(i[2])
#
# total = sum(prices)
# average = total / len(employees)
#
# for above in employees:
#     if above[2] > average:
#         print(f"{above[0]} earned above average.")
#     else:
#         print(f"{above[0]} hasnot made it.")

# for x in range(1, 101):
#     if x % 3 == 0:
#         if x % 5 == 0:
#             print("fizzBuzz")
#         else:
#             print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(f"{x}")

# Sorted_numbers = [1, 2, 3, 4, 5]
# print(Sorted_numbers)
# print(type(Sorted_numbers))
# Sorted_numbers = str(Sorted_numbers)
# print(type(Sorted_numbers))
# print(Sorted_numbers)
# name = ["Mike", "Sofia", "Helen"]
# print(name)
# print(", ".join(name))
# print(name)
# print(f"My friends are: {', '.join(name)}")
#
#
# Sorted_numbers = [1, 2, 3, 4, 5]
# Stringfied_numbers = []
# for y in Sorted_numbers:
#     Stringed_numbers.append(str(y))
#
# print(Stringfied_numbers)
#
#
# print(", ".join(Stringfied_numbers))
#
# split_input = input("Please enter your name: ")
# split_input = split_input.split()
#
# first_name = split_input[0]
# second_name = split_input[1]
#
# print(first_name)
# print(second_name)
#
# print(split_input)

# Sorted_numbers = [1, 2, 3, 4, 5]
# str_numbers = []
# for y in Sorted_numbers:
#     str_numbers.append(str(y))
#
# print(str_numbers)
# print(" ".join(str_numbers))


# quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
# ]
#
# for quote in quotes:
#     print(len(quote))

# sample_string = input("Please enter a word: ").strip()
#
# character_count = len(sample_string)
# word_count = len(sample_string.split())
#
# print(f"Character count: {character_count}")
# print(f"Word count: {word_count}")

# def multigreet(other, *names):
#     for name in names:
#         print(f"Hello, {name}!")
#
#
# multigreet("Jose", "Phil", "Ahmed", "Mohamed", "Zakaria", "Abdelmagid", "Soliman")
#
# phil = dict(name="Phil", age=29, city="Budapest", nationality="British")
#
# print(phil)

# def pretty_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# pretty_print(title="The Matrix", director="Wachowski", year=1999)

# while True:
#     select_option = input("Select 'a', 'b', 'c', 'd','e', or 'q' to quite. ")
#     if select_option == 'a':
#         print(f"You entered: ({select_option})")
#     elif select_option == 'b':
#         print(f"You entered: ({select_option})")
#     elif select_option == 'c':
#         print(f"You entered: ({select_option})")
#     elif select_option == 'd':
#         print(f"You entered: ({select_option})")
#     elif select_option == 'e':
#         print(f"You entered: ({select_option})")
#     elif select_option == 'q':
#         confirmation = input("are you sure you want to quite? [y/n].")
#         if confirmation == 'y':
#             print("see you later.")
#             break
#         elif confirmation == 'n':
#             pass
#         else:
#             print(f"You entered {confirmation} and its not acceptable.")
#     else:
#         print("you entered invalid option.")



