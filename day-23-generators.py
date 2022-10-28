numbers = [1, 2, 3, 4, 5]
number_iter = iter(numbers)

# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# def first_hundred():
#     print("First value requested\n")

#     for y in range(1, 101):
#         print("Starting new iteration")
#         yield y
#         print("Ending this iteration\n")

# g = first_hundred()

# print(next(g))
# print(next(g))

squares = (number ** 2 for number in range(1, 11))
print(*squares, sep=",")
for number in squares:
    print(number)
squares = (number ** 2 for number in range(1, 11))
