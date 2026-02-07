"""
This program polls users about their dream vacation. It contains a prompt
similar to 'If you could visit one place in the world, where would you go?'
It also includes a block of code that prints the results of the poll.
"""

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ").title()
    vacation_location = input(
        "If you could visit and vacation in one place in the world, "
        "where would you go? ").title()
    responses[name] = vacation_location

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == "no":
        polling_active = False

print("\n\t--- POLL RESULTS ---")
for name, vacation_location in responses.items():
    print(f"{name} would like to vacation in {vacation_location}.")