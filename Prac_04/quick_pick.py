
import random

numbers_per_line = 6
smallest_number = 1
largest_number = 45

number_of_quick_picks = int(input("How many quick picks: "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(numbers_per_line):
        number = random.randint(smallest_number, largest_number)
        while number in quick_pick:
            # if number is repeated, get another random number
            number = random.randint(smallest_number, largest_number)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))


