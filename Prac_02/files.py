output_file = "name.txt"
name_file = open(output_file, 'w')
user_name = input("Please enter your name: ")
print(user_name, file =name_file)
name_file.close()

name_file = open(output_file, 'r')
print("Your name is: {}".format(name_file.readline()))
name_file.close()

numbers_file = open("numbers.txt", 'r')
number_1 = int(numbers_file.readline())
number_2 = int(numbers_file.readline())
print(number_1 + number_2)
numbers_file.close()

numbers_file = open("numbers.txt", 'r')
calculated_total = 0
for line in numbers_file:
    number = int(line)
    calculated_total += number
print(calculated_total)
numbers_file.close()
