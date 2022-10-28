books = []


def add_books():
    title = input("Please enter book title: ")
    author = input("Please enter author's name: ")
    year = input("Please enter the year of publication: ")
    books.append({
        "title": title,
        "author": author,
        "year": year
    })


def show_books():
    for counter, book in enumerate(books, start=1):
        title, author, year = book.values()
        print(f"{counter}- {title} ({year}), published by {author}.")


def menu():
    user_input = input("Enter 'a' to add books, 'l' to show books, 'f' to find books, 'q' to exit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_books()
        elif user_input == 'l':
            if books:
                show_books()
            else:
                print("You have no books.")
        elif user_input == 'f':
            find_books()
        else:
            print("Please choose one of the above choices: ")
        user_input = input("Enter 'a' to add books, 'l' to show books, 'f' to find books, 'q' to exit: ")


menu()

print("Thanks for using my Program xD \nProgram closing...")
