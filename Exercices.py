nearby_people = {"Islam", "Mohamed", "Haitham"}
user_friend = set()

friend = input("Enter your friend's name to see if he is nearby: ")

user_friend.add(friend)

soltuion = user_friend.intersection(nearby_people)
comma_seperated = ",".join(soltuion)
output_message = "Good for you, we've found a nearby friend, {} is here! "

print(f"Good for you, we've found a nearby friend, '{comma_seperated}' is here! ")









