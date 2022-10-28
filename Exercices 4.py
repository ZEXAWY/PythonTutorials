import random

lottery_number = set(random.sample(range(22), 6))
players = [
    {'name': 'Rolf', 'Sorted_numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'Sorted_numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'Sorted_numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'Sorted_numbers': {19, 20, 12, 7, 3, 5}}
]

top_player = players[0]
for player in players:
    matched_number = len(player['Sorted_numbers'].intersection(lottery_number))
    if matched_number > len(top_player['Sorted_numbers'].intersection(lottery_number)):
        top_player = player

wining = 100 ** len(top_player['Sorted_numbers'].intersection(lottery_number))
print('{} won {}.'.format(top_player['name'], wining))
