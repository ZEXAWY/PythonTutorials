# 1) Define four functions: add, subtract, divide, and multiply:
# ********************************************************************************************************

def summation(x, y):
    print(f"{x + y}")


def subtraction(x, y):
    if x >= 0 and y >= 0:
        if x > y:
            print(f"{x - y}")
        elif x < y:
            print("The result is negative Value.")
            user_confirm = input("Are you want to subtract the (second - first)? (y/n)")
            if user_confirm == 'y':
                print(f"{y - x}")
            elif user_confirm == 'n':
                print(f"Ok.")
    else:
        print("Please enter a positive value.")


def multiplication(x, y):

    print(f"{x * y}")


def division(x, y):
    if y != 0:
        print(f"{x / y}")
    else:
        print("You are trying divide by Zero.. We cannot do that.")


def menu():
    user_input = input("Enter '1' to sum, '2' to subtract, '3' to multiply, '4' to divide, 'q' to exit: ")
    while user_input != 'q':
        if user_input == '1':
            x = int(input("Please enter the First Number: "))
            y = int(input("Please enter the Second Number: "))
            summation(x, y)
        elif user_input == '2':
            x = int(input("Please enter the First Number: "))
            y = int(input("Please enter the Second Number: "))
            subtraction(x, y)
        elif user_input == '3':
            x = int(input("Please enter the First Number: "))
            y = int(input("Please enter the Second Number: "))
            multiplication(x, y)
        elif user_input == '4':
            x = int(input("Please enter the First Number: "))
            y = int(input("Please enter the Second Number: "))
            division(x, y)
        else:
            print("Please one of the above choices: ")
        user_input = input("Enter '1' to sum, '2' to subtract, '3' to multiply, '4' to divide, 'q' to exit: ")


menu()

print("Thanks for using my Program xD \nProgram closing...")

# ********************************************************************************************************
# 2) Define a function called (print_show_info) should print the information stored in the dictionary :
# ********************************************************************************************************
# tv_show = {
#     "title": "Breaking Bad",
#     "seasons": 5,
#     "initial_release": 2008
# }
#
#
# def print_show_info(show_info):
#     title = tv_show["title"]
#     season = tv_show["seasons"]
#     initial_release = tv_show["initial_release"]
#
#     print(f"{title} ({initial_release}) -{season} seasons.")
#
#
# print_show_info(tv_show)

# ********************************************************************************************************
# 3) se your function, print_show_info, and a for loop, to iterate over the series :
# **********************************************************************************
# series = [
#     {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
#     {"title": "Fargo", "seasons": 4, "initial_release": 2014},
#     {"title": "Firefly", "seasons": 1, "initial_release": 2002},
#     {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
#     {"title": "True Detective", "seasons": 3, "initial_release": 2014},
#     {"title": "Westworld", "seasons": 3, "initial_release": 2016},
# ]
#
#
# def tv_shows():
#     for shows in series:
#         title = shows["title"]
#         seasons = shows["seasons"]
#         initial_release = shows["initial_release"]
#         print(f"{title} ({initial_release}) -{seasons} seasons.")
#
#
# tv_shows()

# ********************************************************************************************************
# 2) Define a function called (print_show_info) should print the information stored in the dictionary :
# ********************************************************************************************************
# tv_show = {
#     "title": "Breaking Bad",
#     "seasons": 5,
#     "initial_release": 2008
# }
#
#
# def print_show_info(show):
#     title = show["title"]
#     season = show["seasons"]
#     initial_release = show["initial_release"]
#
#     print(f"{title} ({initial_release}) -{season} season(s).")
#
#
# print_show_info(tv_show)

# ********************************************************************************************************
# 3) se your function, print_show_info, and a for loop, to iterate over the series :
# **********************************************************************************
# series = [
#     {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
#     {"title": "Fargo", "seasons": 4, "initial_release": 2014},
#     {"title": "Firefly", "seasons": 1, "initial_release": 2002},
#     {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
#     {"title": "True Detective", "seasons": 3, "initial_release": 2014},
#     {"title": "Westworld", "seasons": 3, "initial_release": 2016},
# ]
#
#
# def print_show_info(show):
#
#     title = show["title"]
#     seasons = show["seasons"]
#     initial_release = show["initial_release"]
#     print(f"{title} ({initial_release}) -{seasons} seasons.")
#
#
# for shows in series:
#     print_show_info(shows)
