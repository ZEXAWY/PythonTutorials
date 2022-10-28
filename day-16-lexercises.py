# 1-
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]


def get_name(student):
    return student['name']


# name_sort = sorted(students, key=get_name)
# name_sort = sorted(students, key=lambda student: student['name'])
# students.sort(key=get_name)
students.sort(key=lambda student: student['name'])
print(students)

# 2-

expo = lambda base, exponent: base ** exponent
print(expo(20, 2))
