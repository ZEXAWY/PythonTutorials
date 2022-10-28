pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)

print(pets_and_owners)

pets_and_owners = list(zip(pet_owners, pets))
print(pets_and_owners)