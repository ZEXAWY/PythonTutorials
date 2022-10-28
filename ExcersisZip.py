# 1-
# main_characters = [
#     ("BoJack Horseman", "Will Arnett", "Horse"),
#     ("Princess Carolyn", "Amy Sedaris", "Cat"),
#     ("Diane Nguyen", "Alison Brie", "Human"),
#     ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
#     ("Todd Chavez", "Aaron Paul", "Human")
# ]
# for character, actor, species in main_characters:
#     print(f"{character} is a {species.lower()} voiced by {actor}.")

# 2-
# data = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# student_name, student_id_number, disciplines = data
# major_discipline , minor_discipline = disciplines
# print(student_name)
# print(student_id_number)
# print(disciplines)
# print(major_discipline)
# print(minor_discipline)

# 3-
data = ("John Smith", 11743, "Mathematics")
data1 = ("John Smith", 11743, "Computer Science", "Mathematics")
new_data = list(zip(data1,data))
print(new_data)