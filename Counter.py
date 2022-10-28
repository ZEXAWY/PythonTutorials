movies = [
    ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004),
    ("Memento", "Christopher Nolan", 2000),
    ("Requiem for a Dream", "Darren Aronofsky", 2000)
]

# counter = 1
# for title, director, year in movies:
#     print(f"{title} ({year}), directed by {director}")

# 1- Using "index" to count:
# for index in range(len(movies)):
#     print(f"{index+1}. {movies[index][0]} ({movies[index][2]}), directed by {movies[index][1]}.")

# 2- Using "counter" Variable to count for us:
# for title, director, year in movies:
#     print(f"{counter}- {title} ({year}), directed by {director}")
#     counter += 1 # += refer to (counter = counter + 1 )

# 3- Using "Enumerate" function to counter: (The Best solution)
# names = ["Ahmed", "Mohamed", "Seny"]
# for counter, name in enumerate(names):
#     print(f"{counter}- {name}.") # "counter here starts from zero, we want it to start from 1"

# for counter, name in enumerate(names, start=1):
#     print(f"{counter}- {name}.")

# 4- back to our main movies list:
# for counter, movie in enumerate(movies, start=1):
#     print(f"{counter}- {movie[0]} ({movie[2]}), by {movie[1]}")

# Or we can Use:
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}- {title} ({year}), by {director}")
