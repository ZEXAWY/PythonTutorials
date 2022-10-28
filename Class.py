our_student = {
    'name': "Ahmed Mohamed",
    'grades': [10, 20, 40, 50, 35]
}


def average_grades(student):
    return sum(student['grades']) / len(student['grades'])


# print(average_grades(our_student))


# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student_one = Student("Ahmed Mohamed", [48, 98, 79, 89, 87])
# print(student_one.average())
# print(Student.average(student_one))
# print(Student("Ahmed Mohamed", [48, 98, 79, 89, 87]).grades)
# student_two = Student("Mostafa Abdelrahman", [56, 99, 87, 56, 60])
# print(student_two.average())
#
#
# def average(self):
#     return sum(self.grades) / len(self.grades)
#
#
# print(average(student_one))
#
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
#
# ford = Garage()
# ford.cars.append("Fiesta")
# ford.cars.append("Focus")
#
# print(ford[1])
#
# for i in ford:
#     print(i)

# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.grades = []
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# class WorkingStudents(Student):
#     def __init__(self, name, school, salary):
#         super().__init__(name, school)
#         self.salary = salary
#
#     def weekly_salary(self):
#         return self.salary * 8 * 6
#
#
# ahmed = WorkingStudents("Ahmed", "HUM", 140.0)
# print(ahmed.salary)
# ahmed.grades.append(79)
# ahmed.grades.append(99)
# ahmed.grades.append(86)
# print(ahmed.average())
# print(ahmed.weekly_salary())

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


object1 = Foo()
object1.hi()


class Bar:
    @staticmethod
    def hi():
        print('i print whatever i Want in here :D')


new_object = Bar()
new_object.hi()