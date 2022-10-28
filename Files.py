# example_file = open("example.txt", mode="r")
# print(example_file.read())
# example_file.close()
# **********************************************************************************************************************

# write_file = open("write_example.txt", "w")
# write_file.write("Hello There you are getting in a dangerous area.")
# write_file.close()
# **********************************************************************************************************************
# write_file = open("write_example.txt", "a")
# write_file.write("\nIt's amazing progress, now i can open and add lines to the files xD.")
# write_file.close()
# **********************************************************************************************************************
with open("write_example.txt", "r") as write_file:
    print(write_file.read())