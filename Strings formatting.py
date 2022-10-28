# -f strings is used when you want to add an int to a str


age = 28
print(f"You are {age}")

name = "Zex"
greetings = f"How are you, {name}?"
print(greetings)

# if u changed a variable contain str after -f strings is used then it won't be changed in code
# as this example

name = "Haitham"
print(greetings)

# when you run the code it still the same as before

# another method for -f strings is .format (variable). like:

name1 = "Zex"
final_greeting = "How are you, {}?"
zex_greeting = final_greeting.format(name1)
print(zex_greeting)

name1 = "Haitham"
haitham_greeting = final_greeting.format(name1)
print(haitham_greeting)

# another way doing this

name = "Zex "
final_greeting = "How are you, {}"
zex_greeting = final_greeting.format(name)

print(zex_greeting)
print(final_greeting.format(name))
