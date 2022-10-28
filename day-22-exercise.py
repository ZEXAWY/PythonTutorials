# 1-
numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

totals = map(sum, numbers)

print(next(totals))
print(next(totals))
print(next(totals))
print(next(totals))
print(next(totals))

# 2-
import itertools

employees = itertools.cycle(["Peter", "Fiona", "Carl", "Helen"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
for day in range(1, 32):
    print(f"Day {day} ({next(days)}): {next(employees)} closes.")
