"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state), "is", STATE_NAMES[state]
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

for state, full_state_name in STATE_NAMES.items():
    print("{:3} is {}".format(state, full_state_name))
