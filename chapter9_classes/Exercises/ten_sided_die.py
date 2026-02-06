"""Utilize the dice_module to import the Die class."""

from dice_module import Die

# Calling the method 'roll_die' later will take the value it returns

# Create an instance from the 'Die' class and assign it to the object 'die'.
ten_die = Die(10)   # Ten sided die.

# Assign an empty list to the variable 'die_results'.
die_results = []

# Use a for loop to iterate 10 times.
for roll in range(10):
    # Store the result of the method on the object in a variable.
    result = ten_die.roll_die()
    # Add to the end of the empty list the variable that contains a random int.
    die_results.append(result)

print(f"You rolled the following with a 10-sided die:")
print(die_results)