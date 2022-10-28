# 1-


# user_input = input(
#     "Please Enter you students average grades seperated by comma's: ").split(',')
# print(user_input)
# try:
#     grades = [int(grade.strip()) for grade in user_input]
#     print(grades)

# finally:
#     print("The value you entered cannot be converted to string.")
# 2-
# def test_somethings():
#     try:
#         return "you try try."
#     finally:
#         return "you try finally."

# print(test_somethings())
# 3-
from cgitb import text
from itertools import count


try:
    with open("data.txt", "r") as text_read:
        # print(text_read.read())
        text_data = text_read.read()
        characters = len(text_data)
        words = len(text_data.split(" "))
        print(f"the characters are: {characters}")
        print(f"the words count: {words}")
        

except FileNotFoundError:
    print("no file found in this location.")
