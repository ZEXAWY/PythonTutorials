import random

guess = random.randint(1, 101)
user_number = int(input("Guess the y: "))
while user_number != guess:
    if user_number > guess:
        print(f"You guessed ({user_number}), and it's higher than the y.")
    elif user_number < guess:
        print(f"You guessed ({user_number}), and it's lower than the y.")

    user_number = int(input("Guess the y: "))
else:
    print(f"You guessed ({user_number}), and that's correct.")
