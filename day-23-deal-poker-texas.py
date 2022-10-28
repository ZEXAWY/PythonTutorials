import itertools
import random


def shuffle_deck(cards):
    deck = list(cards)
    random.shuffle(deck)

    return iter(deck)


def get_player():
    while True:
        number_of_player = input("how many players are there? ").strip()

        try:
            number_of_player = int(number_of_player)
        except ValueError:
            print("you must enter an integer")
        else:
            if number_of_player in range(2, 11):
                return number_of_player
            elif number_of_player < 2:
                print("you must have at least two player.")
            else:
                print("you can have a maximum 10 player.")


def deal(card, number_of_player):
    deck = shuffle_deck(card)

    deal_to_player(deck, number_of_player)
    deal_to_table(deck)


def deal_to_player(deck, number_of_player):
    first_card = [next(deck) for _ in range(number_of_player)]
    second_card = [next(deck) for _ in range(number_of_player)]
    hands = zip(first_card, second_card)

    print()
    for i ,(first_card, second_card) in enumerate(hands, start=1):
        print(f"player {i} was dealt: {first_card}, {second_card}")

def deal_to_table(deck):
    next(deck)
    flop = ','.join(str(next(deck)) for _ in range(3))
    print(f"the flop is: {flop} ")

    next(deck)
    print(f"the turn is: {next(deck)} ")

    next(deck)
    print(f"the river is: {next(deck)} ")

    print()


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

# cards = [(rank, suit) for rank in ranks for suit in suits]
# cards = []
# for rank in ranks:
#     for suit in suits:
#         cards.append(rank,suit)

# print(cards)

cards = list(itertools.product(ranks, suits))

deal(cards, get_player())
