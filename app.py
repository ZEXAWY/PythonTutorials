"""
Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add a movie
- See your movies
- Find your movie
- quit the program

tasks:
[]: Decide where to save their movies
[]: show to user the main interface and get their input.
[]: Allow users to add movie
[]: show all their movies
[]: find their movies
[] Allow users to stop running the program
"""

movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print("stopping the program... ")
        else:
            print("unknown command, please try again")

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input("Input movie name: ")
    director = input("Input Director name: ")
    year = input("Input the year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movies_details(movie)


def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by = input("what property you looking for? ")
    looking_by = input("What are you looking for? ")

    found_movies = find_by_attribute(movies, looking_by, lambda x: x[find_by])
    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
