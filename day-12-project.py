reading_list = []
menu_prompt = """Please select one of the following options:
- 'a' for adding books.
- 'l' for showing books.
- 'q' to quite.

What will you choose? """

select_option = input(menu_prompt).strip().lower()


def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("year: ").strip().title()

    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    reading_list.append(new_book)


def show_book():
    print()
    for book in reading_list:
        title, author, year = book.values()

        print(f"{title} {year}, by {author}")
    print()


while select_option != 'q':
    if select_option == 'a':
        add_book()
    elif select_option == 'l':
        if reading_list:
            show_book()
        else:
            print("you have no books.")
    else:
        print(f"you entered '{select_option}' and it's invalid.")

    select_option = input(menu_prompt).strip().lower()
