"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

# TODO: Using a for loop with the range function and string formatting,
# produce the following output:
#   0
#  50
# 100
for n in range(0,101,50):
    print('{:>5}'.format(n))

import random
print(random.randint(5, 20)) #line 1
print(random.randrange(3, 10, 2)) #line 2
print(random.uniform(2.5, 5.5)) #line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
## Smallest: 5
## Biggest: 19

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
## Smallest: 3
## Biggest: 9
# Could line 2 have produced a 4?
## No

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
## Smallest: 2.5
## Biggest: Can be any number less than 5.5 (eg. 5.4999)
