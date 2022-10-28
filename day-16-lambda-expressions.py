# def add(a, b):
#     print(f"the result: {a + b}")
#
#
# adder = add
# del add
#
# adder(6, 56)
# print(adder(6, 56)) # None


# x = [56, 3, 45, 29, 102, 30, 73]
# Sorted_numbers = sorted(x)
# print(Sorted_numbers)
# highest_number = max(Sorted_numbers) # max function is to calculate the max y in the list.
# print(highest_number)

# students = [
#     {"name": "Hannah", "grade_average": 83},
#     {"name": "Charlie", "grade_average": 91},
#     {"name": "Peter", "grade_average": 85},
#     {"name": "Rachel", "grade_average": 79},
#     {"name": "Lauren", "grade_average": 92}
# ]
#
#
# def get_average_grades(student):
#     return student['grade_average']
#
#
# def get_student_name(student):
#     return student['name']
#
#
# validecoration = max(students, key=get_average_grades)
# print(f"The student {validecoration['name']}, score average: {validecoration['grade_average']}")
#
# # name_sorted = sorted(students, key= get_average_grades)
# name_sorted = sorted(students, key=get_student_name)   # beccause it's a list we can't use 'sorted(students.items())'
# print(name_sorted)


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)


operations = {
    "a": add,
    "b": subtract,
    "c": multiply,
    "d": divide
}

selected_option = input("""Please select one of the following options:
- 'a' To add.
- 'b' to subtract.
- 'c' To multiply.
- 'd' To divide.

What will you Choose?: """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("What you mean by that.")
