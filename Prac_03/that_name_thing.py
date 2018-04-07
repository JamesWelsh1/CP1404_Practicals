
name = input("Name: ")
while name == "":
    print("Invalid name.")
    name = input("Name: ")
print(name[::2])
