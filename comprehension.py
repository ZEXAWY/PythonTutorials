names = ["mary", "Richard", "Noah", "KATE"]
# for name in names:
#     processed_names.append(name.title())
#
# print(processed_names)
#
# processed_names_2 = [name_2.case fold() for name_2 in names]
# print(processed_names_2)

ages = (36, 21, 40, 28)
# people_data = []
# for name, age in zip(names, ages):
#     person_data = ((name.title()), age)
#     people_data.append(person_data)
# print(people_data)

# people = [(name.title(), age) for name, age in zip(names, ages)]
# people = [(name.title(), age)
#           for name, age in zip(names, ages)
# ]
#
# print(people)

student_ids = (112343, 134555, 113826, 124888)
# students = {}
#
# for student_id, name in zip(student_ids, names):
#     student = {student_id: name.title()}
#     students.update(student)
#
# print(students)

# students = {
#     student_id: name.title()
#     for student_id, name in zip(student_ids, names)
# }
# print(students)

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}
new_movie = {
    key: name.title()
    for key, name in movie.items()
}
print(new_movie)
