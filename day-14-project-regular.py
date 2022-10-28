menu_prompt = """Please select one of the following options:
- 'a' for adding books.
- 'l' for showing books.
- 'q' to quite.
- 'f' to find your book.

What will you choose? """

select_option = input(menu_prompt).strip().lower()


def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("year: ").strip()

    with open("books.csv", "a") as book_list:
        book_list.write(f"{title},{author},{year}\n")


def get_all_books():
    books = []

    with open("books.csv", "r") as book_list:
        for book in book_list:
            title, author, year = book.strip().split(",")
            new_book = {
                "title": title,
                "author": author,
                "year": year
            }
            books.append(new_book)

    return books


def show_book(books):
    print()

    for counter, book in enumerate(books, start=1):
        title, author, year = book.values()
        print(f"{counter}- {title} {year}, by {author}")
    print()


def find_books():
    book_list = get_all_books()
    matching_books = []
    search_term = input("Please enter a book title to search for: ").lower()
    for book in book_list:
        if search_term in book['title'].lower():
            matching_books.append(book)

    return matching_books


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
    if select_option == 'f':
        matching_book = find_books()
        if matching_book:
            print(f"We find {len(matching_book)} Book(s).")
            show_book(matching_book)
        else:
            print("Sorry, we cant get any value for that title.")
    else:
        print(f"you entered '{select_option}' and it's invalid.")

    select_option = input(menu_prompt).strip().lower()
