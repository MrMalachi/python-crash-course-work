# This program iterates through a list of numbers & displays each as an ordinal number

# List of numbers 1 - 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Looping through every number in the list 'numbers'
for number in numbers:
    if number == 1: # using conditionals based on ordinal number endings
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

