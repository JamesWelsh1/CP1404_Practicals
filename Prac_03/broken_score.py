"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = get_score()
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_score():
    score = float(input("Enter score: "))
    return score


main()
