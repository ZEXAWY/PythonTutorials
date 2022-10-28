student = {
    "name": "John Smith",
    "grades": [88, 76, 92, 85, 69]
}
student["age"] = 17
# print(student)
student["age"] = 18
# print(student)

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019,
    "runtime": 181
}

#
# meta_info = {
#     "runtime": 181,
#     "budget": "$356 million",
#     "earnings": "$2.798 billion",
#     "producer": "Kevin Feige"
# }
#
del movie["runtime"]
# movie.update(meta_info)

for attribute in movie:
    print(attribute)

for value in movie.values():
    print(value)

for key, value in movie.items():
    print(f"{key}: {value}")
