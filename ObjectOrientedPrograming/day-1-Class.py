# *********************************************************************************************************************
# class (object oriented program):
# *********************************
# my_student = {
#     "name": "Ahmed Mohamed",
#     "grades": [89, 90, 44, 51, 100]
# }
#
#
# def average_grade(student):
#     grades = student['grades']
#     average = sum(grades) / len(grades)
#     print(average)
#
#
# average_grade(my_student)
#
#
# class Student:
#     def __init__(self, new_name, new_grades):
#         self.name = new_name
#         self.grades = new_grades
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student_one = Student('Ahmed', [89, 90, 44, 51, 100])
# student_two = Student('Mohamed', [89, 90, 77, 85, 100])
# print(f"{student_one.name} has average degrees of ({student_one.get_average()})")
# print(f"{student_one.name} has average degrees of ({student_two.get_average()})")
#
# print(student_one.name, ' gets average of ', student_one.get_average())
# print(student_two.name, ' gets average of ', student_two.get_average())
# # or
# print(Student.get_average(student_one))
#
#
# class Movie:
#     def __init__(self, new_movie, new_director):
#         self.name = new_movie
#         self.director = new_director
#
#     def print_info(self):
#         print('<<{}>> by {}'.format(self.name, self.director))
#
#
# movie_one = Movie('The Matrix', 'MyDream')
# movie_one.print_info()

# *********************************************************************************************************************
# Magic Methods in class:
# ***********************
# class Garage:
#     def __init__(self):
#         self.cars = []
#
#     def __len__(self):
#         return len(self.cars)
#
#     def __getitem__(self, item):
#         return self.cars[item]
#
#     def __repr__(self):
#         return f'<Garage {self.cars}> {len(self)}'
#
#     # def __str__(self):
#     #     return f'Garage with {len(self)} cars.'
#
#
# ford = Garage()
# ford.cars.append('Fiesta')
# ford.cars.append('Focus')
#
# print(ford.cars)
# print(ford[0])
# # only after defining __len__ and __getitem__ method, we can use for loop on objects.
# for car in ford:
#     print(car)
#
# print(ford)

# *********************************************************************************************************************
# inheritance in python:
# **********************
# class Student:
#     def __init__(self, name, school, profession):
#         self.name = name
#         self.school = school
#         self.marks = []
#         self.profession = profession
#
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
#
# class WorkingStudent(Student):
#     def __init__(self, name, school, salary, profession=None):
#         super().__init__(name, school, profession)
#         self.salary = salary
#
#     @property
#     def weekly_salary(self):
#         return self.salary * 32.5
#
#
# rolf = WorkingStudent('Rolf', 'HUE', 13.5)
# rolf.marks.append(60)
# rolf.marks.append(99)
# # print(rolf.profession)
# print(rolf.average())
# print(rolf.weekly_salary)
#
# mohamed = Student('Mohamed', 'CU', 'Physics Professor')
# mohamed.marks.append(79)
# mohamed.marks.append(89)
# print(mohamed.average())
# print(mohamed.profession)

# *********************************************************************************************************************
# Class Method and Static Method:
# *******************************

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


new_number = FixedFloat.from_sum(19.5563, 0.2256)
print(new_number)


class Egyptian(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Egyptian {self.symbol}{self.amount}'


money = Egyptian.from_sum(15.5364, 4.3261)
print(money)
