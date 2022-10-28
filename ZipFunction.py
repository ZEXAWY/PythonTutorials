# The zip function:
#
# pet_owners = ["Paul", "Andrea", "Marta"]
# pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
# owners_and_pets = zip(pet_owners, pets)
# # print(list(owners_and_pets))
#
# # 1- Using zip in loops:
# for counter, (owner, pet) in enumerate(zip(pet_owners, pets), start=1):
#     print(f"{counter}- {owner} own {pet}.")

# 2- A caveat for when using enumerate and zip:
movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

# movies = zip(movie_titles, movie_directors) # consumed when requested:
movies = list(zip(movie_titles, movie_directors))

for title, director in movies:
    print(f"{title}, by {director}.")

movie_list = list(movies)

print(f"There are {len(movie_list)} movies in our collection.")
print(f"There are our movies: {movie_list}.")
