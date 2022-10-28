# 1-
from operator import methodcaller

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]


def line_separator(line):
    return line.strip()


print(*map(methodcaller("strip"), humpty_dumpty), sep="\n")
# 2-
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
new_names = [name.title() for name in names if len(name) < 8]
print()
print(new_names)
print()
names_title = map(methodcaller("title"), filter(lambda name: len(name)<8, names))
print(*names_title, sep=", ")

print()
print(*filter(lambda number: number > 0, range(-5, 21)), sep=", ")

positive = list(filter(lambda number: number > 0, range(-5, 21)))
print(positive)
even_positive = filter(lambda number: number % 2 == 0, positive)
print(*even_positive)
