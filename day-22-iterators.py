# with open("iris.csv", "r") as iris_file:
#     iris_data = iris_file.readlines()
#
# headers = iris_data[0].strip().split(",")
# irises = []
#
# for line in iris_data[1:]:
#     iris = line.strip().split(",")
#     irises_dict = dict(zip(headers, iris))
#
#     irises.append(irises_dict)
#
# print(irises)


# irises = []
#
# with open("iris.csv", "r") as iris_file:
#     header = next(iris_file).strip().split(",")
#
#     for line in iris_file:
#         iris = line.strip().split(".")
#         iris_dict = dict(zip(header, iris))
#
#         irises.append(iris_dict)
#
# print(irises)

# def first_fifty_numbers():
#     nums = []
#     i = 0
#     while i <= 50:
#         nums.append(i)
#         i += 1
#     return nums
#
#
# #
# #
# print(first_fifty_numbers())

# class FirstHundred:
#     def __init__(self):
#         self.number = 0
#
#     def __next__(self):
#         if self.number < 100:
#             current = self.number
#             self.number += 1
#             return current
#         else:
#             raise StopIteration


# class FirstHundred:
#     def __init__(self):
#         self.number = 0
#
#     def __next__(self):
#         if self.number < 50:
#             current = self.number
#             self.number += 1
#             return current
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# print(sum(FirstHundred()))
#
# for i in FirstHundred():
#     print(i)
#
#
# class AnotherIterable:
#     def __init__(self):
#         self.name = ['Ahmed', 'Mohamed']
#
#     def __len__(self):
#         return len(self.name)
#
#     def __getitem__(self, item):
#         return self.name[item]
#
#
# for name in AnotherIterable():
#     print(name)
# print(len(AnotherIterable()))


# from datetime import datetime, timezone, timedelta
#
# today = datetime.now(timezone.utc)
# tomorrow = today + timedelta(days=1)
# after_7_days = today + timedelta(days=7)
# print(today)
# print(tomorrow)
# print(after_7_days)
# time_difference = datetime.now(timezone.utc) - datetime.now()
# print(time_difference)

import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def powers(number):
    return [x ** 2 for x in range(number)]


measure_runtime(lambda: powers(5000000))

import timeit

print(timeit.timeit("[x ** 2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
