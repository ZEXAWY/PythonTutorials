# def multigreet(*args):   # or we replace *args with a good variable name like 'name' or 'names'
#     for name in args:
#         print(f"Hello, {name}")
        
# multigreet("Ahmed", "Moahamed", "Zakaria")


# def multigreets(*names, other="None"):
#     for name in names:
#         print(f"Hello, {name}")
        
        
        
# multigreets("Ahmed", "Mohamed", "Zakaria", "Abdelrahman", "Islam")


# print(dict(name="Phil", age=29, city="Budapest", nationality="British"))


# def pretty_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# pretty_print(name="The Matrix", director="Mekadoweski", year="1995")    

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

# def print_movie(*args):
#     for value in args:
#         print(value)


# print_movie(*movie.keys()) # change the (.keys) to (.values)    and you get values instead of keys.

# def print_movies(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# print_movies(**movie)
# print_movies(studio="BruceLee", **movie)

