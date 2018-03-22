"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When an integer (whole number) is not entered
2. When will a ZeroDivisionError occur?
When the denominator is entered as 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator is 0:
        print("Please enter a non-zero integer as the denominator")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero! ")
print("Finished.")
