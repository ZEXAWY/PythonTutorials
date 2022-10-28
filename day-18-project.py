import json


def create_a_file():
    try:
        with open("books.json", "x") as book_file:
            json.dump([], book_file)
    except FileExistsError:
        pass


def add_book():
    books = get_all_books()

    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("year: ").strip()

    book = {
        "title": title,
        "author": author,
        "year": year,
        "read": "Not Read"
    }
    books.append(book)

    with open("books.json", "w") as book_list:
        json.dump(books, book_list)


def get_all_books():
    with open("books.json", "r") as book_list:
        return json.load(book_list)


def show_book(books):
    print()
    for counter, book in enumerate(books, start=1):
        title, author, year, read = book.values()
        print(f"{counter}- {title} ({year}), by {author} -{read}")
    print()


def find_books():
    book_list = get_all_books()
    matching_books = []
    search_term = input("Please enter a book title to search for: ").lower()
    for book in book_list:
        if search_term in book['title'].lower():
            matching_books.append(book)

    return matching_books


def delete_book(books, book_to_delete):
    books.remove(book_to_delete)


def mark_book_as_read(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Read"


def update_book(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        print(f"you have {len(matching_books)} book(s).")
        show_book(matching_books)
        user_choice = input(f"Do you want to proceed?[y/n] ")
        if user_choice == 'y':
            operation(books, matching_books[0])

            with open("books.json", "w") as book_file:
                json.dump(books, book_file)

        elif user_choice == 'n':
            pass
        else:
            print(f"i didn't get what you mean by that.")
    else:
        print("Sorry we didn't find any match of that title.")


create_a_file()
menu_prompt = """Please select one of the following options:
- 'a' for adding books.
- 'l' for showing books.
- 'f' to find your book.
- 'd' to delete book.
- 'r' to mark as read.
- 'q' to quite.

What will you choose? """

select_option = input(menu_prompt).strip().lower()

while select_option != 'q':
    if select_option == 'a':
        add_book()
    elif select_option == 'l':
        reading_list = get_all_books()
        if reading_list:
            print(f"You have {len(reading_list)} Book(s).")
            show_book(reading_list)
        else:
            print("you have no books.")
    elif select_option == 'f':
        matching_book = find_books()
        if matching_book:
            print(f"We find {len(matching_book)} Book(s).")
            show_book(matching_book)
        else:
            print("Sorry, we cant get any value for that title.")

    elif select_option == 'd':
        update_book(delete_book)
    elif select_option == 'r':
        update_book(mark_book_as_read)
    else:
        print(f"you entered '{select_option}' and it's invalid.")

    select_option = input(menu_prompt).strip().lower()
