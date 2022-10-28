file = open("data.txt")
read_file = file.read()
file.close()
print(read_file)
user_input = input("tell me how you do today? ")
file = open("write_example.txt", "w")
file_write = file.write(user_input)
file.close()


