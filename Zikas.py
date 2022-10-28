# age = input("Enter your age in years = ")
# age_as_number = int(age)
# print(f"you have lived for {age_as_number*12} months.")
# age = int(input("Enter your age in years = "))
# print(f"you have lived for {age*12} months.")

# age = 28
# is_over_age = age >= 18
# is_under_age = age <= 18
# is_twenty_eight = age == 28
#
# print(is_twenty_eight)
# print(is_under_age)
# print(is_over_age)

# my_number = 13
# user_number = int(input("Enter a y: "))
# matches = user_number == my_number
#
# print(f"You got it right: {matches}")

# age = int(input("Enter your age: "))
# can_learn_programing = age > 0 and age<150
# print(f"you can learn programming: {can_learn_programing}")

# age = int(input("Enter your age: "))
# usually_not_working = age < 18 or age > 60
# print(f"at {age},you usually not working: {usually_not_working}")

# friends = [["Islam", 24], ["Mohamed", 31], ["Seny", 19]]
# print(friends)
#
# print(friends[0])
# print(friends[0][0])
# print(friends[0][1])
# print(friends[1][0])
# print(friends[1][1])
# print(friends[2][0])
# print(friends[2][1])

# friends = [
#     ["Islam", 24],
#     ["Mohamed", 31],
#     ["Seny", 19],
#     ["Gimy", 31],
#     ["Zahran", 28]
# ]

# friends = [["Islam", 24], ["Mohamed", 31], ["Seny", 19]]
# friends.append(["Gimy", 31])
# print(friends)

# art_friend = {"Seny", "Snoopy", "Mohamed"}
# # science_friend = {"Mohamed", "Islam"}
# #
# # art_but_not_science = art_friend.difference(science_friend)
# # print(art_but_not_science)
# #
# # science_but_not_art = science_friend.difference(art_friend)
# # print(science_but_not_art)
# #
# # not_in_both = art_friend.symmetric_difference(science_friend)
# # print(not_in_both)

# art_and_science = art_friend.intersection(science_friend)
# print(art_and_science)
# all_friend = art_friend.union(science_friend)
# print(all_friend)

# grades = [50, 70, 40, 100, 94]
# total = sum(grades)
# print(total)
# length = len(grades)
# average = total / length
# print(average)

# friends = ["Mohamed", "Islam", "Seny"]
# print(f"My friends are: {friends}")
# comma_separated = ", ".join(friends) #you can change the ", " with " " or whatever you like
# print(f"My friends are: {comma_separated}")

# ************************************************************************************************************
# name = input("Please enter your full name: ").split()
# print(name)
# first_name = name[0]
# surname = name[1]
#
# print(f"{first_name.title()}, is first name\n{surname.title()} is surname ")
# ************************************************************************************************************
# base_numbers = [1, 2, 3, 4, 5]
# processed_number = [str(n) for n in base_numbers]
# print("|".join(processed_number))
# ************************************************************************************************************
# quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
# ]
# for quote in quotes:
#     print(f"{quote}    #normal print")
#     print(" ")
#     print(f"""{quote[1:-1]}    #Strip the (')""")
#     print("")
#     print(quote.strip("'"), "    #Strip the (')")
#     print("********************************************* ")
# ************************************************************************************************************
# sample_string = input("Please enter a word: ")
# print(sample_string)
# print(sample_string.strip())
# character_count = len(sample_string.strip())
# word_count = len(sample_string.strip().split())
#
# print(f"Character count: {character_count}")
# print(f"Word count: {word_count}")
# ************************************************************************************************************
# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 20000000),
#     ("Memento", 9000000),
#     ("Requiem for a Dream", 4500000),
#     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#     ("Avengers: Age of Ultron", 365000000),
#     ("Avengers: Endgame", 356000000),
#     ("Incredible 2", 200000000)
# ]
# new_movie_count = int(input("How many movie(s) you want to add: "))
# for _ in range(new_movie_count):
#     if new_movie_count != 0:
#         name = input("Enter movie name: ")
#         price = int(input("Enter movie budget: "))
#         new_movie = (name, price)
#         movies.append(new_movie)
#     else:
#         break
#
# high_budget = []
# total_budget = 0
# for movie in movies:
#     total_budget = total_budget + movie[1]
# average = total_budget / len(movies)
#
# print(f"Total budget is {total_budget:,}\nAverage is {average:,}")
#
# for movie in movies:
#     if movie[1] > average:
#         high_budget.append(movie)
#         over_average = movie[1] - average
#         print(f"{movie[0]} cost ${movie[1]:,}, and ${over_average:,} over average price.")
#
# print(f"There were {len(high_budget)} movies over the average price.")
# ask_user_to_see_movies = input("are you want to see our movies? ")
# while ask_user_to_see_movies != 'no':
#     if ask_user_to_see_movies == 'yes':
#         for movie1 in movies:
#             print(f"{movie1[0]} costs ${movie1[1]}")
#     else:
#         print("Sorry that's not correct, please type 'yes' or 'no' only.")
#     ask_user_to_see_movies = input("are you want to see our movies? ")
# print("Ok, no problem, program is stopping now:")
# ************************************************************************************************************
# x = "Python"
# for _ in x:
#     if _ != "o":
#         print(_)
#     else:
#         break

# ************************************************************************************************************

# x = [1, 2, 3, 4, 5]
# squares = [y ** 2 for y in x]
#
# movie = {
#     "title": "thor: ragnarok",
#     "director": "taika waititi",
#     "producer": "kevin feige",
#     "production_company": "marvel studios"
# }
#
# update_movie = {}
# for key, value in movie.items():
#     update_movie.update({key: value.title()})
#
# print(update_movie)

# def print_movie(*args):
#     for value in args:
#         print(value)

#
# movie = {
#     "title": "The Matrix",
#     "director": "Wachowski",
#     "year": 1999
# }
#
# # print_movie(*movie.values())
#
# country = {
#     "name": "Germany",
#     "population": "83 million",
#     "capital": "Berlin",
#     "currency": "Euro"
# }
# country_templates = """Name: {name}
# Population: {population}
# Capital: {capital}
# Currency: {currency}"""


# user_number = input("Please enter a y: ")
#
# while int(user_number) < 10:
#     print("Your y was less than 10.")
#     user_number = input("Please select another y: ")
#
# print("Your y was at least 10.")
# numbers = list(range(1, 11))
# squares = (number ** 2 for number in range(1, 11))
# print(numbers)
# try:
#     for i in numbers:
#         print(f"The square root of ({i}) equals to: {i} ** 2 = {next(squares)}")
#
# except StopIteration:
#     print("iteration. ends")
#
#
# def first_hundred():
#     for number in range(1, 101):
#         yield number
#
#
# x = first_hundred()
# y = list(range(1, 102))
#
# print(*y)

# def before_and_after(func, name, fun2, age):
#     print("before......")
#     func(name)
#     print("after....")
#     print(fun2(age))
#
#
# def greet(name):
#     print(f"Hello!,{name}")
#
#
# def age(age):
#     if age >= 18:
#         return f"you are old enough to learn how to code yourself."
#     else:
#         return f"you quite young for learning such a program."
#
#
# while True:
#     name = input("your name pls: ")
#     age1 = int(input("your age pls: "))
#     if name or age1 == "q":
#         break
#     elif age1 > 0:
#         before_and_after(greet, name, age, age1)
#     elif age1 == 0:
#         print("What are you kiddin me?")
#     else:
#         print("stop kidding me.")


