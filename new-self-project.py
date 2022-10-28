menu_prompt = """Please enter one of the following option below:
- 'a' To add your details:
- 's' To show your details:
- 'f' To find your details:
- 'q' To quit:

what will you choose? """
info_list = []


def add_info():
    name = input("Enter your full Name: ").title()
    age = input("Enter your real age:")
    profession = input("Enter your profession: ").capitalize()
    info_list.append({
        "name": name,
        "age": age,
        "profession": profession
    })
    return info_list


def show_info(per_info):
    print(f"We have {len(per_info)} person(s).\n")
    for counter, person in enumerate(per_info, start=1):
        name, age, profession = person.values()
        print(f"{counter}- {name} is {age} years old, works as {profession}")


def find_info():
    find_by = input("Search By (name, age, profession): ")
    looking_for = input("Enter your value: ")

    person_details = find_by_attribute(lambda x: x[find_by], looking_for)
    show_info(person_details)


def find_by_attribute(properties, value):
    finder = []
    for person in info_list:
        if properties(person) == value:
            finder.append(person)
        else:
            print("No match for what you looking!!!")
    return finder


while True:
    select_option = input(menu_prompt).lower()
    if select_option == 'q':
        break
    elif select_option == 'a':
        add_info()
    elif select_option == 's':
        show_info(info_list)
    elif select_option == 'f':
        find_info()
    else:
        print("Invalid-command....")
