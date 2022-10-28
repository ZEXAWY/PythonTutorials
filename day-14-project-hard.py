menu_prompt = """Please select one of the following options:
- 'a' for adding books.
- 'l' for showing books.
- 'f' to find your book.
- 'd' to delete book.
- 'r' to mark as read.
- 'q' to quite.

What will you choose? """

select_option = input(menu_prompt).strip().lower()


def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("year: ").strip()

    with open("books.csv", "a") as book_list:
        book_list.write(f"{title},{author},{year},Not Read\n")


def get_all_books():
    books = []

    with open("books.csv", "r") as book_list:
        for book in book_list:
            title, author, year, read = book.strip().split(",")

            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "read": read
            }
            books.append(new_book)
    books.sort(key=lambda book_: book_['title'])
    return books


def show_book(books):
    print()
    for counter, book in enumerate(books, start=1):
        title, author, year, read = book.values()
        print(f"{counter}- {title} {year}, by {author} -{read}")
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

            with open("books.csv", "w") as book_file:
                for book in books:
                    title, author, year, read = book.values()
                    book_file.write(f"{title},{author},{year},{read}\n")

        elif user_choice == 'n':
            pass
        else:
            print(f"i didn't get what you mean by that.")
    else:
        print("Sorry we didn't find any match of that title.")


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
